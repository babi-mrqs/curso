const express = require("express");
const app = express();
const handlebars = require("express-handlebars");
const bodyParser = require("body-parser");
const Func = require("./models/funcionario");
const { where } = require("sequelize");


app.engine('handlebars', handlebars.engine({
    defaltLayout: "main",
    runtimeOptions: {
        allowProtoPropertiesByDefault: true,
        allowProtoMethodsByDefault: true,
    },
}));
app.set("view engine", "handlebars")
    //Body Parser
    app.use(bodyParser.urlencoded({extended: false}))
    app.use(bodyParser.json());

app.get("/", function(req, res){
    Func.findAll().then(function(funcionario){
        res.render("home",{funcionario: funcionario})
    })
})

app.get("/cadastrar", function(req, res){
    res.render("formulario")
})

app.post("/addFunc", function(req,res){
    Func.create({
        nome: req.body.nome,
        email: req.body.email,
        telefone: req.body.telefone,
        cargo: req.body.cargo
    }).then(function(){
        res.send("<script>alert('Funcionário cadastrado com sucesso!'); document.location.href = '/' </script>")
    }).catch(function(erro){
        res.send("Houve um erro: "+erro)
    });
})

app.get("/deletar/:id" , function(req,res){
    Func.destroy({where: {'id': req.params.id}}).then(function(){
        res.redirect("/");
    }).catch(function(erro){
        res.send('Erro ao deletar: '+erro)
    })
})

app.get("/editar/:id", function(req, res){
    Func.findAll(
        {where : { id : req.params.id}}
    ).then( function (dados){
        console.log(dados[0]);
        res.render("editar", {funcionario : dados[0]})
    });
})


app.post("/editFunc", function(req, res){                    
    const IdFunc = req.body.id;
    const updatedName = req.body.nome;
    const updatedPhone = req.body.telefone;
    const updatedEmail = req.body.email;
    const updatedCargo = req.body.cargo;

    Func.update(
        {nome: updatedName , email: updatedEmail, telefone: updatedPhone, cargo: updatedCargo},
        {where: {id: IdFunc}}
    ).then(function(){
        res.send("<script> confirm('Você tem certeza que deseja editar este funcionário?'); document.location.href = '/' </script> ")
    }).catch(function(erro){
        res.send("Erro ao atualizar: "+ erro );
    })
})


app.listen(8081, function(){
    console.log("http://localhost:8081 Servidor rodando!");
})