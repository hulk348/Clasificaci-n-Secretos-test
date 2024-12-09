##AWS
$AWSClientID = "AKIAEXAMPLE5566778899"
$AWSRegion = "us-east-1"


##PASSWORD
$User = "admin"
$Password = "RandomKey*&76"
$Server = "localhost"

function Connect-AWS {
    Write-Output "Conectando a AWS..."
    Write-Output "Client ID: $AWSClientID"
    Write-Output "Región: $AWSRegion"
    # Simula la conexión a un cliente AWS
    Start-Sleep -Seconds 2
    Write-Output "Conexión a AWS exitosa."
}

function Connect-Database {
    Write-Output "Conectando a la base de datos..."
    Write-Output "Servidor: $Server"
    Write-Output "Usuario: $User"
    Write-Output "Contraseña: (oculta por seguridad)"
    # Simula la conexión al servidor
    Start-Sleep -Seconds 2
    Write-Output "Conexión a la base de datos exitosa."
}

Write-Output "=== EJECUTANDO SCRIPT DE CONFIGURACIÓN ==="
Connect-AWS
Connect-Database
Write-Output "=== SCRIPT FINALIZADO ==="
