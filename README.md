# japan-anime-figure-mcp — Japan Anime Figure Price MCP Server

[![AgentHub 已收录：japan-anime-figure-mcp](https://myagenthub.cn/badge/io.github.atushi1841/japan-anime-figure-mcp)](https://myagenthub.cn/p/io.github.atushi1841/japan-anime-figure-mcp)
Read-only MCP server exposing the kensho Japan anime figure price dataset
collected from MyFigureList and other sources.

## Tools

| Tool | Description |
|---|---|
| `figure_current_price(name)` | Latest price snapshot (JPY) for a figure |
| `figure_price_history(name, limit=50)` | Price time series (oldest first) |
| `figure_lowest_price(name)` | Cheapest available across all shops |

## Data

- Source: `data/anime_figure_prices_normalized.jsonl`
- Marketplace: MyFigureList, various Japanese retailers
- No network, no API key, no account required

## Installation (Smithery)

Install via Smithery registry:
```bash
smithery install @atushi1841/japan-anime-figure-mcp
```

## More MCP Servers

- **[kensho-kaku](https://github.com/atushi1841/kensho-kaku)** — Sweepstakes from ken-kaku.com
- **[kensho-kclub](https://github.com/atushi1841/kensho-kclub)** — Sweepstakes from kenshou.club
- **[kensho-kema](https://github.com/atushi1841/kensho-kema)** — Sweepstakes from ke-ma.net
- **[kensho-sweep-mcp](https://github.com/atushi1841/kensho-sweep-mcp)** — Full pipeline sweepstakes data
- **[tcg-price-japan](https://github.com/atushi1841/tcg-price-japan)** — TCG used-price trends

## Data Source: Apify Store

The underlying dataset is also available as a managed Apify Actor:

- **[Apify Store: japan-anime-figure-price-data](https://apify.com/atushi1841/acts/japan-anime-figure-price-data)**
  (Actor ID: `DKzufUSvmuXNKHeYx`) — same anime figure price data, refreshed on a schedule

## Run

```bash
python server/server.py          # stdio MCP transport
python server/server.py --http   # streamable-http at /mcp
```

Requires `fastmcp>=3.0.0` (see `requirements.txt`).

## MCP Bundle

`manifest.json` follows the MCPB v0.4 spec. Pack with:

```bash
npx -y @anthropic-ai/mcpb pack . dist/japan-anime-figure-mcp.mcpb
```