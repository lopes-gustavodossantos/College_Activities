<?php

function somarDois($numero1, $numero2) {
    echo "$numero1 + $numero2 = " . ($numero1 + $numero2) . "\n";
}

function subtrairDois($numero1, $numero2) {
    echo "$numero1 - $numero2 = " . ($numero1 - $numero2) . "\n";
}

function multiplicarDois($numero1, $numero2) {
    echo "$numero1 x $numero2 = " . ($numero1 * $numero2) . "\n";
}

function dividirDois($numero1, $numero2) {
    echo "$numero1 ÷ $numero2 = " . ($numero1 / $numero2) . "\n";
}

while (TRUE) {
    system("clear");

    $numero1 = readline("(1/2) Digite um número inteiro: ");
    $numero2 = readline("(2/2) Digite um número inteiro: ");

    system("clear");

    echo "1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n";
    $opcao = readline("Escolha uma das opções acima: ");

    if ($opcao == 1 || $opcao == 2 || $opcao == 3 || $opcao == 4 || $opcao == 5) {
        switch ($opcao) {
            case '1':
                somarDois($numero1, $numero2);
                sleep(1);
                break;
            case '2':
                subtrairDois($numero1, $numero2);
                sleep(1);
                break;
            case '3':
                multiplicarDois($numero1, $numero2);
                sleep(1);
                break;
            case '4':
                if ($numero2 == 0 ) {
                    echo $numero1 . " ÷ 0 = 0";
                } else {
                    dividirDois($numero1, $numero2);
                }
                sleep(1);
                break;
        }
    }
}

?>
