<?php

echo filter_input(INPUT_GET, "nome", FILTER_SANITIZE_STRING);
echo "<br>";
echo filter_input(INPUT_GET, "email", FILTER_SANITIZE_STRING);

?>