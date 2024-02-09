<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
<br><br>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="cadastrar.php">Cadastrar Aluno</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Buscar" name="buscar" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Buscar</button>
      </form>
  </div>
</nav>

<table class="table table-bordered"  style="width:50% ; margin-right: 15%; margin-left:25% ; margin-top: 50px;">
  <thead>
    <tr>
      <th scope="col">ID</th>
      <th scope="col">Nome</th>
      <th scope="col">Idade</th>
      <th scope="col">Email</th>
      <th scope="col">Ações</th>
    </tr>
  </thead>
  <tbody>
<?php

include_once("conecta_banco.php");
@$buscar = $_GET['buscar'];
if (isset($buscar)){
    $sql_select = "SELECT * FROM aluno WHERE nome LIKE '%$buscar%' ";
} else{
    $sql_select = "SELECT * FROM aluno";
};
        $result = $conn->query($sql_select);
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                ?>
                <tr>
                <td><?php echo $row['id'] ?> </td>
                <td><?php echo$row['nome']?></td>
                <td><?php echo$row['idade']?></td>
                <td><?php echo$row['email']?></td>
                <td><a href="/form_editar.php/?id=<?php echo $row['id']?>"><button type='button' class='btn btn-primary'>Editar</button> </a>
                <a onclick="return confirm('Você tem certeza que deseja excluir este aluno?')"  href="/deletar.php/?id=<?php echo $row['id']?>" ><button class='btn btn-danger'>X</button></a>
            </tr>
            <?php
            }
        } else {
            echo "Nenhum resultado encontrado!";
        }
    



?>
  </tbody>
</table>