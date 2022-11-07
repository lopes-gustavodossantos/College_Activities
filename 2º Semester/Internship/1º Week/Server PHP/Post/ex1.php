<?php

$estados = ["AC" =>"Acre",
            "AL"=> "Alagoas",
            "AP"=> "Amapá",
            "AM"=> "Amazonas",
            "BA"=> "Bahia",
            "CE"=> "Ceará",
            "DF"=> "Distrito Federal",
            "ES"=> "Espírito Santo",
            "GO"=> "Goiás",
            "MA"=> "Maranhão",
            "MT"=> "Mato Grosso",
            "MS"=> "Mato Grosso do Sul",
            "MG"=> "Minas Gerais",
            "PA"=>"Pará",
            "PB"=>"Paraíba",
            "PR"=> "Paraná",
            "PE"=> "Pernambuco",
            "PI"=> "Piauí",
            "RJ"=> "Rio de Janeiro",
            "RN"=> "Rio Grande do Norte",
            "RS"=> "Rio Grande do Sul",
            "RO"=>"Rondônia",
            "RR"=>"Roraima",
            "SC"=> "Santa Catarina",
            "SP"=> "São Paulo",
            "SE"=> "Sergipe", 
            "TO"=> "Tocantins",
        ];

$aviso = "";

if (filter_input(INPUT_POST, "btnEnviar", FILTER_SANITIZE_STRING)) {
    if (strlen(filter_input(INPUT_POST, "nome", FILTER_SANITIZE_STRING)) >= 5 && strlen(filter_input(INPUT_POST, "nome", FILTER_SANITIZE_STRING)) <= 100) {
        $aviso = "<span style='color: green'>Nome válido.</span>";
    } else {
        $aviso = "<span style='color: red'>Nome inválido! <br> Mínimo de 5, e máximo de 100 caracteres.</span>";
    }


    $valido = false;
    $estado = filter_input(INPUT_POST, "estados", FILTER_SANITIZE_STRING);

    foreach ($estados as $key => $value) {
        if($key == $estado){
            $valido = true;
        }
    }
}

?>

<!DOCTYPE HTML>
<html lang="pt-br">

<head>
    <title>Post Ex.1</title>
    <meta charset="utf-8" />
</head>
    
<body>
    <h1>
        Crie um formulário com dois campos de entrada, um para o nome e outro
        para o estado (utilizando um select, não precisa ser todos os estados). Sua
        aplicação deverá conter as seguintes funcionalidades quando o formulário
        for submetido:
        - Utilize o filter_input para obter os valores dos formulários;
        - Você deverá verificar se o nome possui mais de 5 caracteres e menos
        que 100;
        - Crie um array associativo utilizando os mesmos valores do array como
        chave, e verifique se o estado selecionado está ou não no array, caso
        esteja, exiba o nome do estado completo na tela;
    </h1>

    
    <form method="post" name="usuario">
        <label>Nome: <input type=text name=nome></label><br>

        <label>
            <br>Estado: 
            <select name="estados">
                <?php
                foreach ($estados as $key => $value) {
                ?>
                    <option value="<?= $key; ?>"><?= $value; ?></option>
                <?php
                }
                ?>
            </select>
        </label><br><br> 

        <input type=submit name="btnEnviar" value="Enviar"/>
        <p><?= $aviso ?></p>

    </form>
</body>
</html>
