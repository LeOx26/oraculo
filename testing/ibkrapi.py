
import json
import requests
import pandas as pd

class stock:

 def history(symbols, period, bar):
    reqUrl = 'https://localhost:5000/v1/api/iserver/secdef/search'
    payload = {'symbol':symbols,'name':'false','secType':'STK'}
    res = requests.request("GET", reqUrl, params=payload, verify=False )
    res.encoding = 'utf-8'
    ### Obtener los datos historicos de un contrato
    reqUrl = 'https://localhost:5000/v1/api/iserver/marketdata/history'
    payload = {'conid':res.json()[0]['conid'],'period':period,'bar':bar}
    response = requests.request("GET", reqUrl, params=payload, verify=False )
    response.encoding = 'utf-8'
    
    return response.json()

 def conid(symbols,*args):
    reqUrl = 'https://localhost:5000/v1/api/iserver/secdef/search'
    payload = {'symbol':symbols,'name':'false','secType':'STK'}
    response = requests.request("GET", reqUrl, params=payload, verify=False )
    response.encoding = 'utf-8'
    return response.json()[0]['conid']

class portafolio:

 def obtener_portafolio():
        ### Obtiene los datos de los activos en el portafolio
        reqUrl = "https://localhost:5000/v1/api/portfolio/U2794747/positions/0" 
        response = requests.request("GET", reqUrl, verify=False )
        response.encoding = 'utf-8'
        return response.json()

class scanner:
   
   
   
   def scanner_type_list(type_doc='Js'):
      """type_doc(string):'Dt'->DataFrame,'Js'->json
      """
      reqUrl = "https://localhost:5000/v1/api/iserver/scanner/params"

      headersList = {
         "Accept": "*/*",
          "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
           }
      payload = ""

      response = requests.request("GET", reqUrl, data=payload,  headers=headersList,verify=False) 
      json_=response.json()['scan_type_list']
      if type_doc=='Dt':
           return pd.DataFrame(json_)
      elif type_doc=='Js':
           return json_
   
   
   def scanner_run(instrument="",type=""):

      reqUrl = "https://localhost:5000/v1/api/iserver/scanner/run"

      headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/json" 
        }

      payload = json.dumps({
      "instrument": instrument,
      "type": type,
      "filter": [
      {
      "code": "",
      "value": 0
      }
     ],
      "location": "",
       "size": ""
     })

      response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
      resp=response.json()

      return pd.DataFrame(resp)


         


          
      
           
       
       

      
