package mongodb;

import org.springframework.context.annotation.Configuration;

@Configuration
public class MongoConfig4 {

    // Variables únicas para este archivo
    private final String USER = "SUPERUSER";
    private final String PASSWORD = "SUPERSECRETPASS123";
    private final String SERVER = "MONGODB.CLOUD.SERVER4";

    public String getUser() {
        return USER;
    }

    public String getPassword() {
        return PASSWORD;
    }

    public String getServer() {
        return SERVER;
    }

    public String getMongoClientUri() {
        try {
            // Construir la URI de MongoDB dinámicamente
            String mongoClientUri = "mongodb+srv://" + USER + ":" + PASSWORD + "@" + SERVER + "/superdb";
            return mongoClientUri;
        } catch (Exception e) {
            // Manejar posibles errores en la construcción de la URI
            System.err.println("Error al construir la URI de MongoDB: " + e.getMessage());
            return null;
        }
    }

    @Override
    public String toString() {
        return "MongoConfig4{" +
                "USER='" + USER + '\'' +
                ", PASSWORD='" + PASSWORD + '\'' +
                ", SERVER='" + SERVER + '\'' +
                ", mongoClientUri='" + getMongoClientUri() + '\'' +
                '}';
    }
}

