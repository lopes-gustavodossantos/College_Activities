<?php

$query = filter_input(INPUT_GET, "msg", FILTER_SANITIZE_NUMBER_INT);
$msg = "&nbsp";
switch ($query) {
    case 1:
        $msg = "Sua sessão expirou, faça o login novamente.";
        break;

    case 2:
        $msg = "Você não possui permissão para acessar.";
        break;
}

?>

<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Get Ex.1</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie uma página que receba pela URL uma Query String com o nome de
        msg e o valor podendo ser 1 ou 2, para cada valor, exiba as mensagens
        abaixo dentro de elemento P.
        Valor 1: Sua sessão expirou, faça o login novamente.
        Valor 2: Você não possui permissão para acessar.
    </h1>

    <div>
        <p><?= $msg; ?></p>
        <a href="?msg=1">1ª Mensagem </a><br>
        <a href="?msg=2">2ª Mensagem </a><br><br>
        <a href="ex1.php">Resetar Mensagens </a>
    </div>
</body>
</html>
