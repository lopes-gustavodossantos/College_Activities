<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Array Ex.3</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Utilizando o array criado no exercício anterior, exiba os valores começando
        da última posição até a primeira. ["Mouse", "Teclado", "Monitor",
        "Gabinete", "Estabilizador", "Caixa de som"]
    </h1>

    <div>
        <?php

        $perifericos = ["Mouse", "Teclado", "Monitor", "Gabinete", "Estabilizador", "Caixa de Som"];
        $perifericos_reverso = array_reverse($perifericos, TRUE);

        foreach ($perifericos_reverso as $key => $val) {
            echo "<li> $val </li><br>";
        }
        ?>
    </div>
</body>
</html>