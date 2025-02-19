from google.cloud import bigquery,bigquery_v2
from google.oauth2 import service_account
import json
import numpy as np
import req
import datetime as dt
import ast

key_path="/home/leox/projects/.std/oraculoTf.json"
credentials = service_account.Credentials.from_service_account_file(key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])

global client
client=bigquery.Client(credentials=credentials)

class bigqueryStorage():
    
 def  __init__(self):
   
    self.schema_simbolo_data=[
    bigquery.SchemaField("symbol","STRING"),
    bigquery.SchemaField("cik", "STRING"),
    bigquery.SchemaField("data", "JSON")
    ]
    self.cik_schema=[bigquery.SchemaField("date","STRING"),
    bigquery.SchemaField("data", "JSON")]
    
    self.dataset_babynames_id=client.dataset('babynames')
    self.dataset_CIKLIST_id=client.dataset('ListCik',)
    

 def InsertData(self,cik:str,symbol:str):
     
  data_=req._req_fundamentals(cik)
  
  tables = bigquery.Table(client.dataset('babynames').table(symbol.upper()),self.schema_simbolo_data)
  data = [ 
   
    {"symbol" : symbol, "cik" : cik, "data" : json.dumps(data_)}
    ]
  client.insert_rows(tables, data)
  
 def crear_tablas_babynames(self,table_nombre:str):
    #flyte
   name=table_nombre.upper()
   table = bigquery.Table(self.dataset_babynames_id.table(name), schema=self.schema_simbolo_data)
   table = client.create_table(table) 
   print("tabla creada")
 
 def crearListCIKtables(self):
    #flyte
      time=dt.date.today().strftime("%Y-%m-%d")
      table=bigquery.Table(self.dataset_CIKLIST_id.table('CIKS'),self.cik_schema)
      data=req._req_cik_list()
      row=[{"date":time,"data":json.dumps(data)}]
      client.insert_rows(table,row)
  
 def get_list_Cik(self) -> list:
     data=[]
     
     table=bigquery.Table(self.dataset_CIKLIST_id.table('CIKS'),self.cik_schema)
     i_table=client.list_rows(table)
     for i in i_table:
        data.append(i[1])
     
     return data[0]
 def get_data(self,simbolo): 
     data=[]
     
     table = bigquery.Table(self.dataset_babynames_id.table(simbolo), schema=self.schema_simbolo_data)
     i_table=client.list_rows(table)
     for i in i_table:
        data.append(i[2])
     
     return data[-1]        
  
def zeros (num) ->str:
   zeros_length=10-len(num)
   array_zeros=np.zeros(zeros_length,dtype=int)

   return ''.join(str(i) for i in array_zeros)+num

    
    
    
    
    
    
 

#export GOOGLE_APPLICATION_CREDENTIALS="/home/leox/projects/.std/oraculoTf.json"