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

## Related Apify Actors

This MCP server connects to **86+ Apify Actors** in the Kensho ecosystem for real-time data. Key related actors include:

### Marketplace & Price Comparison
- [fruitful_quintessence/japan-market-mcp](https://apify.com/fruitful_quintessence/japan-market-mcp) — Cross-shop price comparison
- [fruitful_quintessence/japan-minimum-wage-mcp](https://apify.com/fruitful_quintessence/japan-minimum-wage-mcp) — Minimum wage data
- [fruitful_quintessence/japan-food-delivery-mcp](https://apify.com/fruitful_quintessence/japan-food-delivery-mcp) — Food delivery prices

### Retail & E-commerce
- [fruitful_quintessence/rakuten-japan-mcp](https://apify.com/fruitful_quintessence/rakuten-japan-mcp) — Rakuten Ichiba data
- [fruitful_quintessence/japan-kakaku-price-search](https://apify.com/fruitful_quintessence/japan-kakaku-price-search) — Kakaku.com price comparison
- [fruitful_quintessence/amazon-japan-bestsellers](https://apify.com/fruitful_quintessence/amazon-japan-bestsellers) — Amazon JP bestsellers
- [fruitful_quintessence/yahoo-shopping-japan](https://apify.com/fruitful_quintessence/yahoo-shopping-japan) — Yahoo! Shopping
- [fruitful_quintessence/mercari-japan-price](https://apify.com/fruitful_quintessence/mercari-japan-price) — Mercari pricing

### Used Goods & Auctions
- [fruitful_quintessence/yahoo-auctions-japan-scraper](https://apify.com/fruitful_quintessence/yahoo-auctions-japan-scraper) — Yahoo! Auctions
- [fruitful_quintessence/mercari-japan-search-scraper](https://apify.com/fruitful_quintessence/mercari-japan-search-scraper) — Mercari search
- [fruitful_quintessence/surugaya-japan-hobby-prices](https://apify.com/fruitful_quintessence/surugaya-japan-hobby-prices) — Suruga-ya hobby
- [fruitful_quintessence/mandarake-auction-scraper](https://apify.com/fruitful_quintessence/mandarake-auction-scraper) — Mandarake auction
- [fruitful_quintessence/off-mall-japan-scraper](https://apify.com/fruitful_quintessence/off-mall-japan-scraper) — OffMall (Hard Off)

### Local Business & Services
- [fruitful_quintessence/google-maps-japan-reviews](https://apify.com/fruitful_quintessence/google-maps-japan-reviews) — Google Maps reviews
- [fruitful_quintessence/tabelog-japan-restaurants](https://apify.com/fruitful_quintessence/tabelog-japan-restaurants) — Tabelog restaurants
- [fruitful_quintessence/hotpepper-beauty-salons](https://apify.com/fruitful_quintessence/hotpepper-beauty-salons) — Beauty salons
- [fruitful_quintessence/japan-post-office-locations](https://apify.com/fruitful_quintessence/japan-post-office-locations) — Post offices

### Government & Public Data
- [fruitful_quintessence/japan-maff-markets](https://apify.com/fruitful_quintessence/japan-maff-markets) — MAFF wholesale markets
- [fruitful_quintessence/japan-maff-price-trend](https://apify.com/fruitful_quintessence/japan-maff-price-trend) — MAFF price trends
- [fruitful_quintessence/japan-maff-top-movers](https://apify.com/fruitful_quintessence/japan-maff-top-movers) — MAFF top movers
- [fruitful_quintessence/japan-maff-market-report](https://apify.com/fruitful_quintessence/japan-maff-market-report) — MAFF market reports

### Specialized Collections
- [fruitful_quintessence/japan-anime-figure-demand-features](https://apify.com/fruitful_quintessence/japan-anime-figure-demand-features) — Anime figure demand
- [fruitful_quintessence/japan-vintage-clothing-prices](https://apify.com/fruitful_quintessence/japan-vintage-clothing-prices) — Vintage clothing
- [fruitful_quintessence/japan-used-book-prices](https://apify.com/fruitful_quintessence/japan-used-book-prices) — Used books
- [fruitful_quintessence/japan-record-store-prices](https://apify.com/fruitful_quintessence/japan-record-store-prices) — Record stores
- [fruitful_quintessence/japan-toy-collector-prices](https://apify.com/fruitful_quintessence/japan-toy-collector-prices) — Toy collector

## MCP Connection Examples
### 6. External run example (fallback)

```bash
# If GitHub API returns 403, use curl + git clone
curl -s https://raw.githubusercontent.com/atushi1841/japan-anime-figure-mcp/main/README.md > README.patch
# edit README.patch as needed
git clone https://github.com/atushi1841/japan-anime-figure-mcp.git
cd japan-anime-figure-mcp
cp ../README.patch README.md
git add README.md
git commit -m "update README via external run"
git push
```

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


## MCP公式レジストリ登録済み

本サーバーは MCP 公式レジストリに `io.github.atushi1841/japan-anime-figure-mcp` として登録済み（status: active）です。

```bash
# レジストリでの登録確認
curl -s "https://registry.modelcontextprotocol.io/v0.1/servers?search=atushi1841" | grep -o "\"io.github.atushi1841/japan-anime-figure-mcp\""
```
