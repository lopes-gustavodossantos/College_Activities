<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Requisição de Arquivos Ex.1</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie um arquivo chamado de functions.php, nele escreva quatro funções
        que calcule as operações básicas, na sequencia utilizando uma página
        principal, chame este arquivo e exiba o resultado de cada uma das funções
        passando alguns valores.
    </h1>

    <div>
        <?php

        require_once("functions.php");
        
        echo "Soma: " . somaDois(4, 3) . "<br>Subtração:" .subtracaoDois(20, 7);
        echo "<br>Multiplicação: " . multiplicacaoDois(7, 7) . "<br>Divisão: " . divisaoDois(70, 3.5);

        ?>
    </div>
</body>
</html>
