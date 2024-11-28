import os
import random

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/config_file_jwt"
os.makedirs(output_dir, exist_ok=True)

# Extensiones de archivos
extensions = [".yaml", ".properties", ".yml"]

# Ejemplo de configuraciones con JWT para cada tipo de archivo
jwt_configurations = {
    ".yaml": "auth:\n  jwt: \"{}\"\n  token_expiry: 3600\n",
    ".properties": "auth.jwt={}\nauth.token_expiry=3600\n",
    ".yml": "authentication:\n  jwt: \"{}\"\n  token_lifetime: 3600\n",
}

# Ficticios JSON Web Tokens
jwt_tokens = [
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.s5Gh6Bh8hBv5vGBm6",
    "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJteXNlcnZlci5jb20iLCJ1c2VyIjoiYWxpY2UiLCJleHAiOjE2ODAwMDAwMDB9.aSd1b6cgh6Ah5b34bgH5",
    "eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjM0LCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE2NzgxMDAwMDB9.Xy6Zg5Nb5D6Ng3c5L4G5",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXlsb2FkIjoiZXhhbXBsZSJ9.6H5Yhg6HgJgNbgH5Bg5",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.3G5Y6hgHbGg5g5J5J5",
    "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYm9iIiwiYWRtaW4iOmZhbHNlfQ.D5L5F6H6B5L5FgFg6Fg",
    "eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJyb2xlIjoiYWRtaW4ifQ.P5K5J6G5H6K5B6G5",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXlsb2FkIjoiYW5vdGhlci1leGFtcGxlIn0.2J4G6H5G5H6B5G6H5",
    "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiY2hhcmxpZSIsImV4cCI6MTY4MDAwMDB9.X6G5H5J5H6B5N6M5H",
    "eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzgxMDAwMDB9.P6N5J5H6B5G5F6H5",
]

# Crear 30 archivos con configuraciones diferentes
for i in range(1, 31):
    # Seleccionar una extensión y un JWT al azar
    ext = random.choice(extensions)
    jwt_token = random.choice(jwt_tokens)
    
    # Generar el contenido del archivo
    content = jwt_configurations[ext].format(jwt_token)
    
    # Crear el nombre del archivo
    file_name = f"jwt_config_{i}{ext}"
    file_path = os.path.join(output_dir, file_name)
    
    # Guardar el contenido en el archivo
    with open(file_path, "w") as file:
        file.write(content)

# Mostrar mensaje de éxito
print(f"Se crearon 30 archivos de configuración de JSON Web Tokens en el directorio '{output_dir}'.")


