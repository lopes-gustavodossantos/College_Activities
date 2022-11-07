<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Function Ex.1</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie uma função que mostre a soma de dois números.
    </h1>

    <div>
        <?php

        function somaDois() {
            $num1 = 7;
            $num2 = 13;
            return $num1 + $num2;
        }

        echo somaDois();

        ?>
    </div>
</body>
</html>
