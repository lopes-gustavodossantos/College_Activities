<?php

system("clear");
$numeros = [];

for ($i = 1; $i < 11; $i++) { 
    $numero = readline("($i/10) Digite um número inteiro: ");

    if ($numero > 30 && $numero < 90) {
        array_push($numeros, $numero);
    }
}

$quantidade_numeros = count($numeros);

echo "Quantidade de números entre 30 e 90: $quantidade_numeros\n";

?>