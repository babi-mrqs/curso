const mysql = require('mysql2');

const connection = mysql.createConnection({
    host: 'localhost' ,
    user: 'root', 
    password: '',
    database: 'revisao_banco',
})

var nome = 'Victor'
var sobrenome = 'Silva'
var email = 'vicstonie@gmail.com'
var data = '2023-11-15'

connection.query('INSERT INTO cliente (Nome, Sobrenome, Email, Data) VALUEs (?, ?, ?, ?)',[nome,sobrenome,email,data] ,(error, results, fields) => {
    if (error) {
        console.error('Erro na consulta:', error);
        return;
    }
})

    console.log('Resultados: ', results)

connection.end((error)=> {
    if(error){
        console.error('Erro ao encerrar conexão:', error);
    }
    console.log('Conexão encerrada!')
})