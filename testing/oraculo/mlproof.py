import requests
import numpy as np
import pandas as pd

print('HOLA')
class  Create__Data():
  
  def __init__(self):
     
     self._es_valido=False
     self.data_keys=[]
     self.Fundamental=None
     self.financial=None
     self.ratios=None
     self.enterprise_value=None
     self.data=[]
     
     
 
  def train_data(self,ticker:str,datos:list)-> list:
     
     self.ratios=requests.request(method='GET',url='https://financialmodelingprep.com/api/v3/ratios-ttm/'+ticker+'?apikey=b29d19c0bc11e8a86d6ed7245bf19b5e')
     self.financial=requests.request(method='GET',url='https://financialmodelingprep.com/api/v3/income-statement/'+ticker+'?limit=120&apikey=b29d19c0bc11e8a86d6ed7245bf19b5e')
     self.enterprise_value=requests.request(method='GET',url='https://financialmodelingprep.com/api/v3/enterprise-values/'+ticker+'?limit=40&apikey=b29d19c0bc11e8a86d6ed7245bf19b5e')
     
     financial=np.append(self.financial.json()[0],self.enterprise_value.json()[0])
     ad_=np.append(financial,self.ratios.json()[0])
     
     
     for i in range(ad_.shape[0]):
         
        data=dict(ad_[i]).items()
        
        
        
        for i in list(data):
        
             self.data_keys.append(i)
      
     self.Fundamental=datos
      
     v_=[]

     for keys_ in self.Fundamental:
        
        for keys_array in self.data_keys:
           
            if keys_==keys_array[0]:

                 v_.append(0)  
            
     if len(v_) < len(self.Fundamental): 
        pass
     else:
        self._es_valido=True
        
     if self._es_valido==True:

        for keys_ in self.Fundamental:
        
         for keys_array in self.data_keys:
            
            if keys_==keys_array[0]:

               self.data.append(keys_array[1])
     
     return self.data
   





        
  

 