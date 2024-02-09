const Sequelize = require('sequelize');
const sequelize = new Sequelize('revisao_banco' , 'root', '' , {
    host: "localhost",
    dialect: "mysql"
});

sequelize.authenticate().then(function(){
    console.log("conectado com sucesso!")
}).catch(function(erro){
    console.log("Falha ao conectar: " +erro);
})

const Postagem = sequelize.define('postagens',{
    titulo: {
        type: Sequelize.STRING
    },
    conteudo: {
        type: Sequelize.TEXT
    }
})

const Usuario = sequelize.define('usuarios',{
    nome: {
        type: Sequelize.STRING
    },
    Sobrenome: {
        type: Sequelize.STRING
    },
    idade: {
        type: Sequelize.INTEGER
    },
    email: {
        type: Sequelize.STRING
    }
})

Usuario.create({
    nome: "Bárbara",
    Sobrenome: "Marques",
    idade: 19,
    email: "babi123@gmail"
})

Usuario.create({
    nome: "Fernando",
    Sobrenome: "Oliveira",
    idade: 21,
    email: "fefedelas123@gmail"
})

//Usuario.sync({force: true})
