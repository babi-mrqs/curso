const express = require("express");
const app = express();

app.get("/", function(req,res){
    res.sendFile(__dirname + "/view/wellcome.html")
})

app.get("/contador", function(req,res){
    res.sendFile(__dirname + "/view/contador.html")
})

app.get("/somar", function(req,res){
    res.sendFile(__dirname + "/view/somar.html")
})

app.get("/calculadora", function(req,res){
    res.sendFile(__dirname + "/view/calcIMC.html")
})


app.get("/ola/:nome/:cargo/", function(req,res){
    res.send("Olá " + req.params.nome + "<br>"+"Seu cargo é: "+req.params.cargo)
})

app.listen(8081, function(){
    console.log("Servidor Rodando!")
});
