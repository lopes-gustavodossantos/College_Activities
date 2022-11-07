<?php

system("clear");

echo "Utilize o formato Ano-Mês-Dia ou Ano/Mês/Dia.\n";
$usuario_nascimento = readline("Informe sua data de nascimento: ");

$data_atual = new DateTime("now");
$data_nascimento = new DateTime("$usuario_nascimento");

$intervalo = $data_atual->diff($data_nascimento);

$validar_18anos_atras = new DateTime("now");
$validar_18anos_atras->sub(new DateInterval("P18Y"));

$calculo = $validar_18anos_atras->diff($data_nascimento);

$faltam_anos = $calculo->format("%y");
$faltam_meses = $calculo->format("%m");
$faltam_dias = $calculo->format("%d");

$ano = "anos";
$mes = "meses";
$dia = "dias";

if ($faltam_anos == 1) {
    $ano = "ano";
} else {
    $ano = $ano;
}

if ($faltam_meses == 1) {
    $mes = "mês";
} else {
    $mes = $mes;
}

if ($faltam_dias == 1) {
    $dia = "dia";
} else {
    $dia = $dia;
}

if ($intervalo->y >= 18) {
    echo "Apta para tirar a carteira.\n";
} elseif ($intervalo->y < 18) {
    echo "Faltam $faltam_anos $ano, $faltam_meses $mes e $faltam_dias $dia.\n";
}

?>
