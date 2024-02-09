<?php
    @$math = $_POST['math'];
    @$port = $_POST['port'];
    @$bio = $_POST['bio'];
    @$quim = $_POST['quim'];
?>
<br>
<br><br><br><br>
<form method="POST">
    <input required type="number" name="math" placeholder="nota matemática"> 
    <input required type="number" name="port" placeholder="nota português">
    <input required type="number" name="bio" placeholder="nota biologia">
    <input required type="number" name="quim" placeholder="nota química">
    <button type="submit" >Calcular média</button>
</form>

<?php
    $media = ($math + $port + $quim + $bio)/4;
    if (isset($_POST['math'])){
        if($media >= 6){
            echo 'Sua nota foi '.$media.'! <br> Parabéns, você passou';
        }else{
            echo 'Sua nota foi '.$media.'! <br> Você rodou';
        }
    }
    ?>