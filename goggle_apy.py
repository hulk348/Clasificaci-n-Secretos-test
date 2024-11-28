import os
import random

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/config_file_Google_API_Key"
os.makedirs(output_dir, exist_ok=True)

# Extensiones de archivos
extensions = [".json", ".ml_conf"]

# Ejemplo de configuraciones con Google API Key para cada tipo de archivo
google_configurations = {
    ".json": '{{"google_api_key": "{}", "service": "maps"}}',
    ".ml_conf": "google_api_key: {}\nservice: translate\n",
}

# Claves API ficticias
google_api_keys = [
    "AIzaSyDk3eXAMPLE1234abcdEfgh5678",
    "AIzaSyAbCwFakSYz1234ExampleAPIkey",
    "AIzaSyC6UtExAmPlE5678FakeApikey",
    "AIzaSyXyzFakeKEY123456789abcDEF",
    "AIzaSyFake4567eXAMPKeyabcD1234",
    "AIzaSy1234EXAmPlEfAKEApiKey789",
    "AIzaSyTestAPkEy56789example1234",
    "AIzaSyFake1234eKeyExampleTest567",
    "AIzaSyExample789ApiFakeKEY1234",
    "AIzaSyFakeAPI4567EXampleKey123",
]

# Crear 10 archivos con configuraciones diferentes
for i in range(1, 11):
    # Seleccionar una extensión y una Google API Key al azar
    ext = random.choice(extensions)
    api_key = random.choice(google_api_keys)
    
    # Generar el contenido del archivo
    content = google_configurations[ext].format(api_key)
    
    # Crear el nombre del archivo
    file_name = f"google_config_{i}{ext}"
    file_path = os.path.join(output_dir, file_name)
    
    # Guardar el contenido en el archivo
    with open(file_path, "w") as file:
        file.write(content)

# Mostrar mensaje de éxito
print(f"Se crearon 10 archivos de configuración con Google API Key en el directorio '{output_dir}'.")


