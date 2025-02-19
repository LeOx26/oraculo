import requests

# us_market
def _req_fundamentals(cik:str):
  reqUrl = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
  headersList = {
  "Accept": "*/*",
  "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
  }
  response = requests.request("GET", reqUrl,  headers=headersList)
  resp=response.json()

  return resp

def _req_cik_list():

    response=requests.get("https://www.sec.gov/include/ticker.txt")
    Text=response.text
    return Text


