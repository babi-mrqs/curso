<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

<br><br><br>

<?php
    @$a = $_POST['num1'];
    @$b = $_POST['num2'];
    @$op = $_POST['operacao'];

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
<form style="display: inline-block" method="POST">
    <input class="input-group-text" type="number" name="num1">
    <select class="btn btn-primary dropdown-toggle" name="operacao" id=''>
        <option class="dropdown-item" value="+">+</option>
        <option class="dropdown-item" value="-">-</option>
        <option class="dropdown-item" value="*">*</option>
        <option class="dropdown-item" value="/">/</option>
    </select>
    <input class="input-group-text" type="number" name="num2">

    <button type="submit" class="btn btn-outline-primary" >Calcular</button>
</form>

    <?php 
    var_dump(@$resultado);
    if(isset($resultado)){
    ?>
        <p><?php echo "O resultado é ".$resultado; ?></p>
       <?php 
    }
    ?>