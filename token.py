import os
import random

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/config_file_token"
os.makedirs(output_dir, exist_ok=True)

# Extensiones de archivos
extensions = [".json", ".js", ".yaml", ".properties", ".conf"]

# Ejemplo de configuraciones con Token para cada tipo de archivo
token_configurations = {
    ".json": '{{"auth_token": "{}", "service": "api_service"}}',
    ".js": 'const authToken = "{}";\nconst service = "api_service";\n',
    ".yaml": "auth:\n  token: {}\n  service: api_service\n",
    ".properties": "auth.token={}\nservice=api_service\n",
    ".conf": "auth_token={}\nservice=api_service\n",
}

# Tokens ficticios
tokens = [
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.exampleToken1",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.exampleToken2",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.exampleToken3",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.exampleToken4",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.exampleToken5",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.exampleToken6",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.exampleToken7",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.exampleToken8",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.exampleToken9",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.exampleToken10",
]

# Crear 10 archivos con configuraciones diferentes
for i in range(1, 11):
    # Seleccionar una extensión y un token al azar
    ext = random.choice(extensions)
    token = random.choice(tokens)
    
    # Generar el contenido del archivo
    content = token_configurations[ext].format(token)
    
    # Crear el nombre del archivo
    file_name = f"token_config_{i}{ext}"
    file_path = os.path.join(output_dir, file_name)
    
    # Guardar el contenido en el archivo
    with open(file_path, "w") as file:
        file.write(content)

# Mostrar mensaje de éxito
print(f"Se crearon 10 archivos de configuración con tokens en el directorio '{output_dir}'.")


