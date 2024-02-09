<?php

if(isset($_GET['cep'])){

    //criando o recurso cURL
    $curl = curl_init();

    $street= $_GET['rua'];
    $rua = str_replace(' ', '+', $rua); 

    $city = 

    $url = 'https://viacep.com.br/ws/'.$_GET['uf'].'/'.$_GET['cidade'].'/'.$rua.'/json/';

    //definido a url de busca
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

    //executando o recurso
    $response = curl_exec($curl);

    //fecha a sessão cURL
    curl_close($curl);

    //exibe a resposta
    $endereco = json_decode($response, true);

    /*echo "<pre>";
    var_dump($endereco);
    echo "<pre>";*/

    



}
?> 

<form method="get">
<input type="text" name="cidade" placeholder="dige a cidade">
<input type="text" name="uf" placeholder="dige o estado">
<input type="text" name="rua" placeholder="dige a rua">

<button type="submit" >Enviar </button>
</form>

<input type="text"value='<?php echo @$endereco['logradouro'] ?>' >
<input type="text" value='<?php echo @$endereco['bairro'] ?>' >
<input type="text" value='<?php echo @$endereco['localidade'] ?>' >
<input type="text" value='<?php echo @$endereco['uf'] ?>' >
<input type="text" value='<?php echo @$endereco['ddd'] ?>' >
