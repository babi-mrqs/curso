<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

<h2 style="width:50% ; margin-right: 15%; margin-left:25% ; margin-top: 50px;" >Cadastrar Novo Aluno</h2>

<form action="inserir_aluno.php" method="POST" style="width:50% ; margin-right: 15%; margin-left:25% ; margin-top: 50px;" >
    <input class="form-control" type="text" name="nome" placeholder="Digite o nome">
    <br>
    <input class="form-control" type="number" name="idade" placeholder="Digite a idade">
    <br>
    <input class="form-control" type="text" name="email" placeholder="Digite o email">
    <br>
    <button class="btn btn-primary" type="submit" >Cadastrar aluno</button>
</form>