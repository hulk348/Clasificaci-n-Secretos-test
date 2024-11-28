import os

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/config_file_rsa_keys"
os.makedirs(output_dir, exist_ok=True)

# Plantilla de clave RSA privada tipo PEM
private_key_template = """-----BEGIN RSA PRIVATE KEY-----
MIIBOgIBAAJBALFzH6f7+/vbDehVjdhbdXpZBqvMLPLWqVGWcX8VRISZJqNSeG58
D1JnJ/pQiRVqakKlMk8iLGlX2QaBdd5qjaECAwEAAQJAE3Vt/qwMhdk+zSbsXBc+
9/EG+QfI+5RaF5LoDoOqOvzBJU23lN3xrzFylxRjvhr7nC4fp4n6OqRrZUTBxOXO
wQIhAPaxKpFHY9MbRLJho7O4DJaXzDlxysLFhnEhn3RHFIxDAiEAxkqDqV1LUHfS
ZwoqXudxEU7FELFgITJ2gyN3BRQyfGcCIHUAi7Cf52glR4DROGx6eRNW2YZ6b6xl
dAM4vAVQuosLAiAVbPHeoGAC2vFPmVWpmxaklzA+E2t8FtlPiLpQ/NbnvQIgKqSf
uXH7JZGUEq7Qz9KwgiqEFfdH5gAKWEse2u44DTw=
-----END RSA PRIVATE KEY-----
"""

# Crear 30 archivos con extensiones .pem y .key
for i in range(1, 16):  # 15 archivos .pem
    file_name = f"private_key_{i}.pem"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, "w") as file:
        file.write(private_key_template)

for i in range(16, 31):  # 15 archivos .key
    file_name = f"private_key_{i}.key"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, "w") as file:
        file.write(private_key_template)

# Mostrar mensaje de éxito
print(f"Se generaron 30 archivos RSA privados en el directorio '{output_dir}'.")


