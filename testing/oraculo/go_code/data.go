package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"math/rand"
	"net/http"
    "github.com/redis/go-redis/v9"
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

type snd struct{
	
	data []string 
}

func random_data(values string, simbolos_num int) []string {

	var data Response
	json.Unmarshal([]byte(values), &data)

	var simbolos []string
	datos := data.Data.Table.Rows
	length_data := len(datos)

	for i := 0; i < simbolos_num; i++ {
		symbol := rand.Intn(length_data)
		simbolos = append(simbolos, datos[symbol].Symbol)
	}

	return simbolos
}


func main() {

	var ctx= context.Background()

	url := "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=0"
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		log.Fatal(err)
	}
	rdb := redis.NewClient(&redis.Options{
        Addr:     "localhost:6379",
        Password: "", // no password set
        DB:       0,  // use default DB
    })
    
	

	req.Header.Add("accept", "application/json")
	req.Header.Add("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41")

	res, _ := http.DefaultClient.Do(req)
    
	

	defer res.Body.Close()
	body, err := io.ReadAll(res.Body)
	values := string(body)

	datos := random_data(values, 200)
	fmt.Println(datos)

    //jsondat := snd{data: datos }

	b,err:= json.Marshal(datos)
	if err !=nil{
		fmt.Printf("hola")
	}
    
	fmt.Println(string(b))

	br := rdb.Set(ctx, "simbolos Entrenos",string(b), 0).Err()
    if br != nil {
        panic(br)
    }
}

