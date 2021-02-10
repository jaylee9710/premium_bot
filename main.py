import pandas as pd
import numpy as np
import requests
import pyupbit
import pprint
from binance_API_key import api_key, api_secret
from binance.client import Client
clientB = Client(api_key, api_secret)
from coin_list import coin_list
from bs4 import BeautifulSoup

#---업비트 가격 정보 호출---
upbit_KRW_list = []
for i in range(len(coin_list)):
    upbit_KRW_list.append('KRW-'+coin_list[i])

print(pyupbit.get_current_price(upbit_KRW_list))

#---바이낸스 가격 정보 호출---
#pprint.pprint(clientB.get_all_tickers())
binance_get = clientB.get_all_tickers()
binance_USDT_symbol_list = []
for i in range(len(coin_list)):
    binance_USDT_symbol_list.append(coin_list[i]+'USDT')
#print(binance_USDT_symbol_list)
binance_USDT_list = []
for i in range(len(binance_USDT_symbol_list)):
    binance_USDT_list.append(next((item for item in binance_get if item['symbol'] == binance_USDT_symbol_list[i]), None))

print(binance_USDT_list)

#---환율 정보 호출---
url_naver_finance = 'http://finance.naver.com/'
res = requests.get(url_naver_finance)
text = res.text
soup = BeautifulSoup(text, 'html.parser')
td = soup.select_one("#content > div.article2 > div.section1 > div.group1 > table > tbody > tr > td")
print(td.text) #환율



data_frame = pd.DataFrame({
    'Coin List' : coin_list,
    'Upbit' : coin_list,
    'Binance' :
})

# let notiHistory = [{symbol: "abc", timestamp: 123456789}]
# #이렇게 메모리에 남기고
# #보낼때 최근 알람 시간 검사
# if (alertHistory.find(coin=>coin.symbol === "abc").timestamp < Date(지금 - 알림주기)) {
# 텔레그램알림api()
# notiHistory = notiHistory.filter(coin=>coin.symbol !== "abc")
# notiHistory.push({symbol: "abc", timestamp: Date(지금)})
# }