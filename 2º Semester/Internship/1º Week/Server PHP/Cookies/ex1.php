<?php

$msg = "";


if (filter_input(INPUT_POST, "btnEnviar", FILTER_SANITIZE_STRING)) {
    if (strlen(filter_input(INPUT_POST, "nome", FILTER_SANITIZE_STRING)) >= 5) {
        setcookie("nome", filter_input(INPUT_POST, "nome", FILTER_SANITIZE_STRING));
        header("Location: ler.php");
    } else {
        $msg = "<span style='color: red;'>Nome inválido. Mínimo de 5 caracteres!</span>";
    }
}
?>
<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Cookie</title>
    <meta charset="utf-8" />
</head>

<body>
    <form method="POST">
        <label>Nome: <input type="text" name="nome" /></label>
        <br/> <br/>
        <input type="submit" name="btnEnviar" value="Enviar" />
    </form>
    <br />
    <p><?= $msg; ?></p>
</body>
</html>