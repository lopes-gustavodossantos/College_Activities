<?php

system("clear");

function ordenarDecrescente($a, $b) {
    return $a < $b;
}

$produtos = [
    ["Camiseta", 125.99],
    ["Calça"   , 254.30],
    ["Tênis"   , 458.99],
    ["Boné"    ,  35.00], 
    ["Relógio" ,  50.00],
            ];
$preco = [];
$total_vendas = 0;

for($i = 0; $i < count($produtos); $i++) {
    array_push($preco, $produtos[$i][1]);
    $maior_valor = max($preco);

    $total_vendas += $produtos[$i][1];

    if ($maior_valor == $produtos[$i][1]) {
        $maior_valor_produto = $produtos[$i][0];
    }
}

echo "Item com maior valor de venda: $maior_valor_produto R$$maior_valor\nTotal de vendas: R$$total_vendas\n";

?>
