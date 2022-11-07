<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Array Ex.2</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie um array com os seguintes valores: Mouse, Teclado, Monitor,
        Gabinete, Estabilizador e Caixa de som. Exiba na tela através de seu
        respectivo índice, apenas o Teclado e o Gabinete.
    </h1>

    <div>
        <?php

        $perifericos = ["Mouse", "Teclado", "Monitor", "Gabinete", "Estabilizador", "Caixa de Som"];
        echo "$perifericos[1] <br> $perifericos[3]";

        ?>
    </div>
</body>
</html>