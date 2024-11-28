import os
import random

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/nuevo"
os.makedirs(output_dir, exist_ok=True)

# Extensiones de archivos
extensions = [
    ".yaml", ".yml", ".ini", ".properties", ".back", ".etx",
    ".json", ".py", ".php", ".conf", ".ps1"
]

# Contraseñas ficticias para incluir en los archivos
passwords = [
    "Password123!", "SecurePass456$", "MySecret789#", "AdminKey2023",
    "TestPass@2024", "UserKey#987", "DevSecret%001", "RandomKey*&76",
    "Encrypted$Key", "BackupPass$!"
]

# Ejemplo de configuraciones para cada tipo de archivo
configurations = {
    ".yaml": "database:\n  username: admin\n  password: {}\n  host: localhost\n",
    ".yml": "auth:\n  username: admin\n  password: {}\n  server: example.com\n",
    ".ini": "[database]\nusername=admin\npassword={}\nserver=localhost\n",
    ".properties": "db.username=admin\ndb.password={}\ndb.host=127.0.0.1\n",
    ".back": "backup_user=admin\nbackup_password={}\nbackup_location=/backups\n",
    ".etx": "external_service_user=admin\nexternal_service_password={}\nendpoint=api.example.com\n",
    ".json": '{{"username": "admin", "password": "{}", "server": "127.0.0.1"}}',
    ".py": 'DB_USER = "admin"\nDB_PASSWORD = "{}"\nDB_HOST = "localhost"\n',
    ".php": '<?php\n$db_user = "admin";\n$db_password = "{}";\n$db_host = "localhost";\n?>',
    ".conf": "user=admin\npassword={}\nhost=127.0.0.1\n",
    ".ps1": '$User = "admin"\n$Password = "{}"\n$Server = "localhost"\n'
}

# Crear 100 archivos con configuraciones diferentes
for i in range(1, 101):
    # Seleccionar una extensión y contraseña al azar
    ext = random.choice(extensions)
    password = random.choice(passwords)
    
    # Generar el contenido del archivo
    content = configurations[ext].format(password)
    
    # Crear el nombre del archivo
    file_name = f"config_{i}{ext}"
    file_path = os.path.join(output_dir, file_name)
    
    # Guardar el contenido en el archivo
    with open(file_path, "w") as file:
        file.write(content)

# Mostrar mensaje de éxito
print(f"Se crearon 100 archivos de configuración en el directorio '{output_dir}'.")


