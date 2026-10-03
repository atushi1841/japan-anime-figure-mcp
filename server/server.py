#!/usr/bin/env python3
"""japan-anime-figure-mcp MCP server (MCPB bundle entry point).

Exposes the kensho Japan anime figure price dataset as read-only MCP tools
for AI agents.

Tools:
  - figure_current_price(name) -> latest price snapshot
  - figure_price_history(name, limit=50) -> time series
  - figure_lowest_price(name) -> cheapest available across shops

Data source: bundled data/anime_figure_prices_normalized.jsonl (read-only).
No network, no API key required.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Optional

from fastmcp import FastMCP

DATA = Path(__file__).resolve().parent.parent / "data" / "anime_figure_prices_normalized.jsonl"

server = FastMCP("japan-anime-figure-mcp")


def _load() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not DATA.exists():
        return rows
    with DATA.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def _match(rows: list[dict[str, Any]], name: str) -> list[dict[str, Any]]:
    q = name.strip().lower()
    if not q:
        return rows
    out = []
    for r in rows:
        blob = " ".join([
            str(r.get("name", "")),
            str(r.get("series", "")),
            str(r.get("character", "")),
            str(r.get("manufacturer", "")),
            str(r.get("source_url", "")),
        ]).lower()
        if q in blob:
            out.append(r)
    return out


@server.tool()
async def figure_current_price(name: str) -> dict[str, Any]:
    """Current price snapshot for an anime figure in the Japan dataset.

    Args:
        name: figure name, series, character, or URL substring.
    Returns the latest observed price snapshot plus match count.
    """
    rows = sorted(_match(_load(), name), key=lambda r: r.get("fetched_at", ""))
    if not rows:
        return {"name": name, "matches": 0, "error": "no matching figure in dataset"}
    latest = rows[-1]
    offers = latest.get("offers", [])
    in_stock = [o for o in offers if o.get("availability") == "InStock"]
    return {
        "name": latest.get("name"),
        "series": latest.get("series"),
        "character": latest.get("character"),
        "manufacturer": latest.get("manufacturer"),
        "category": latest.get("category"),
        "matches": len(rows),
        "lowest_price_jpy": latest.get("lowest_price_jpy"),
        "highest_price_jpy": latest.get("highest_price_jpy"),
        "msrp_jpy": latest.get("msrp_jpy"),
        "in_stock_count": latest.get("in_stock_count"),
        "total_offers": latest.get("total_offers_count"),
        "in_stock_offers": in_stock[:5],
        "all_offers": offers[:10],
        "fetched_at": latest.get("fetched_at"),
        "source_url": latest.get("source_url"),
    }


@server.tool()
async def figure_price_history(name: str, limit: int = 50) -> dict[str, Any]:
    """Price time series for an anime figure in the Japan dataset.

    Args:
        name: figure name or URL substring.
        limit: max number of history rows to return (default 50).
    Returns oldest-first observations of lowest/highest prices (JPY).
    """
    rows = sorted(_match(_load(), name), key=lambda r: r.get("fetched_at", ""))
    if not rows:
        return {"name": name, "matches": 0, "error": "no matching figure in dataset"}
    hist = [
        {
            "fetched_at": r.get("fetched_at"),
            "lowest_price_jpy": r.get("lowest_price_jpy"),
            "highest_price_jpy": r.get("highest_price_jpy"),
            "in_stock_count": r.get("in_stock_count"),
        }
        for r in rows[-limit:]
    ]
    return {"name": name, "matches": len(rows), "history": hist}


@server.tool()
async def figure_lowest_price(name: str) -> dict[str, Any]:
    """Cheapest available price for an anime figure across all shops.

    Args:
        name: figure name or URL substring.
    Returns the lowest-priced in-stock offer.
    """
    rows = _match(_load(), name)
    if not rows:
        return {"name": name, "matches": 0, "error": "no matching figure in dataset"}
    
    # Get latest observation
    latest = max(rows, key=lambda r: r.get("fetched_at", ""))
    offers = latest.get("offers", [])
    in_stock = [o for o in offers if o.get("availability") == "InStock"]
    
    if not in_stock:
        # Return any offer if none in stock
        best = min(offers, key=lambda o: o.get("price_jpy", float("inf"))) if offers else None
    else:
        best = min(in_stock, key=lambda o: o.get("price_jpy", float("inf")))
    
    return {
        "name": latest.get("name"),
        "series": latest.get("series"),
        "character": latest.get("character"),
        "matches": len(rows),
        "lowest_price_jpy": best.get("price_jpy") if best else None,
        "shop": best.get("shop_name") if best else None,
        "url": best.get("url") if best else None,
        "condition": best.get("condition") if best else None,
        "fetched_at": best.get("fetched_at") if best else None,
    }


if __name__ == "__main__":
    server.run(transport="stdio")
