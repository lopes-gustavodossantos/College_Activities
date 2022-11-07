<?php 

system("clear");

$numero = readline("Digite um número para descobrir seu fatorial: ");
$fatorial = 1;

for ($i = 1; $i <= $numero ; $i++) { 
    $fatorial = $fatorial * $i;
}

echo "$numero! = $fatorial\n";

?>