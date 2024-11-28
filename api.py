import os
import random

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/config_file_api"
os.makedirs(output_dir, exist_ok=True)

# Extensiones de archivos
extensions = [".json", ".js", ".yaml", ".properties", ".conf"]

# Ejemplo de configuraciones con API para cada tipo de archivo
api_configurations = {
    ".json": '{{"api_key": "{}", "endpoint": "https://api.example.com", "timeout": 30}}',
    ".js": 'const API_KEY = "{}";\nconst API_ENDPOINT = "https://api.example.com";\nconst TIMEOUT = 30;\n',
    ".yaml": "api:\n  key: {}\n  endpoint: https://api.example.com\n  timeout: 30\n",
    ".properties": "api.key={}\napi.endpoint=https://api.example.com\napi.timeout=30\n",
    ".conf": "api_key={}\napi_endpoint=https://api.example.com\napi_timeout=30\n",
}

# API Keys ficticias
api_keys = [
    "12345-ABCDE-67890-FGHIJ-12345",
    "ABCDE-12345-FGHIJ-67890-KLMNO",
    "FGHIJ-ABCDE-67890-12345-PQRST",
    "67890-FGHIJ-ABCDE-12345-UVWXY",
    "UVWXY-67890-ABCDE-12345-ZABCD",
    "ZABCD-UVWXY-67890-FGHIJ-EFGHI",
    "EFGHI-ZABCD-UVWXY-ABCDE-KLMNO",
    "KLMNO-ABCDE-67890-FGHIJ-QRSTU",
    "QRSTU-KLMNO-ABCDE-67890-VWXYZ",
    "VWXYZ-QRSTU-KLMNO-ABCDE-12345",
]

# Crear 10 archivos con configuraciones diferentes
for i in range(1, 11):
    # Seleccionar una extensión y una API Key al azar
    ext = random.choice(extensions)
    api_key = random.choice(api_keys)
    
    # Generar el contenido del archivo
    content = api_configurations[ext].format(api_key)
    
    # Crear el nombre del archivo
    file_name = f"api_config_{i}{ext}"
    file_path = os.path.join(output_dir, file_name)
    
    # Guardar el contenido en el archivo
    with open(file_path, "w") as file:
        file.write(content)

# Mostrar mensaje de éxito
print(f"Se crearon 10 archivos de configuración de API en el directorio '{output_dir}'.")


