<?php

system("clear");

$numero = readline("Digite um número: ");
$anterior = 1;
$dois_antes = 0;

$contador = $numero;

echo "0\n1\n";

for ($i = 1; $i < $contador; $i++) {
    $numero = $anterior + $dois_antes;
    echo "$numero\n";

    $dois_antes = $anterior;
    $anterior = $numero;

}

?>