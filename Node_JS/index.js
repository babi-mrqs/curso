const express = require("express");
const app = express();
const handlebars = require("express-handlebars");
const bodyParser = require("body-parser");
const Post = require("./models/Post");

//Config
    //Template Engine
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

//Rotas
app.get("/", function(req, res){
    Post.findAll().then(function(posts){
        res.render("home",{posts: posts})
    })
})

app.get("/cad", function(req, res){
    res.render('formulario');
    
})


app.post("/add", function(req,res){
    Post.create({
        titulo: req.body.titulo,
        conteudo: req.body.conteudo
    }).catch(function(erro){
        res.send("Houve um erro: "+erro)
    })
})

//Rota para atualizar uma postagem
app.post('/edit/:id' , function(req,res){
    const postId = req.params.id;
    const updatedTitle = req.body.titulo;
    const updatedContent = req.body.conteudo;

    Post.update(
        {titulo: updatedTitle, conteudo: updatedContent},
        {where: {id: postId} }
    ).then(function(){
        res.redirect("/");
    }).catch(function(erro){
        res.send("Erro ao atualizar: "+ erro );
    });
});


app.get("/deletar/:id", function(req,res){
    Post.destroy({where: {'id': req.params.id}}).then(function(){
        res.redirect("/");
    }).catch(function(erro){
        res.send('Erro ao deletar: '+erro)
    })
})

//Rota para editar uma postagem

app.get("/editar/:id", function(req, res){
    //Recupere o ID da postagem a ser editada a partir dos parâmetros da URL
    Post.findAll({
            where:{
            'id' : req.params.id
            }
        }).then(function (postagens){
        res.render("form_edit", { postagens : postagens[0]});
    });
})

app.post("/edit", function(req, res){

    Post.update(
        {
            titulo : req.body.titulo,
            conteudo: req.body.conteudo
        },
        { where:{
            'id' : req.body.id
        }}
    ).then( function(){
        res.send("<script>alert('Post atualizado com sucesso'); window.location.href = '/'; </script>");
    })
})

app.listen(8081, function(){
    console.log("http://localhost:8081 Servidor rodando!");
})