<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "aula_php";

//conectando com banco
$conn = new mysqli($servername, $username, $password, $dbname);

/*if ($conn->connect_error) {
    die("Conexão falhou". $conn->connect_error);
}
echo"Conectado com sucesso";

$sql = "INSERT INTO aluno (nome, idade, email) VALUES ('Babi',19,'babi@gmail.com') "; 
if ($conn->query($sql) === TRUE) {
    echo "Dado inserido com sucesso";
} else {
    echo "Erro na inserção: ".$conn->error;
}

echo"<br>";
$sql_select = "SELECT * FROM aluno";
$result = $conn->query($sql_select);
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "- ID: ". $row["id"] ."- Nome: ". $row["Nome"] ."- Idade: ". $row["idade"] ."- Email: ". $row["email"];
    }
} else {
    echo "Nenhum resultado encontrado!";
}*/
?>