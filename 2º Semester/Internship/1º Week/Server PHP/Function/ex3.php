<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Function Ex.3</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie uma função que receba um array por parâmetro e exiba os valores na
        tela.
    </h1>

    <div>
        <?php

        function listaFrutas() {
            $frutas = ["Abacaxi", "Banana", "Caju", "Kiwi", "Mamão", "Melancia"];
            
            foreach ($frutas as $key => $value) {
                echo "$value <br>";
            }
             
        }

        echo listaFrutas();

        ?>
    </div>
</body>
</html>