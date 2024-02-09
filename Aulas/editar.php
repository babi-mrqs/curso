<?php
include_once("conecta_banco.php");
$id =  $_POST["id"];
$nome = $_POST["nome"];
$idade = $_POST["idade"];
$email = $_POST["email"];

$sql = "UPDATE aluno SET nome='$nome', idade='$idade', email='$email' WHERE id=$id";
if ($conn->query($sql) === TRUE) {
    echo "<script>
    alert('Aluno atualizado com sucesso!');
    window.location.href='/listar.php';
    </script>";
} else {
    echo "Erro na inserção: ".$conn->error;
}
?>