import requests
import numpy as np
import redis
import json ,ast
from sklearn.preprocessing import MinMaxScaler
from redis.commands.json.path import Path




print('bueno')
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
     print(ticker)
     self.data.clear()
     
     self.ratios=requests.request(method='GET',url='https://financialmodelingprep.com/api/v3/ratios-ttm/'+ticker+'?apikey=b29d19c0bc11e8a86d6ed7245bf19b5e')
     self.financial=requests.request(method='GET',url='https://financialmodelingprep.com/api/v3/income-statement/'+ticker+'?limit=120&apikey=b29d19c0bc11e8a86d6ed7245bf19b5e')
     self.enterprise_value=requests.request(method='GET',url='https://financialmodelingprep.com/api/v3/enterprise-values/'+ticker+'?limit=40&apikey=b29d19c0bc11e8a86d6ed7245bf19b5e')
     
     if self.financial.json() !=[] and self.enterprise_value.json()!=[] and self.ratios.json()!=[] :
         
         if type(self.financial.json())==dict and type(self.ratios.json())==dict and type(self.enterprise_value.json())==dict:
             pass
             print("no data")
         else:
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
             self.data.clear()
             _datos_entrenos=[]
             if self._es_valido==True:

                 for keys_ in self.Fundamental:
        
                     for keys_array in self.data_keys:
            
                        if keys_==keys_array[0]:
                
            
                           self.data.append(keys_array[1])
              
             
             
             return self.data
             
     else:
   
         pass
     

 
  def DataScaler(samples:list):
      
      mean_dat=[]
      
      for i in range(dat.shape[0]):
         mean_dat.append(samples[:,i].mean())
      

      clf=MinMaxScaler()
      scale=clf.fit_transform(mean_dat) 
      
      return scale
   

if __name__ == "__main__":
    
    rdb=redis.Redis(host='localhost', port=6379, db=0)
    train_data=rdb.get("train_data")
    class_1=Create__Data()
    
    if train_data!=None:
        cn=json.load(train_data.decode())
        class_1.DataScaler(cn)
        
    else:
      dt=rdb.get("simbolos Entrenos")
      
     
      string=ast.literal_eval(dt.decode()) 
    
      string.append("AAPL")
      string.append("INTC")
      string.append("AMZ")
      val=[]
      try: 
          
       for i in string:
      
         datos=class_1.train_data(i,["quickRatioTTM","priceToFreeCashFlowsRatioTTM","priceSalesRatioTTM","ebitda","enterpriseValue"])
         val.append(datos)
         print(datos)
      except KeyError:
          pass
      
      numpy_data=np.array(val).reshape(5,len(val))
      data={"train_data":numpy_data}
      rdb.set("train_data",str(data))   
    
    
    
       
       
       
    
 