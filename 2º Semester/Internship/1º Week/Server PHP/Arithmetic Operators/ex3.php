<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Operadores Matemáticos Ex.3</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie uma variável responsável por receber a subtração de dois números quaisquer,
        na sequencia crie uma segunda variável que receba o valor da variável anterior e
        dívida por 100.
    </h1>

    <div>
        <?php

        $subtracao = 77 - 27;
        $divisao = ($subtracao / 100);

        echo "77 - 27 = {$subtracao} <br>";
        echo "{$subtracao} ÷ 100 = {$divisao}";

        ?>
    </div>
</body>
</html>