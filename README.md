# japan-anime-figure-mcp

**MCP server for Japanese anime figure price data — scraping used-good prices from Mandarake, Surugaya, Yahoo Auctions Japan, Mercari Japan, and Rakuten.**

An [MCP](https://modelcontextprotocol.io/) server that gives AI agents access to **current Japanese anime figure market prices** with citations. Every response carries `sources` and `data_gaps`.

Built for collectors, AI agents, and developers who need price tracking without manual scraping.

---

## Why this exists

Japanese anime figure prices are scattered across multiple platforms (Mandarake, Surugaya, Yahoo Auctions, Mercari) with no unified API. This server normalizes them behind **read-only tools**.

- **Free** — no API key required
- **Cited** — every response includes source URLs
- **Honest** — failures reported in `data_gaps`, never silently dropped

## Tools

| Tool | Description | Source |
|------|-------------|--------|
| `search_figures(keyword, limit)` | Search across Mandarake, Surugaya, Yahoo Auctions | Multi-platform |
| `get_price_trend(item_id, days)` | Historical price trend (last N days) | Apify Actor |
| `get_category_list()` | Available categories (figures, scale models, etc.) | Internal |

## Install

```bash
pip install -e .
```

## Usage

```bash
japan-anime-figure-mcp          # stdio mode
python -m japan_anime_figure_mcp.server
```

### Claude Code

```json
{
  "mcpServers": {
    "japan-anime-figure": {
      "command": "python",
      "args": ["-m", "japan_anime_figure_mcp.server"]
    }
  }
}
```

## Install via Smithery

```bash
npx -y @smithery/cli install atushi1841/japan-anime-figure-mcp
```

## Related

- [Apify Actor: japan-anime-figure-price-scraper](https://apify.com/atushi1841/japan-anime-figure-price-scraper)
- [Kensho Apify Bundle](https://github.com/atushi1841/kensho-actor-showcase)

## License

MIT
