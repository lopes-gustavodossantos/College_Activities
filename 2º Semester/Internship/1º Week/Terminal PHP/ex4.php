<?php

system("clear");

$quantidade_soma = readline("Digite a quantidade de números que você quer somar: ");
$numeros = [];

for ($i = 1; $i < $quantidade_soma + 1; $i++) { 
    $numero = readline("($i/$quantidade_soma) Digite um número inteiro: ");

    array_push($numeros, $numero);
}

sort($numeros);
$soma = array_sum($numeros);
$media = number_format($soma / $quantidade_soma, 2);

system("clear");

$ultimo_numero_lista = $quantidade_soma - 1;
echo "Maior número: $numeros[$ultimo_numero_lista]\nMenor número: $numeros[0]\n\nSoma dos números: $soma\nMédia dos números: $media\n"; 

?>
