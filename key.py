import os
import random

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/config_file_key"
os.makedirs(output_dir, exist_ok=True)

# Extensiones de archivos
extensions = [".json", ".conf", ".php", ".py"]

# Ejemplo de configuraciones con Keys para cada tipo de archivo
key_configurations = {
    ".json": '{{"api_key": "{}", "client_key": "{}", "service": "example_service"}}',
    ".conf": "api_key={}\nclient_key={}\nservice=example_service\n",
    ".php": '<?php\n$api_key = "{}";\n$client_key = "{}";\n$service = "example_service";\n?>',
    ".py": 'API_KEY = "{}"\nCLIENT_KEY = "{}"\nSERVICE = "example_service"\n',
}

# Keys ficticias
api_keys = [
    "AKIAEXAMPLE1234567890",
    "AKIAEXAMPLE0987654321",
    "AKIAEXAMPLE1122334455",
    "AKIAEXAMPLE5566778899",
    "AKIAEXAMPLEAABBCCDDEE",
    "AKIAEXAMPLEZXY98765432",
    "AKIAEXAMPLEREALID1234",
    "AKIAEXAMPLESIMULATEDKEY",
    "AKIAEXAMPLENEW09876543",
    "AKIAEXAMPLESAMPLEKEY876"
]

client_keys = [
    "Ck123ExampleClientKey",
    "Ck456ExampleClientKey",
    "Ck789ExampleClientKey",
    "Ck101ExampleClientKey",
    "Ck112ExampleClientKey",
    "Ck131ExampleClientKey",
    "Ck415ExampleClientKey",
    "Ck161ExampleClientKey",
    "Ck718ExampleClientKey",
    "Ck192ExampleClientKey"
]

# Crear 10 archivos con configuraciones diferentes
for i in range(1, 11):
    # Seleccionar una extensión, un API Key y un Client Key al azar
    ext = random.choice(extensions)
    api_key = random.choice(api_keys)
    client_key = random.choice(client_keys)
    
    # Generar el contenido del archivo
    content = key_configurations[ext].format(api_key, client_key)
    
    # Crear el nombre del archivo
    file_name = f"key_config_{i}{ext}"
    file_path = os.path.join(output_dir, file_name)
    
    # Guardar el contenido en el archivo
    with open(file_path, "w") as file:
        file.write(content)

# Mostrar mensaje de éxito
print(f"Se crearon 10 archivos de configuración de Keys en el directorio '{output_dir}'.")


