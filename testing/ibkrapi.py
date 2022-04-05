import requests

class market_data:

    def __init__(self) -> None:
        pass

    def history(self,symbols, period, bar):

        # Obtener id del simbolo
        self.reqUrl = 'https://localhost:5000/v1/api/iserver/secdef/search'
        self.payload = {'symbol':symbols,'name':'false','secType':'STK'}
        self.response = requests.request("GET", self.reqUrl, params=self.payload, verify=False )
        self.response.encoding = 'utf-8'

        ### Obtener los datos historicos de un contrato
        self.reqUrl = 'https://localhost:5000/v1/api/iserver/marketdata/history'
        self.payload = {'conid':self.response.json()[0]['conid'],'period':period,'bar':bar}
        self.response = requests.request("GET", self.reqUrl, params=self.payload, verify=False )
        self.response.encoding = 'utf-8'
        return self.response.json()


    def conid(symbols):

        reqUrl = 'https://localhost:5000/v1/api/iserver/secdef/search'
        payload = {'symbol':symbols,'name':'false','secType':'STK'}
        response = requests.request("GET", reqUrl, params=payload, verify=False )
        response.encoding = 'utf-8'
        return response.json()[0]['conid']

class potafolio:

    def obtener_portafolio(self):
        ### Obtiene los datos de los activos en el portafolio
        reqUrl = "https://localhost:5000/v1/api/portfolio/U2794747/positions/0" 
        response = requests.request("GET", reqUrl, verify=False )
        response.encoding = 'utf-8'
        return response.json()