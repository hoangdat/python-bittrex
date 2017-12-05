from bittrex import Bittrex, API_V2_0, API_V1_1, BUY_ORDERBOOK, TICKINTERVAL_ONEMIN
import json
#666c43de4e0244c6b090040beacf64b2
#Secret:9e707a83bfea41b99e85aff8c49163b2


btrex = Bittrex("666c43de4e0244c6b090040beacf64b2",
                "9e707a83bfea41b99e85aff8c49163b2",
                api_version=API_V1_1)
cur = btrex.get_currencies()
market = btrex.get_markets()
print(market)

results = market['result']

name_key = 'name'
market_key = 'market_name'
market_cur_key = 'market_cur'
logo_key = 'logo'

btc_cur = []
eth_cur = []
usdt_cur = []

for coin in results:
    if coin['IsActive'] is True:
        marketName = str(coin['MarketName'])
        tmp_market = dict()
        tmp_market[name_key] = coin['MarketCurrencyLong']
        tmp_market[market_key] = marketName
        tmp_market[market_cur_key] = coin['MarketCurrency']
        tmp_market[logo_key] = coin['LogoUrl']
        if marketName.startswith('BTC'):
            btc_cur.append(tmp_market)
        elif marketName.startswith('ETH'):
            eth_cur.append(tmp_market)
        elif marketName.startswith('USDT'):
            usdt_cur.append(tmp_market)

with open('btc_market.json', 'w') as outfile:
    btc = dict()
    btc['markets'] = btc_cur
    json.dump(btc, outfile)

with open('eth_market.json', 'w') as outfile:
    eth = dict()
    eth['markets'] = eth_cur
    json.dump(eth, outfile)

with open('usdt_market.json', 'w') as outfile:
    usdt = dict()
    usdt['markets'] = usdt_cur
    json.dump(usdt, outfile)

print(cur)
