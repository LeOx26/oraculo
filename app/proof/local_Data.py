
import req
import auht
import time
import ast
import numpy as np
from google.cloud import bigquery


class ServerSaveData():

  def __init__(self):
    self.dir=str
    self.req_data=None
    self.local_file_data=True
  def save_data(self,path="",name=''):
   file=f"datasets_train_data\{name}.txt"
   try: 
       open(file)
   except FileNotFoundError:
       print("creando")
       self.local_file_data = False 
       self.req_data=req._req_fundamentals(path) 

   if self.local_file_data is False:
    #estos datos cambiaran a la api del server
      with open(file,'w') as newdata:
        newdata.write(str(self.req_data))
      print("hola")
      return self.req_data
      
   else:  
       with open(file) as data:
            isdata=data.read()
       print('analizando')
       time.sleep(0.5)
       return ast.literal_eval(isdata)
   
  def save_list(self):
   self.dir="datasets_train_data\list.txt"
   try: 
       open(self.dir)
   except FileNotFoundError:
       print("creando")
       self.local_file_data = False 
       self.req_data=req._req_cik_list()
       data={"data":self.req_data}

   if self.local_file_data is False:
    #estos datos cambiaran a la api del server
      with open(self.dir,'w') as newdata:
        newdata.write(str(data))
      print("hola")
      return self.req_data
      
   else:  
       with open(self.dir) as data:
            isdata=data.read()
       print('mostrando')
       time.sleep(0.5)
       return ast.literal_eval(isdata)



def zeros (num) ->str:
   zeros_length=10-len(num)
   array_zeros=np.zeros(zeros_length,dtype=int)

   return ''.join(str(i) for i in array_zeros)+num
   
   


def buscador(symbol=''):
   cls=ServerSaveData()
   s=symbol.lower()
   list=np.array(cls.save_list()['data'])
   #slice_array=list.reshape(-1,2)
   for i in list:
       if i[0]==s:
           
           return cls.save_data(zeros(i[1]),s) 



        
if __name__== "__main__":
   
   
  auht.TodaDataSimbolo()
  

    
