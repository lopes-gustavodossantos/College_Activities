<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Operadores Matemáticos Ex.2</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Exiba na tela a soma de 87 + 45, com o resultado multiplique por 3, exiba o resultado na tela.
    </h1>

    <div>
        <?php

        $num1 = 87;
        $num2 = 45;
        $soma = ($num1 + $num2);
        echo "87 + 45 = {$soma} <br>";

        $soma_x3 = $soma * 3;
        echo "{$soma} x 3 = {$soma_x3}";

        ?>
    </div>
</body>
</html>