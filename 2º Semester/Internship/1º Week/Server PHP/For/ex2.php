<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>For Ex.2</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Utilizando o FOR dentro de um elemento UL do HTML, crie uma repetição
        que vai de 0 a 20, para cada repetição crie um elemento LI que exiba o
        valor do índice atual multiplicado por 30.
    </h1>

    <ul>
        <?php

        for ($indice=0; $indice < 21; $indice++) { 
            $indice_valor = $indice * 30;
            echo "<li> $indice * 30 = $indice_valor </li>";
        }

        ?>
    </ul>
</body>
</html>