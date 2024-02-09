<?php 
    $nome_da_pagina = "Titulo Teste";
    @$nome = $_POST = ["nome"];
    @$idade = $_POST = ["idade"];

?>

<html>
    <body>
        <h1> <?php echo $nome_da_pagina?> </h1>
        <?php 
        if(isset($_POST['nome']) and isset($_POST['idade'])){
        ?>
        <h2> <?php echo "Olá ".$nome.", você tem ".$idade."anos"?> </h2>
        <?php } ?>

        <form method="post" action = 'index.php'>
            Nome: <input type="text" name='nome'>
            Idade: <input type="text" name='idade'>

            <button type= 'submit'> Enviar </button>
        </form>
        
    </body>

</html>