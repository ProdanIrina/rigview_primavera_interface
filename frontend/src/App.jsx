import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import DashboardPage from "./pages/DashboardPage";
import SyncPage from "./pages/SyncPage";
import LogsPage from "./pages/LogsPage";
import LoginPage from "./pages/LoginPage";
import { SnackbarProvider } from "notistack";

function App() {
  return (
    <SnackbarProvider maxSnack={3}>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/" element={<Layout />}>
            <Route index element={<DashboardPage />} />
            <Route path="dashboard" element={<DashboardPage />} />
            <Route path="sync" element={<SyncPage />} />
            <Route path="logs" element={<LogsPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </SnackbarProvider>
  );
}

export default App;
