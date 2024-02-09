<?php
include_once("conecta_banco.php");

$nome = $_POST["nome"];
$idade = $_POST["idade"];
$email = $_POST["email"];


$sql = "INSERT INTO aluno (nome, idade, email) VALUES ('$nome', $idade,'$email') "; 
if ($conn->query($sql) === TRUE) {
    echo header('location: /listar.php');
} else {
    echo "Erro na inserção: ".$conn->error;
}
?>