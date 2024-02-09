const Sequelize = require('sequelize');
const sequelize = new Sequelize('sistema_funcionarios' , 'root', '' , {
    host: "localhost",
    dialect: "mysql"
});

sequelize.authenticate().then(function(){
    console.log("conectado com sucesso!")
}).catch(function(erro){
    console.log("Falha ao conectar: " +erro);
})


const tabela = sequelize.define('funcionario',{

    Nome: {
        type: Sequelize.STRING
    },
    Email: {
        type: Sequelize.STRING
    },
    Telefone: {
        type: Sequelize.STRING
    },
    Cargo: {
        type: Sequelize.STRING
    }
})

tabela.sync({force: true})