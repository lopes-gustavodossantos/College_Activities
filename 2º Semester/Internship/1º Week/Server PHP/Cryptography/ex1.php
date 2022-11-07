<?php

$msg = "";

if (filter_input(INPUT_POST, "btnEnviar", FILTER_SANITIZE_STRING)) {
    if (strlen(filter_input(INPUT_POST, "nome", FILTER_SANITIZE_STRING)) >= 5) {
        if (strlen(filter_input(INPUT_POST, "email", FILTER_SANITIZE_STRING)) >= 2) {
            $mail = base64_encode(filter_input(INPUT_POST, "email", FILTER_SANITIZE_STRING));
            header("Location: ler.php?mail={$mail}");
        } else {
            $msg = "<span style='color: red;'>E-mail inválido.</span>";
        }
    } else {
        $msg = "<span style='color: red;'>Nome inválido. Mínimo de 5 cracteres!</span>";
    }
}

?>

<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Criptografia</title>
    <meta charset="utf-8" />
</head>

<body>
    <form method="POST">
        <label>Nome: <input type="text" name="nome" /></label>
        <br/> <br/>
        <label>E-mail: <input type="text" name="email" /></label>
        <br/> <br/>
        <input type="submit" name="btnEnviar" value="Enviar" />
    </form>
    <br />
    <p><?= $msg; ?></p>
</body>
</html>