import os
import random
import csv

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/conf_file_password"
os.makedirs(output_dir, exist_ok=True)

# Contraseñas ficticias
passwords = [
    "Password123!", "SecurePass456$", "MySecret789#", "AdminKey2023",
    "TestPass@2024", "UserKey#987", "DevSecret%001", "RandomKey*&76",
    "Encrypted$Key", "BackupPass$!"
]

# Servicios ficticios
services = [
    "database", "api", "backup", "email", "ftp", "webapp",
    "cloud_storage", "analytics", "devops_tool", "messaging_service"
]

# Crear 20 archivos CSV con configuraciones diferentes
for i in range(1, 21):
    file_name = f"config_{i}.csv"
    file_path = os.path.join(output_dir, file_name)

    # Generar filas de configuraciones aleatorias
    rows = []
    for service in services:
        rows.append({
            "Service": service,
            "Username": f"user_{service}",
            "Password": random.choice(passwords),
            "Endpoint": f"https://{service}.example.com",
            "Port": random.randint(1000, 9999)
        })

    # Escribir contenido en el archivo CSV
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Service", "Username", "Password", "Endpoint", "Port"])
        writer.writeheader()
        writer.writerows(rows)

# Mostrar mensaje de éxito
print(f"Se crearon 20 archivos CSV de configuración en el directorio '{output_dir}'.")


