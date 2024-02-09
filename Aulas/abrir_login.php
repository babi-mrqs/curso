<?php 
$usuario  = "admin";
$senha = "admin";

$user= $_POST['user'];
$pass= $_POST['pass'];

if($usuario == $user and $senha == $pass){
    echo "Você logou com sucesso" ;
}elseif($usuario == $user and $senha != $pass){
    echo "<h1>Falha ao logar!</h1><br><h3>Senha incorreta</h3>";
}elseif($usuario != $user){
    echo "<h1>Falha ao logar!</h1><br><h2>Usuário não encontrado!</h2>";
}else{
    echo "<h1>Falha ao logar!</h1>";
}
?>

