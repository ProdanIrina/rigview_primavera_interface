import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Layout from "./components/Layout";
import DashboardPage from "./pages/DashboardPage";
import SyncPage from "./pages/SyncPage";
import LogsPage from "./pages/LogsPage";
import LoginPage from "./pages/LoginPage";
import { SnackbarProvider } from "notistack";
import ProtectedRoute from "./components/ProtectedRoute";

function App() {
  return (
    <SnackbarProvider maxSnack={3}>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          {/* Toate rutele "private" sub Layout, protejate */}
          <Route element={<ProtectedRoute><Layout /></ProtectedRoute>}>
            <Route index element={<Navigate to="/dashboard" />} />
            <Route path="/dashboard" element={<DashboardPage />} />
            <Route path="/sync" element={<SyncPage />} />
            <Route path="/logs" element={<LogsPage />} />
          </Route>
          {/* Catch-all pentru rute greșite */}
          <Route path="*" element={<Navigate to="/dashboard" />} />
        </Routes>
      </BrowserRouter>
    </SnackbarProvider>
  );
}

export default App;
