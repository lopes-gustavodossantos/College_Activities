<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Foreach Ex.1</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie um array com alguns nomes e utilizando o foreach exiba cada nome
        dentro de um elemento LI, filho do elemento UL.
    </h1>

    <div>
        <?php 

        $nomes = ["Bernardo", "Gustavo", "João", "Vilmar"];

        foreach ($nomes as $key => $value) { 
        ?>

        <ul>
            <?php echo "<li> $value </li>" ?>
        </ul>

        <?php
        }
        ?>
    </div>
</body>
</html>
