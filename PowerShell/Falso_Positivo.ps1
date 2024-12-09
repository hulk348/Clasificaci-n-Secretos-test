#####Falso Positivo ---- renameuser ----- Reset-SqlSaPassword

# Definición de comandos en un hash table
$commandrename = @{
    "Reset-SqlSaPassword" = "Resets the SA password for a SQL Server instance."  
    "ResetSqlAdmin"       = "Resets the administrator password for a SQL Server instance."
    "Backup-Database"     = "Creates a backup of a specified database."
    "Restore-Database"    = "Restores a database from a backup file."
    "Check-SqlStatus"     = "Checks the status of a SQL Server instance."
    "Start-SqlService"    = "Starts the SQL Server service."
    "Stop-SqlService"     = "Stops the SQL Server service."
    "Restart-SqlService"  = "Restarts the SQL Server service."
    "Get-DbUsers"         = "Retrieves a list of users from a database."
    "Create-DbUser"       = "Creates a new user in a database."
    "Delete-DbUser"       = "Deletes a user from a database."
    "Grant-DbAccess"      = "Grants access to a user for a database."
}

# Mostrar los comandos y sus descripciones
Write-Host "List of Commands and Descriptions:"
foreach ($key in $commandrename.Keys) {
    Write-Host "$key: $($commandrename[$key])"
}


####Falso Positivo ---- link in comments
#"https://support.microsoft.com/5679349ndhbuyb98-evg45ys-b4rt6h4rtb/how-to-retrieve-password-saved-by-sql-server?"

