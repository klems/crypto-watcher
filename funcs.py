#!/usr/bin/python

import requests

def getBtcInWallet(address):
   """
   Return the number of BTC in a given address using blockchain.info
   """
   btc = 'https://blockchain.info/q/addressbalance/' + address
   check = requests.get(btc)
   value = int((check.content)) / 100000000.0
   return value
   
def getChange(coin,interval):
   """
   Return the change of a coin value for the last (1h/24h/7d) using the coinmarketcap API
   """
   change = 'https://api.coinmarketcap.com/v1/ticker/' + coin
   json = requests.get(change).json()
   value = json[0]['percent_change_' + str(interval)]
   return value
   
def getPrice(coin,cur):
   """
   Return the price of a coin in USD/BTC using the coinmarketcap API
   """
   price = 'https://api.coinmarketcap.com/v1/ticker/' + coin
   json = requests.get(price).json()
   value = json[0]['price_' + str(cur)]
   return value

if __name__ == "__main__":
   print('Checking --> getBtcInWallet')
   btc = getBtcInWallet('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa')
   print ('The Genesis Bitcoin address still holds = ' + str(btc) + ' BTC')
   print ('')
   print('Checking --> getChange')
   change1h = getChange('bitcoin','1h')
   print ('Change of Bitcoin value for the last hour = ' + change1h + ' %')
   change24h = getChange('bitcoin','24h')
   print ('Change of Bitcoin value for the last 24 hours = ' + change24h + ' %')
   change7d = getChange('bitcoin','7d')
   print ('Change of Bitcoin value for the last week = ' + change7d + ' %')
   print ('')
   print('Checking --> getPrice')
   moneroUsd = getPrice('monero','usd');
   print ('Price for a single monero in US dollars = ' + moneroUsd + ' $');
   moneroBtc = getPrice('monero','btc');
   print ('Price for a single monero in Bitcoin = ' + moneroBtc + ' BTC');
