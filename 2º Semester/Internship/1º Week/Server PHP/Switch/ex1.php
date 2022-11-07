<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Switch Ex.1</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Declare uma variável responsável por armazenar o dia da semana, começando
        de 1 (segunda) até 7 (domingo), por exemplo, 3 que corresponde a quarta.
        Verifique qual o valor da variável e exiba o dia por extenso na tela com base no
        valor da variável.
    </h1>

    <div>
        <?php

        $dia = 6;

        switch ($dia) {
            case '1':
                echo "Domingo"; 
                break;
            case '2':
                echo "Segunda-Feira";
                break;
            case '3':
                echo "Terça-Feira";
                break;
            case '4':
                echo "Quarta-Feira";
                break;
            case '5':
                echo "Quinta-Feira";
                break;
            case '6':
                echo "Sexta-Feira";
                break;
            case '7':
                echo "Sábado";
                break;
        }

        ?>
    </div>
</body>
</html>
