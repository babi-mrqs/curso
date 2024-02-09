const db = require("./db2");
const Func = db.sequelize.define('funcionarios', {
    nome: {
        type: db.Sequelize.STRING
    },
    email: {
        type: db.Sequelize.STRING
    },
    telefone: {
        type: db.Sequelize.STRING
    },
    cargo: {
        type: db.Sequelize.STRING
    }
})

module.exports = Func;

//Func.sync({force: true})