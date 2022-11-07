<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Do While Ex.2</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie um loop com dowhile que exiba dentro de um elemento <div> o índice
        atual, porém quando o índice de repetição for 2, 6 e 10, troque a cor de
        fundo apenas desta div. O loop começa de 0 e vai até 12.
    </h1>

    <div>
        <?php

        $indice = 0;

        do {
            if ($indice == 2 || $indice == 6 || $indice == 10) {
        ?>
                <div style="background-color: #C0C0C0"><?php echo $indice ?></div>
        <?php
            } else {
        ?>
                <div><?php echo $indice ?></div>
        <?php
            }      
            $indice++;
        } while ($indice <= 12);
    
        ?>
    </div>
</body>
</html>
