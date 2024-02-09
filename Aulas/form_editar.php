<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

<?php
include_once("conecta_banco.php");
$id = $_GET['id'];

$sql_select = "SELECT * FROM aluno WHERE id=$id";
$result = $conn->query($sql_select);
if ($result->num_rows > 0) {
    $row = $result->fetch_assoc() ;
?>


<h2 style="width:50% ; margin-right: 15%; margin-left:25% ; margin-top: 50px;" >Editar Aluno</h2>

<form action="../editar.php" method="POST" style="width:50% ; margin-right: 15%; margin-left:25% ; margin-top: 50px;" >
    <input hidden name="id" value="<?php echo$row['id']?>">
    <input class="form-control" type="text"  name="nome" value="<?php echo$row['nome']?>">
    <br>
    <input class="form-control" type="number" name="idade" value="<?php echo$row['idade']?>">
    <br>
    <input class="form-control" type="text" name="email" value="<?php echo$row['email']?>">
    <br>
    <button class="btn btn-primary" type="submit" >Atualizar aluno</button>
</form>
<?php
} else {
            echo "Nenhum resultado encontrado!";
        }
?>