<?php

$numero = readline("Informe um número inteiro: ");
$zero = 0;
$soma = 0;

while ($zero != $numero) {
    $zero += 1;
    if ($zero % 2 != 0) {
        $soma += $zero;
    }
}
echo "$soma\n";

?>