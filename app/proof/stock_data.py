import numpy as np
import requests
import yfinance as yf
from yfinance import base
from datetime import datetime

class data:

  def __init__(self,ticker='') -> None:
     self.ticker=ticker
     self._info=None
     self.data=list()
     self.profile=None
     pass

  def tingo_data(self):
    url="https://www.tiingo.com/asset/assetdetails?assetTicker="+self.ticker
    headersList = {
       "Accept": "*/*",
       "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
                  }      
    payload = ""
    response=requests.request(method="GET",url=url,data=payload,headers=headersList)
    return response.json()
  
  
  def yahoo_data(self,time=str):
    url="https://query1.finance.yahoo.com/v8/finance/chart/"+self.ticker+"?region=US&lang=en-US&includePrePost=false&interval=1d&useYfid=true&range=1y&corsDomain=finance.yahoo.com&.tsrc=finance"
    headersList = {
       "Accept": "*/*",
       "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
                  }      
    payload = ""
    response=requests.request(method="GET",url=url,data=payload,headers=headersList)
    self._info=response.json()
    
   # dict_price={
      #"timestamp":self._info['chart']['result'][0]['timestamp'],
      #"Open":self._info['chart']['result'][0]['indicators']['quote'][0]['open'],
      #"high":self._info['chart']['result'][0]['indicators']['quote'][0]['high'],
      #"low":self._info['chart']['result'][0]['indicators']['quote'][0]['low'],
      #"close":self._info['chart']['result'][0]['indicators']['quote'][0]['close']
    #}
    size_data=len(self._info['chart']['result'][0]['timestamp'])
    chart=self._info['chart']['result'][0]['indicators']['quote'][0]
    if time=="ip":
     for i in range(size_data):
        data=[self._info['chart']['result'][0]['timestamp'][i],chart['open'][i],chart['high'][i],chart['low'][i],chart['close'][i],chart['volume'][i]]
        self.data.append(data)
    else:
       
       for i in range(size_data):
         ts=datetime.utcfromtimestamp(self._info['chart']['result'][0]['timestamp'][i]).strftime('%Y-%m-%d %H:%M:%S')
         data_date={"time":ts,"value":chart['close'][i]}
         self.data.append(data_date)
    return self.data
  
  
  def profile_share(self):
      
    info=base.TickerBase(self.ticker).stats()

    if info['price'][ 'quoteType']=="EQUITY":
    
     self.profile={
         'sector':info['summaryProfile']['sector'],
         'profile':info['summaryProfile']['longBusinessSummary'],
         'industry':info['summaryProfile']['industry'],
         'market':{
            'name':info['price']['shortName'],
            'symbol':info['price']['symbol'],
            'exchange':info['price']['exchangeName'],
            'price':info['price']['regularMarketPrice'],
            'marketcap':info['price']['marketCap'],
            'quoteType':info['price'][ 'quoteType'],
            'currency':info['price']['currency']}
}
    elif info['price'][ 'quoteType']=="ETF":
      self.profile={
         'sector':None,
         'profile':info['assetProfile']['longBusinessSummary'],
         'industry':None,
         'market':{
            'name':info['price']['shortName'],
            'symbol':info['price']['symbol'],
            'exchange':info['price']['exchangeName'],
            'price':info['price']['regularMarketPrice'],
            'marketcap':info['price']['marketCap'],
            'quoteType':info['price'][ 'quoteType'],
            'currency':info['price']['currency']}
         }

    return self.profile
  
  def fundamentals(self):
      
       url="https://query2.finance.yahoo.com/v10/finance/quoteSummary/"+self.ticker+"?formatted=true&crumb=sm3xpA2Nbv.&lang=en-US&region=US&modules=incomeStatementHistory%2CcashflowStatementHistory%2CbalanceSheetHistory%2CincomeStatementHistoryQuarterly%2CcashflowStatementHistoryQuarterly%2CbalanceSheetHistoryQuarterly&corsDomain=finance.yahoo.com"
       headersList = {
       "Accept": "*/*",
       "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
                  }      
       payload = ""
       response=requests.request(method="GET",url=url,data=payload,headers=headersList)
      
       return response.json()
       
  

