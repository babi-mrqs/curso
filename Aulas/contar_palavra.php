<form method="POST">
    <label>Digite abixo a frase</label> <br>
    <textarea name="frase" placeholder="digite aqui a frase"></textarea>
    <button type="submit"> Enviar frase</button>
</form>
<br>

<?php
@$frase = $_POST['frase'];
//@$resultado = str_word_count($frase);
@$palavras = explode(' ', $frase); 
@$resultado = count($palavras);
echo 'Há '.$resultado.' palavras na frase: <br>'.$frase;
?>