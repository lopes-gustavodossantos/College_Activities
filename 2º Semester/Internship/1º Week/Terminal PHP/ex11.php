<?php

system("clear");

$lista_numeros = [52, 15, 17, 25, 39, 48, 63, 72, 10];
sort($lista_numeros);
$lista_menores18 = [];
$lista_maiores50 = [];

echo "Lista completa: ";

foreach ($lista_numeros as $key => $value) {
    if ($value < 18) {
        array_push($lista_menores18, $value);
    } elseif ($value > 50) {
        array_push($lista_maiores50, $value);
    }
    echo "$value ";
}

echo "\n";
echo "Menores que 18: ";
foreach ($lista_menores18 as $key => $value) {
    echo "$value ";
}

echo "\n";
echo "Maiores que 50: ";
foreach ($lista_maiores50 as $key => $value) {
    echo "$value ";
}
echo "\n";

?>
