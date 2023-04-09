package main

import (
	"encoding/json"
	"fmt"
)

type Header struct {
    Symbol    string `json:"symbol"`
    Name      string `json:"name"`
    LastSale  string `json:"lastsale"`
    NetChange string `json:"netchange"`
    PctChange string `json:"pctchange"`
    MarketCap string `json:"marketCap"`
}

type Row struct {
    Symbol    string `json:"symbol"`
    Name      string `json:"name"`
    LastSale  string `json:"lastsale"`
    NetChange string `json:"netchange"`
    PctChange string `json:"pctchange"`
    MarketCap string `json:"marketCap"`
    Url       string `json:"url"`
}

type Table struct {
    Headers Header `json:"headers"`
    Rows    []Row  `json:"rows"`
}

type Data struct {
    Filters interface{} `json:"filters"`
    Table   Table       `json:"table"`
}

type Response struct {
    Data Data `json:"data"`
}

func main() {
    jsonString := `{
        "data": {
            "filters": null,
            "table": {
                "headers": {
                    "symbol": "Symbol",
                    "name": "Name",
                    "lastsale": "Last Sale",
                    "netchange": "Net Change",
                    "pctchange": "% Change",
                    "marketCap": "Market Cap"
                },
                "rows": [
                    {
                        "symbol": "AAPL",
                        "name": "Apple Inc. Common Stock",
                        "lastsale": "$153.85",
                        "netchange": "2.84",
                        "pctchange": "1.881%",
                        "marketCap": "2,667,349,759,000",
                        "url": "/market-activity/stocks/aapl"
                    },
                    {
                        "symbol": "MSFT",
                        "name": "Microsoft Corporation Common Stock",
                        "lastsale": "$271.32",
                        "netchange": "8.22",
                        "pctchange": "3.124%",
                        "marketCap": "2,019,652,774,574",
                        "url": "/market-activity/stocks/msft"
                    }
                ]
            }
        }
    }`

	var response Response
    err := json.Unmarshal([]byte(jsonString), &response)
    if err != nil {
        fmt.Println("Error decoding JSON:", err)
        return
    }

    fmt.Printf("rows: %+v\n", response.Data.Table.Rows[0])

}