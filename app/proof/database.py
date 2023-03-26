from ast import JoinedStr
import json
from tracemalloc import start
import redis



redis=redis.Redis(host="localhost",port=6379)

#podman start redis-stack

finacials = redis.hget("yfinance_api_url", 'financials')
print(finacials)
financials1 = {"1":"https://query2.finance.yahoo.com/v10/finance/quoteSummary/"
            ,"2":"?formatted=true&crumb=sm3xpA2Nbv.&lang=en-US&region=US&modules=incomeStatementHistory%2CcashflowStatementHistory%2CbalanceSheetHistory%2CincomeStatementHistoryQuarterly%2CcashflowStatementHistoryQuarterly%2CbalanceSheetHistoryQuarterly&corsDomain=finance.yahoo.com"}

set = 'financials1:'+str(financials1)
redis.hset("yfinance_api_url", "financials1", str(financials1 ))
print(redis.hget('yfinance_api_url', 'financials1'))
