<?php
// =========================================================
// KEY
// =========================================================
$api_key = "AKIAEXAMPLE0987654321";
$client_key = "Ck718ExampleClientKey";
$service = "example_service";

// =========================================================
// AWS
// =========================================================
$aws_client_id = "AKIAEXAMPLE0987654321";
$aws_region = "us-east-1";

// =========================================================
// PASSWORD
// =========================================================
$db_user = "admin";
$db_password = "MySecret789#";
$db_host = "localhost";

header('Content-Type: application/json');

$response = [
    "key" => [
        "api_key" => $api_key,
        "client_key" => $client_key,
        "service" => $service
    ],
    "aws" => [
        "aws_client_id" => $aws_client_id,
        "aws_region" => $aws_region
    ],
    "database" => [
        "db_user" => $db_user,
        "db_password" => $db_password,
        "db_host" => $db_host
    ]
];

echo json_encode($response, JSON_PRETTY_PRINT);
?>

