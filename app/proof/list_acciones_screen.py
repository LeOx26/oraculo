
from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from stock_data import data
from yfinance import base
from redis.commands.json.path import Path
import redis as rd
import pandas as pd

server=rd.Redis(host='localhost', port=6379, db=0)


DAG(dag_id='list_acciones_screener',
schedule='@monthly',
start_date=datetime(2022,11,3),
tags=['task']
)

def cargar_data(ticker=''):

    estadis=base.TickerBase(ticker).stats()
    if estadis=={}:
      pass
    else:
     estadis_info=estadis['defaultKeyStatistics']
     fundamental=data(ticker)
    
     quotetype=estadis['price']['quoteType']
     if quotetype=='ETF':
        return {'response':'informacion de ETF no disponible'}
     elif fundamental.fundamentals()['quoteSummary']['result'][0]['incomeStatementHistoryQuarterly']['incomeStatementHistory']==[]:
           pass
     else:
      info=fundamental.fundamentals()['quoteSummary']['result'][0]['incomeStatementHistoryQuarterly']['incomeStatementHistory'][0]       
    #finanza
      net_income_json=info['netIncome']['raw']
      revenue_json=info['totalRevenue']['raw']
      profit_json=info['grossProfit']['raw']
      deuda=estadis['financialData']['totalDebt']
      ebit=info['ebit']['raw']
      
      revenue_accion=revenue_json/estadis_info['sharesOutstanding']
      deuda_accion=deuda/estadis_info['sharesOutstanding']
      dvdendo=estadis['earnings']

      if fundamental.fundamentals()['quoteSummary']['result'][0]['incomeStatementHistoryQuarterly']['incomeStatementHistory'][1]['totalRevenue']['raw']==0 or dvdendo==None:
         crecimineto_=0
         dvdendo=0
      else:
        dvdendo=estadis['earnings']
        por=fundamental.fundamentals()['quoteSummary']['result'][0]['incomeStatementHistoryQuarterly']['incomeStatementHistory'][0]['totalRevenue']['raw']*100/fundamental.fundamentals()['quoteSummary']['result'][0]['incomeStatementHistoryQuarterly']['incomeStatementHistory'][1]['totalRevenue']['raw']
        crecimineto_=por-100
        dvdendo=dvdendo['earningsChart']
     
      fundamental={'finanzas':{
            'netincome':net_income_json,
            'revenue':revenue_json,
            'profit':profit_json,
            'deuda':deuda,
            'ebit':ebit,
           },
           'estadistica':{
            'ganancias/accion':revenue_accion,
            'deuda/accion':deuda_accion,
            'dividendo':dvdendo,
            'crecimiento':round(crecimineto_,2)
           }
     }
     


     
     return fundamental
@task(id='cargar_datos_al_server')
    
def server_data():

    simbolos=pd.read_csv('nasdaq_screener.csv')["Symbol"].values
    lengh=len(simbolos)
    for i in range(lengh):
         data=cargar_data(simbolos[i])
         data_error=str(data)
         if data_error=="{'response':'informacion de ETF no disponible'}":
             pass
         else:
            server.hset('data entreno',simbolos[i],str(data))
         print(str(i)+"/"+str(lengh))

          
        
    






  
