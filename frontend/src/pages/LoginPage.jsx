import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { saveToken } from "../utils/auth";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [rememberMe, setRememberMe] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

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
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <form
        onSubmit={handleLogin}
        className="bg-white p-8 rounded shadow-md w-full max-w-sm"
      >
        <h2 className="text-2xl font-semibold mb-6">Autentificare Primavera</h2>

        <input
          type="text"
          placeholder="Utilizator"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="mb-4 w-full p-2 border rounded"
          required
        />

        <input
          type="password"
          placeholder="Parolă"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="mb-4 w-full p-2 border rounded"
          required
        />

        <label className="flex items-center mb-4">
          <input
            type="checkbox"
            checked={rememberMe}
            onChange={() => setRememberMe(!rememberMe)}
            className="mr-2"
          />
          Ține-mă minte
        </label>

        {error && <p className="text-red-500 mb-2">{error}</p>}

        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
        >
          Login
        </button>
      </form>
    </div>
  );
}
