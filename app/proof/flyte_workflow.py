import ast
import numpy as np
from auht import bigqueryStorage,zeros
from flytekit import workflow, task
from google.api_core.exceptions import Conflict

cls=bigqueryStorage()
@task
def crear_tabla(symbol):
    cls.crear_tablas_babynames(symbol)
@task
def list_cik():
    list_cik=cls.get_list_Cik()
    array_cik=ast.literal_eval(list_cik)
    return np.array(array_cik).reshape(-1,2)

@workflow   
def load_symbol_fundamental_data():
    numpy_array=list_cik()
    
    for i in range(1,4):
        
     symbols_ciks=numpy_array[i]
     symbol=symbols_ciks[0]
     cik=zeros(symbols_ciks[1])
     try:
      crear_tabla(symbol)
     except Conflict:
       pass
     
     cls.InsertData(cik,symbol)

