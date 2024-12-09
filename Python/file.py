# ============================================================
# PASSWORD
# ============================================================
DB_USER = "admin"  # Usuario de la base de datos
DB_PASSWORD = "Password123!"  # Contraseña de la base de datos
DB_HOST = "localhost"  # Dirección del host de la base de datos

# ============================================================
# API KEY
# ============================================================
API_KEY = "AKIAEXAMPLE1122334455"  # Clave de acceso a la API
CLIENT_KEY = "Ck789ExampleClientKey"  # Clave del cliente
SERVICE = "example_service"  # Nombre del servicio


def conectar_base_datos():
    """Simula la conexión a una base de datos utilizando las credenciales."""
    print("Conectando a la base de datos...")
    print(f"Host: {DB_HOST}")
    print(f"Usuario: {DB_USER}")
    print("Contraseña: (oculta)")

def usar_api():
    """Simula el uso de una API utilizando las claves configuradas."""
    print("Usando la API...")
    print(f"API Key: {API_KEY}")
    print(f"Client Key: {CLIENT_KEY}")
    print(f"Servicio: {SERVICE}")

if __name__ == "__main__":
    conectar_base_datos()
    usar_api()

