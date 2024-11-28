import os
import random

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/config_file_AWS"
os.makedirs(output_dir, exist_ok=True)

# Extensiones de archivos
extensions = [
    ".yaml", ".yml", ".ini", ".properties", ".back", ".etx",
    ".json", ".py", ".php", ".conf", ".ps1"
]

# Ejemplo de configuraciones con AWS Client ID para cada tipo de archivo
aws_configurations = {
    ".yaml": "aws:\n  client_id: {}\n  region: us-east-1\n",
    ".yml": "auth:\n  aws_client_id: {}\n  region: us-west-2\n",
    ".ini": "[aws]\nclient_id={}\nregion=us-east-1\n",
    ".properties": "aws.client_id={}\naws.region=us-east-1\n",
    ".back": "backup_aws_client_id={}\nbackup_region=us-west-1\n",
    ".etx": "external_aws_client_id={}\nendpoint=api.example.com\n",
    ".json": '{{"aws_client_id": "{}", "region": "us-east-1"}}',
    ".py": 'AWS_CLIENT_ID = "{}"\nAWS_REGION = "us-east-1"\n',
    ".php": '<?php\n$aws_client_id = "{}";\n$aws_region = "us-east-1";\n?>',
    ".conf": "aws_client_id={}\nregion=us-east-1\n",
    ".ps1": '$AWSClientID = "{}"\n$AWSRegion = "us-east-1"\n'
}

# IDs ficticios para los archivos
aws_client_ids = [
    "AKIAEXAMPLE1234567890", "AKIAEXAMPLE0987654321", "AKIAEXAMPLE1122334455",
    "AKIAEXAMPLE5566778899", "AKIAEXAMPLEAABBCCDDEE", "AKIAEXAMPLEREALID1234",
    "AKIAEXAMPLESIMULATED", "AKIAEXAMPLELONGKEY9876", "AKIAEXAMPLESHORT123",
    "AKIAEXAMPLERANDOM0987"
]

# Crear 20 archivos con configuraciones diferentes
for i in range(1, 21):
    # Seleccionar una extensión y un AWS Client ID al azar
    ext = random.choice(extensions)
    client_id = random.choice(aws_client_ids)
    
    # Generar el contenido del archivo
    content = aws_configurations[ext].format(client_id)
    
    # Crear el nombre del archivo
    file_name = f"aws_config_{i}{ext}"
    file_path = os.path.join(output_dir, file_name)
    
    # Guardar el contenido en el archivo
    with open(file_path, "w") as file:
        file.write(content)

# Mostrar mensaje de éxito
print(f"Se crearon 20 archivos de configuración con AWS Client ID en el directorio '{output_dir}'.")


