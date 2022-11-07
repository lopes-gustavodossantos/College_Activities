<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>While Ex.2</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Declare uma variável chama de índice começando de 0. Dentro da estrutura
        while, utilizando o if verifique se o índice é igual a 12, caso seja, exiba a
        mensagem “Número válido, posição [variável índice]”. A cada repetição do
        while incremente 1 a variável índice, para a saída a variável índice deve ser
        menor ou igual a 15.
    </h1>

    <div>
        <?php

        $indice = 0;

        while (True) {
            $indice ++;
            echo "$indice <br>";

            if ($indice == 11) {
                $indice ++;
                echo "Número válido, posição $indice <br>";
            }
            
            if ($indice == 15) {
                break;
            }
        }

        ?>
    </div>
</body>
</html>