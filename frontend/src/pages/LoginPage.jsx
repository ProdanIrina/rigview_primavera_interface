import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {
  Box,
  Paper,
  Typography,
  TextField,
  Button,
  Checkbox,
  FormControlLabel,
  Alert
} from "@mui/material";
import { saveToken } from "../utils/auth";

export default function LoginPage() {
  // Vezi dacă există credentiale salvate (userul real sau de test, ce primești de la API)
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [rememberMe, setRememberMe] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  // La montare, opțional: încearcă să preiei user/parolă din API (dacă există și remember)
  useEffect(() => {
    fetch("http://localhost:8000/credentials/latest")
      .then(res => res.json())
      .then(data => {
        if (data?.username && data?.password) {
          setUsername(data.username);
          setPassword(data.password);  // În real life, parola nu ar trebui să fie vizibilă așa, dar pentru mock e ok
          setRememberMe(true);
        }
      })
      .catch(() => {});
  }, []);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password, remember: rememberMe })
      });

      const data = await response.json();

      if (response.ok) {
        saveToken(data.token);
        navigate("/dashboard");
      } else {
        setError(data.detail || "Autentificare eșuată");
      }
    } catch (err) {
      setError("Eroare conexiune cu serverul");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box
      minHeight="100vh"
      display="flex"
      justifyContent="center"
      alignItems="center"
      sx={{ background: "#f4f6fa" }}
    >
      <Paper elevation={6} sx={{ p: 4, minWidth: 340, maxWidth: 400 }}>
        <Typography variant="h5" fontWeight={600} mb={3} align="center">
          Autentificare Interfață
        </Typography>
        <form onSubmit={handleLogin}>
          <TextField
            fullWidth
            label="Utilizator Primavera"
            margin="normal"
            autoFocus
            value={username}
            onChange={e => setUsername(e.target.value)}
            required
            autoComplete="username"
          />
          <TextField
            fullWidth
            label="Parolă"
            type="password"
            margin="normal"
            value={password}
            onChange={e => setPassword(e.target.value)}
            required
            autoComplete="current-password"
          />
          <FormControlLabel
            control={
              <Checkbox
                checked={rememberMe}
                onChange={e => setRememberMe(e.target.checked)}
              />
            }
            label="Ține-mă minte"
            sx={{ mb: 2 }}
          />
          {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 1, fontWeight: 600 }}
            disabled={loading}
          >
            {loading ? "Se autentifică..." : "Login"}
          </Button>
          <Box mt={2} color="text.secondary" fontSize={13} textAlign="center">
            {/* Poți ascunde pe PROD! */}
            Pentru test rapid: <b>testuser</b> / <b>testpass</b>
          </Box>
        </form>
      </Paper>
    </Box>
  );
}
