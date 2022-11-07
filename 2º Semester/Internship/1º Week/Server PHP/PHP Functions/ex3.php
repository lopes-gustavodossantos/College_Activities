<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Funções PHP Ex.3</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Declare uma variável com o seu nome, e utilizando o explode, exiba a
        mensagem “Olá, {SEU_NOME}, porém apenas para o primeiro nome.
    </h1>

    <div>
        <?php

        $nome = "Gustavo dos Santos Lopes";
        $nome_inicio = explode(" ", $nome);

        echo $nome_inicio[0];

        ?>
    </div>
</body>
</html>