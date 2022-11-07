<?php

$numero = readline("Digite um número inteiro: ");

for ($i = 1; $i < 11; $i++) { 
    $tabuada = $numero * $i;
    echo "$i x $numero = {$tabuada}\n";
}

?>