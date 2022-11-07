<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Function Ex.4</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie uma função para fazer o reajuste de um salário que é recebido por
        parâmetro, para o reajuste utilize o valor de entrada + 5%. Retorne este
        valor a uma variável e exiba o seu resultado dentro de um elemento.
    </h1>

    <div>
        <?php

        $salario = 1500;

        function reajusteSalario($salario) {
            $salario_corrigido = $salario + ($salario * 0.05);
            return $salario_corrigido;
        }

        echo "Salário antigo: $salario<br>";
        echo "Salário com reajuste: " . reajusteSalario($salario);

        ?>
    </div>
</body>
</html>