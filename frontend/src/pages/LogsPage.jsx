import React from "react";
import {
  Typography, Table, TableBody, TableCell, TableContainer,
  TableHead, TableRow, Paper, Chip, Box, TextField, CircularProgress, Button
} from "@mui/material";
import * as XLSX from "xlsx";

function LogsPage() {
  const [logs, setLogs] = React.useState([]);
  const [search, setSearch] = React.useState("");
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    fetch("http://localhost:8000/logs")
      .then(res => res.json())
      .then(data => {
        setLogs(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  const filteredLogs = logs.filter(
    log =>
      log.message.toLowerCase().includes(search.toLowerCase()) ||
      log.level.toLowerCase().includes(search.toLowerCase()) ||
      log.component.toLowerCase().includes(search.toLowerCase())
  );

  // Exportă în Excel
  const handleExportExcel = () => {
    // Convertim la format SheetJS-friendly
    const wsData = filteredLogs.map(log => ({
      Data: log.date,
      Tip: log.level === "error" ? "Eroare" : "Info",
      Componentă: log.component,
      Mesaj: log.message,
    }));

    const worksheet = XLSX.utils.json_to_sheet(wsData);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, "Loguri");
    XLSX.writeFile(workbook, "loguri_sincronizare.xlsx");
  };

  return (
    <Box sx={{ maxWidth: "100%" }}>
      <Box display="flex" alignItems="center" justifyContent="space-between" mb={4}>
        <Typography variant="h5" fontWeight={600}>Loguri</Typography>
        <Box display="flex" gap={2}>
          <TextField
            label="Caută în loguri"
            size="small"
            value={search}
            onChange={e => setSearch(e.target.value)}
            sx={{ minWidth: 220 }}
          />
          <Button variant="outlined" onClick={handleExportExcel}>
            Export Excel
          </Button>
        </Box>
      </Box>
      {loading ? (
        <Box display="flex" justifyContent="center" alignItems="center" minHeight={200}>
          <CircularProgress />
        </Box>
      ) : (
        <TableContainer component={Paper} sx={{ borderRadius: 3, boxShadow: 3 }}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell><b>Data</b></TableCell>
                <TableCell><b>Tip</b></TableCell>
                <TableCell><b>Componentă</b></TableCell>
                <TableCell><b>Mesaj</b></TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {filteredLogs.length === 0 ? (
                <TableRow>
                  <TableCell colSpan={4} align="center">Nu există loguri.</TableCell>
                </TableRow>
              ) : (
                filteredLogs.map((log, idx) => (
                  <TableRow key={idx}>
                    <TableCell>{log.date}</TableCell>
                    <TableCell>
                      <Chip
                        label={log.level === "error" ? "Eroare" : "Info"}
                        color={log.level === "error" ? "error" : "info"}
                        sx={{ minWidth: 70, fontWeight: 600 }}
                      />
                    </TableCell>
                    <TableCell>{log.component}</TableCell>
                    <TableCell>{log.message}</TableCell>
                  </TableRow>
                ))
              )}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Box>
  );
}

export default LogsPage;
