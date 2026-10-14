#!/usr/bin/env python3
"""Test script for japan-anime-figure-mcp server."""
import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from server.server import _load, _match, figure_current_price, figure_price_history, figure_lowest_price

async def test():
    rows = _load()
    print(f"Loaded {len(rows)} figures")
    
    # Test search
    matches = _match(rows, "evangelion")
    print(f"\nSearch 'evangelion': {len(matches)} matches")
    if matches:
        print(f"  First match: {matches[0].get('name')}")
    
    matches = _match(rows, "dragon quest")
    print(f"\nSearch 'dragon quest': {len(matches)} matches")
    if matches:
        print(f"  First match: {matches[0].get('name')}")
    
    # Test tools
    result = await figure_current_price("evangelion")
    print(f"\nfigure_current_price('evangelion'):")
    print(json.dumps(result, ensure_ascii=False, indent=2)[:500])
    
    result = await figure_lowest_price("evangelion")
    print(f"\nfigure_lowest_price('evangelion'):")
    print(json.dumps(result, ensure_ascii=False, indent=2)[:500])

if __name__ == "__main__":
    import asyncio
    asyncio.run(test())
