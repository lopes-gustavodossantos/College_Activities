<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Funções PHP Ex.2</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Declare uma variável com o seu nome completo, e utilizando a string
        str_replace, altere todas as vogais por @.
    </h1>

    <div>
        <?php

        $vogais = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"];
        
        $arroba = "@";

        $nome_completo = "Gustavo dos Santos Lopes";
        $nome_replace = str_replace($vogais, $arroba, $nome_completo);

        echo $nome_replace;

        ?>
    </div>
</body>
</html>