<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

<?php
include_once("conecta_banco.php");

$id = $_GET['id'];

$sql = "DELETE FROM aluno WHERE id=$id";
$result = $conn->query($sql);
if ($result === TRUE) {
    echo "<p class='alert alert-success' role='alert' style='width:30% ; margin:30px'>Aluno excluído com sucesso!<p>"
    ?> <br> <a href="/listar.php"><button class="btn btn-outline-success" style="margin-left:40px">Voltar para página inicial</button></a> <?php ;
} else {
    echo "Erro na inserção: ".$conn->error;
}
?>