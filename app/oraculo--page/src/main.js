import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

createApp(App).mount('#app')

function search(){
    var x =window.location.search
    const params=new URLSearchParams(x);
    return params.get('search')
}
var symbol=search()
var url='http://127.0.0.1:8000/price/?symbol='
//cuadro 1

function cuadro_1(){
const xhr = new XMLHttpRequest();
xhr.withCredentials = true;
xhr.addEventListener("readystatechange", function () {
    if (this.readyState === this.DONE) {
        const chart = LightweightCharts.createChart(document.getElementById("plot_size"), { width: 900, height: 490,layout: { textColor: 'white', background: { type: 'solid', color: 'black' }}});
        const lineSeries = chart.addAreaSeries({lineColor: '#2962FF',topColor: '#2962FF'});
        const data=JSON.parse(this.responseText)
        lineSeries.setData(data)
        
    }
   

    
  });
xhr.open("GET",url+symbol);
xhr.send(null);
}

document.getElementById("plot_analisis").onclick=function(){
    var analisis_plot_url='https://es.tradingview.com/chart/?symbol='
    window.open(analisis_plot_url+symbol)

}
//fin cuadro 1
//cuadro 2
var url_profile='http://127.0.0.1:8000/perfil/?symbol='
function cuadro_2(){
    const xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

xhr.addEventListener('readystatechange',function(){
    if(this.readyState==this.DONE){
        var response=JSON.parse(this.responseText)
        console.log(response)
        document.getElementById("name").innerText=response.market.name
        document.getElementById("profile").innerText=response.profile
        document.getElementById("symbol").innerText=response.market.symbol
        document.getElementById("price").innerText=response.market.price+"  "+response.market.currency
        document.getElementById("exchange").innerText=response.market.exchange
        document.getElementById("cap").innerText=response.market.marketcap
        document.getElementById("sec").innerText=response.sector
        document.getElementById("inc").innerText=response.industry
        document.getElementById("quote").innerText=response.market.quoteType
    }
})
xhr.open("GET",url_profile+symbol)
xhr.send(null)
}


cuadro_2()
cuadro_1()
