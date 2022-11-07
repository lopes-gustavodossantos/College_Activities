<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>If Else Elseif Ex.1</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Declare uma variável que receba o nome e a idade do usuário, em seguida
        verifique se o usuário possui ou tenha mais de 18 anos, caso sim, exiba a seguinte
        mensagem na tela “Olá [NOME_DO_USUÁRIO], você pode participar do projeto”,
        caso tenha menos que 18 anos, exiba a seguinte mensagem “Olá
        [NOME_DO_USUÁRIO], você não pode participar do projeto”. EX: If(true) {echo
        “valido”} else {echo “inválido”;}.
    </h1>

    <div>
        <?php

        $usuario_nome = "Gustavo";
        $usuario_idade = "20";
        
        if ($usuario_idade >= 18) {
            echo "Olá {$usuario_nome}, você pode participar do projeto!";
        } else {
            echo "Olá {$usuario_nome}, você não pode participar do projeto!";
        }

        ?>
    </div>
</body>
</html>
