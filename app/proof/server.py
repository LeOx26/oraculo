

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import stock_data


app = FastAPI()

#price_data=stock_data.data('AAPL').yahoo_data('1m','1d')
origins=["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/price/')
def read_root(symbol='AAPL'):
    return stock_data.data(symbol).yahoo_data()

@app.get('/perfil/')
def description(symbol='AAPL'):
    return stock_data.data(symbol).profile_share()
