<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Foreach Ex.2</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
    Crie um array associativo onde a chave é um valor numérico crescente e o
    valor o nome de algumas frutas, utilizando o foreach exiba os valores
    dentro do elemento OPTION, para o atributo value do elemento, insira a
    key do array.
    </h1>

    <div>
        <?php

        $frutas = [1 => "Abacaxi", 2 => "Banana", 3 => "Caju", 4 => "Kiwi", 5 => "Mamão", 6 => "Melancia"];

        ?>

        <select name="slFrutas" id="slFrutas">

        <?php
            foreach ($frutas as $key => $value) {
        ?>
                <option value="<?php $key ?>"><?= $value ?></option>
        <?php
            }
        ?>
        </select>
    </div>
</body>
</html>