<?php

system("clear");

$valor = readline("Informe o valor do carro: ");
echo "\nParcelas:    Juros:\n06           03%\n12           06%\n18           09%\n24           12%\n36           18%\n48           24%\n\n";
$parcelas = readline("Informe o número de parcelas: ");

if ($parcelas <= 6) {
    $total = ($valor + ($valor * 0.03));
} elseif ($parcelas <= 12) {
    $total = ($valor + ($valor * 0.06));
} elseif ($parcelas <= 18) {
    $total = ($valor + ($valor * 0.09));
} elseif ($parcelas <= 24) {
    $total = ($valor + ($valor * 0.12));
} elseif ($parcelas <= 36) {
    $total = ($valor + ($valor * 0.18));
} elseif ($parcelas <= 48) {
    $total = ($valor + ($valor * 0.24));
} else {
    $total = "Opção inválida, utilize uma opção indicada acima!";
}

echo "Valor inicial: $valor\nNº de parcelas: $parcelas\nTotal com juros: $total\n";

?>