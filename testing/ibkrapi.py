
import requests

class stock:

 def history(symbols, period, bar):
    # Obtener id del simbolo
    reqUrl = 'https://localhost:5000/v1/api/iserver/secdef/search'
    payload = {'symbol':symbols,'name':'false','secType':'STK'}
    response = requests.request("GET", reqUrl, params=payload, verify=False )
    response.encoding = 'utf-8'
    ### Obtener los datos historicos de un contrato
    reqUrl = 'https://localhost:5000/v1/api/iserver/marketdata/history'
    payload = {'conid':response.json()[0]['conid'],'period':period,'bar':bar}
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
