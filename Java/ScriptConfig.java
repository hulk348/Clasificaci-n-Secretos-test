package mongodb;

import org.springframework.context.annotation.Configuration;

@Configuration
public class MongoConfig2 {

    // Variables únicas para este archivo
    public final String USER = "MONGOUSER2";
    public final String PASSWORD = "MONGOPASSWORD456";   #Password
    public final String SERVER = "MONGODB.CLOUD.SERVER2";

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
            String mongoClientUri = "mongodb+srv://" + USER + ":" + PASSWORD + "@" + SERVER + "/sampledb?retryWrites=true&w=majority";     ##Auth
            return mongoClientUri;
        } catch (Exception e) {
            // Manejar posibles errores en la construcción de la URI
            System.err.println("Error al construir la URI de MongoDB: " + e.getMessage());
            return null;
        }
    }

    @Override
    public String toString() {
        return "MongoConfig2{" +
                "USER='" + USER + '\'' +
                ", PASSWORD='" + PASSWORD + '\'' +
                ", SERVER='" + SERVER + '\'' +
                ", mongoClientUri='" + getMongoClientUri() + '\'' +
                '}';
    }
}

public class AuthConfig {


    public static final String BAR = "/";
    public static final String SECRET= "mySecretKey123";      ###Secret
    public static final String TOKEN = "sampleToekn123";
    public static final String SEPARATOR= ";";
    public static final String SECRET= "https://api.example.com";

}

package com.example.etl.oracledb.dao;

import java.sql.Connection;
import java.sql.DriverManager;


public class IncidentsDao {
    final String URL = "jdbc:oracle:thin:@localhost:1521:ORCL";
    final String authUser = "test_user";
    final String authPassword = "TestPassword123!"; 

    public Connection getConnection() throws Exception {
        return DriverManager.getConnection(URL, authUser, authPassword);
    }

    public void fetchIncidents() {
        System.out.println("Fetching incidents...");
        // Simulación de una consulta
    }
}
