import os

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/config_file_AWS"
os.makedirs(output_dir, exist_ok=True)

# Contenido de ejemplo para configuraciones con AWS Client ID
config_template = """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <service>
        <name>{service_name}</name>
        <awsClientId>{aws_client_id}</awsClientId>
        <region>{region}</region>
        <endpoint>https://{service_endpoint}.example.com</endpoint>
    </service>
</configuration>
"""

# Datos ficticios para los servicios
services = [
    ("DatabaseService", "AKIAEXAMPLE1234567890", "us-east-1"),
    ("PaymentGateway", "AKIAEXAMPLE0987654321", "us-west-2"),
    ("MessagingAPI", "AKIAEXAMPLE1122334455", "eu-central-1"),
    ("EmailService", "AKIAEXAMPLE5566778899", "ap-southeast-1"),
    ("CloudStorage", "AKIAEXAMPLEAABBCCDDEE", "us-east-2"),
]

# Crear 5 archivos XML con configuraciones
for i, (service_name, aws_client_id, region) in enumerate(services, start=1):
    file_name = f"{service_name}_config.xml"
    file_path = os.path.join(output_dir, file_name)
    content = config_template.format(
        service_name=service_name,
        aws_client_id=aws_client_id,
        region=region,
        service_endpoint=service_name.lower()
    )
    with open(file_path, "w") as file:
        file.write(content)

# Mostrar mensaje de éxito
print(f"Se generaron 5 archivos XML con configuraciones en el directorio '{output_dir}'.")


