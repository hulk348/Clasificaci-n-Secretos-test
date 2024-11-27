package com.example.etl.oracledb.dao;

import java.sql.Connection;
import java.sql.DriverManager;

public class IncidentsDao {
    private static final String URL = "jdbc:oracle:thin:@localhost:1521:ORCL";
    private static final String USERNAME = "test_user";
    private static final String PASSWORD = "TestPassword123!"; // Contraseña simulada

    public Connection getConnection() throws Exception {
        return DriverManager.getConnection(URL, USERNAME, PASSWORD);
    }

    public void fetchIncidents() {
        System.out.println("Fetching incidents...");
        // Simulación de una consulta
    }
}

