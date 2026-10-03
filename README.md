# japan-anime-figure-mcp — Japan Anime Figure Price MCP Server

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
