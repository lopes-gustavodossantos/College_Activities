<?php

system("clear");

$numero = readline("Digite um número: ");
if ($numero > 5) {
    echo "\n2\n3\n";
} elseif ($numero == 2) {
    echo "Não há números primos antes do $numero!\n";
} elseif ($numero == 3) {
    echo "\n2\n";
} elseif ($numero == 4) {
    echo "\n2\n3\n";
} elseif ($numero == 5) {
    echo "\n2\n3\n";
}

for ($i = 2; $i < $numero; $i++) { 
    if ($i / 1 == $i && $i / $i == 1 && $i % 2 != 0 && $i % 3 != 0 && $i % 5 != 0) {
        echo "$i\n";
    }
}

?>