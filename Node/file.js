// ============================================================
// Auth
// ============================================================
const AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.authToken1";
const CLIENT_ID = "client12345";
const AUTH_URL = "https://auth.example.com";

// ============================================================
// API
// ============================================================
const API_KEY = "UVWXY-67890-ABCDE-12345-ZABCD";
const API_ENDPOINT = "https://api.example.com";
const TIMEOUT = 30; // Tiempo en segundos

// ============================================================
// CONFIGURACIÓN DE TOKEN
// ============================================================
const authToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.exampleToken5";
const service = "api_service";

function mostrarAuthConfig() {
  console.log("Configuración de Autenticación:");
  console.log(`  Auth Token: ${AUTH_TOKEN}`);
  console.log(`  Client ID: ${CLIENT_ID}`);
  console.log(`  Auth URL: ${AUTH_URL}`);
}

function mostrarApiConfig() {
  console.log("Configuración de API:");
  console.log(`  API Key: ${API_KEY}`);
  console.log(`  API Endpoint: ${API_ENDPOINT}`);
  console.log(`  Timeout: ${TIMEOUT} segundos`);
}

function mostrarTokenConfig() {
  console.log("Configuración de Token:");
  console.log(`  Auth Token: ${authToken}`);
  console.log(`  Service: ${service}`);
}

console.log("=== Mostrando Configuraciones ===");
mostrarAuthConfig();
mostrarApiConfig();
mostrarTokenConfig();

