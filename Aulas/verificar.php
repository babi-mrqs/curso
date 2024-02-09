<?php
$num = $_POST['num'];

if ($num == 0) {
    $resultado = "Neutro";
}else if ($num > 0) {
    $resultado = "Positivo";
}else if ($num < 0) {
    $resultado = "Negativo";
}else{
    $resultado = "";
}
?>

<form method="POST">
    <input type="text" name="num">
    <button type="submit">Verificar</button>
    <?php echo $resultado; ?>
</form>