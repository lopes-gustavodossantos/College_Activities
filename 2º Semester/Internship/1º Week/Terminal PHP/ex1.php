<?php

system("clear");

$gustavo = 1.40;
$juliano = 1.10;

$ano = 0;

while ($juliano < $gustavo) {
    $gustavo += 0.08;
    $juliano += 0.17;
    $ano += 1;
}

if ($ano > 1) {
    $ano_escrito = "anos";
} else {
    $ano_escrito = "ano";
}

echo "Juliano iniciou com 1.10 metros.\nGustavo iniciou com 1.40 metros.\n\n";
echo "Serão necessários $ano $ano_escrito para Juliano ser maior que Gustavo.\n";
echo "Após este tempo, Juliano terá $juliano metros, e Gustavo $gustavo metros."

?>
