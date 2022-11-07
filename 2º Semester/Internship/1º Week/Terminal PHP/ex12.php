<?php

system("clear");

$lista_numeros = [2, 5, 7, 9, 12, 16, 19, 23, 29, 32];
$lista_pares = [];
$lista_impares = [];

foreach ($lista_numeros as $key => $value) {
    if ($value % 2 == 0) {
        array_push($lista_pares, $value);
    } elseif ($value % 2 != 0) {
        array_push($lista_impares, $value);
    }
}

echo "Quantidade de Pares: " . sizeof($lista_pares) . "\nQuantidade de Ímpares: " . sizeof($lista_impares) . "\n";

?>