import os
import random

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/config_file_secret"
os.makedirs(output_dir, exist_ok=True)

# Extensiones de archivos
extensions = [".yaml", ".properties"]

# Ejemplo de configuraciones con Secrets para cada tipo de archivo
secret_configurations = {
    ".yaml": "secrets:\n  db_secret: {}\n  api_secret: {}\n  encryption_key: {}\n",
    ".properties": "db.secret={}\napi.secret={}\nencryption.key={}\n",
}

# Secrets ficticios
db_secrets = [
    "DBSecret123!", "SecureDB456$", "MyDBSecret789#", "AdminDBKey2023", "TestDBPass@2024"
]

api_secrets = [
    "APISecretKey123!", "SecureAPI456$", "MyAPIKey789#", "AdminAPIKey2023", "TestAPIPass@2024"
]

encryption_keys = [
    "EncryptKey123!", "SecureEncrypt456$", "MyEncryptKey789#", "AdminEncryptKey2023", "TestEncryptPass@2024"
]

# Crear 10 archivos con configuraciones diferentes
for i in range(1, 11):
    # Seleccionar una extensión y varios secretos al azar
    ext = random.choice(extensions)
    db_secret = random.choice(db_secrets)
    api_secret = random.choice(api_secrets)
    encryption_key = random.choice(encryption_keys)
    
    # Generar el contenido del archivo
    content = secret_configurations[ext].format(db_secret, api_secret, encryption_key)
    
    # Crear el nombre del archivo
    file_name = f"secret_config_{i}{ext}"
    file_path = os.path.join(output_dir, file_name)
    
    # Guardar el contenido en el archivo
    with open(file_path, "w") as file:
        file.write(content)

# Mostrar mensaje de éxito
print(f"Se crearon 10 archivos de configuración de secretos en el directorio '{output_dir}'.")


