<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>While Ex.1</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Declare uma variável chama índice e atribua a ela o valor 0, em seguida
        utilizando while, incremente 1 a cada repetição e exiba o valor na tela. A
        condição de saída para o while deve ser quando o índice for menor que 20.
    </h1>

    <div>
        <?php

        $indice = 0;

        while ($indice < 20) {
            echo "{$indice} <br>";
            $indice ++;
        }

        ?>
    </div>
</body>
</html>
