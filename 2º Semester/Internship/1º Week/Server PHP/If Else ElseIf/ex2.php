<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>If Else Elseif Ex.2</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Declare uma variável que receba o salário de um funcionário e outra para receber
        o valor do reajuste, na sequencia faça o reajuste conforme mostrado a seguir:
        - Se o funcionário ganha menos de R$ 1200.00, faça o reajuste de R$ 300,00.
        - Se o funcionário ganha mais de R$ 1200.00 e menos de 1600.00, faça o reajuste
        de R$ 250,00.
        - Se o funcionário recebe mais de R$ 1600.00, faça o reajuste de R$ 200,00.
    </h1>

    <div>
        <?php

        $funcionario_salario = 1200;

        if ($funcionario_salario < 1200) {
            $funcionario_salario += 300;
        } elseif ($funcionario_salario >= 1200 && $funcionario_salario < 1600) {
            $funcionario_salario += 250;
        } else {
            $funcionario_salario += 200;
        }

        echo $funcionario_salario;

        ?>
    </div>
</body>
</html>