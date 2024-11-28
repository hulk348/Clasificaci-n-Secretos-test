import os
import random

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/config_file_auth"
os.makedirs(output_dir, exist_ok=True)

# Extensiones de archivos
extensions = [".json", ".js", ".yaml", ".properties", ".conf"]

# Ejemplo de configuraciones con Autorización para cada tipo de archivo
auth_configurations = {
    ".json": '{{"auth_token": "{}", "client_id": "client12345", "auth_url": "https://auth.example.com"}}',
    ".js": 'const AUTH_TOKEN = "{}";\nconst CLIENT_ID = "client12345";\nconst AUTH_URL = "https://auth.example.com";\n',
    ".yaml": "auth:\n  token: {}\n  client_id: client12345\n  auth_url: https://auth.example.com\n",
    ".properties": "auth.token={}\nauth.client_id=client12345\nauth.url=https://auth.example.com\n",
    ".conf": "auth_token={}\nclient_id=client12345\nauth_url=https://auth.example.com\n",
}

# Tokens de autorización ficticios
auth_tokens = [
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.authToken1",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.authToken2",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.authToken3",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.authToken4",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.authToken5",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.authToken6",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.authToken7",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.authToken8",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.authToken9",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.authToken10",
]

# Crear 10 archivos con configuraciones diferentes
for i in range(1, 11):
    # Seleccionar una extensión y un token de autorización al azar
    ext = random.choice(extensions)
    auth_token = random.choice(auth_tokens)
    
    # Generar el contenido del archivo
    content = auth_configurations[ext].format(auth_token)
    
    # Crear el nombre del archivo
    file_name = f"auth_config_{i}{ext}"
    file_path = os.path.join(output_dir, file_name)
    
    # Guardar el contenido en el archivo
    with open(file_path, "w") as file:
        file.write(content)

# Mostrar mensaje de éxito
print(f"Se crearon 10 archivos de configuración de autorización en el directorio '{output_dir}'.")


