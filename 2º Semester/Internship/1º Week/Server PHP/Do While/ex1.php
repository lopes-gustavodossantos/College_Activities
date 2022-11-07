<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Do While Ex.1</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie um algoritmo utilizando o dowhile que exiba na tela uma única vez o
        índice atual do laço de repetição. O loop começa de 0 e vai até 5.
    </h1>

    <div>
        <?php

        $indice = 0;
        $mostrar_indice = false;

        do {
            if (! $mostrar_indice) {
                echo $indice;
                $mostrar_indice = true;
            }
            $indice ++;
        } while ($indice < 6);

        ?>
    </div>
</body>
</html>
