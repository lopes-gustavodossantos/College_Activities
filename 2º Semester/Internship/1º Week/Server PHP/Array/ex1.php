<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Array Ex.1</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie um array e insira o nome de seis frutas, exiba o nome de cada uma
        delas dentro de um elemento OPTION, filho do elemento SELECT.
    </h1>

    <div>
        <?php

        $frutas = ["Abacaxi", "Banana", "Caju", "Kiwi", "Mamão", "Melancia"];

        ?>

        <p>
            <?php echo "Selecione uma Fruta:" ?>
        </p>

        <select name="<select">
            <option value="valor0" selected ></option>
            <option value="valor1" ><?php echo $frutas[0] ?></option>
            <option value="valor2" ><?php echo $frutas[1] ?></option>
            <option value="valor3" ><?php echo $frutas[2] ?></option>
            <option value="valor4" ><?php echo $frutas[3] ?></option>
            <option value="valor5" ><?php echo $frutas[4] ?></option>
            <option value="valor6" ><?php echo $frutas[5] ?></option>
        </select>
    </div>
</body>
</html>
