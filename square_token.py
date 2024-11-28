import os

# Directorio donde se guardarán los archivos
output_dir = "/mnt/c/Windows/system32/Clasificaci-n-Secretos-test/config_file_square_token"
os.makedirs(output_dir, exist_ok=True)

# Extensiones de archivos
extensions = [".dts", ".process"]

# Ejemplo de configuraciones con Square Access Token para cada tipo de archivo
square_token_configurations = {
    ".dts": """<configuration>
  <service>
    <name>SquareService</name>
    <accessToken>{}</accessToken>
    <endpoint>https://connect.squareup.com/v2/</endpoint>
  </service>
</configuration>""",
    ".process": """process:
  name: SquareDataProcess
  square_access_token: "{}"
  endpoint: "https://connect.squareup.com/v2/"
  action: fetch_data
"""
}

# Square Access Tokens ficticios
square_tokens = [
    "EAAAEXAMPLE1234567890abcdefghijklmn",
    "EAAAEXAMPLESIMULATED0987654321opqrstuv",
    "EAAAEXAMPLESQUARE09876abcdefgHIJKLMN",
]

# Crear 3 archivos con configuraciones diferentes
for i in range(1, 4):
    # Seleccionar una extensión y un Square Access Token al azar
    ext = extensions[i % len(extensions)]
    square_token = square_tokens[i - 1]
    
    # Generar el contenido del archivo
    content = square_token_configurations[ext].format(square_token)
    
    # Crear el nombre del archivo
    file_name = f"square_config_{i}{ext}"
    file_path = os.path.join(output_dir, file_name)
    
    # Guardar el contenido en el archivo
    with open(file_path, "w") as file:
        file.write(content)

# Mostrar mensaje de éxito
print(f"Se crearon 3 archivos de configuración de Square Access Token en el directorio '{output_dir}'.")


