<?php
    $a = $_POST['num1'];
    $b = $_POST['num2'];
    $op = $_POST['operacao'];

    if ($op =='+'){
        $resultado = $a+$b;
    }else if ($op == '-'){
        $resultado = $a-$b;
    }else if ($op == '*'){
        $resultado = $a*$b;
    }else if ($op == '/'){
        $resultado = $a/$b;
    }
?>
<form method="POST">
    <input type="number" name="num1">
    <select name="operacao" id=''>
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
    </select>
    <input type="number" name="num2">

    <button type="submit">Calcular</button>
</form>

    <?php 
    var_dump($resultado);
    if(isset($resultado)){
    ?>
        <p><?php echo "O resultado é ".$resultado; ?></p>
       <?php 
    }
    ?>