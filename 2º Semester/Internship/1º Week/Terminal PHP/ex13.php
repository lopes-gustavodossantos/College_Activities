<?php

system("clear");

$info_usuarios = ["Fernando" => "34",
                  "Marcelo"  => "25",
                  "Roberto"  => "30",
                  "Sandra"   => "22",
                  "Tiago"    => "18",
                 ];
sort($info_usuarios);

echo "Pessoas com menos de 25 anos:\n\nNomes: Tiago Sandra Marcelo\nIdade: ";

foreach ($info_usuarios as $key => $value) {
    if ($value <= 25) {
        echo " $value    ";
    }
}

echo "\n";

?>