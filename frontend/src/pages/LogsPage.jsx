import React from "react";
import {
  Typography, Table, TableBody, TableCell, TableContainer,
  TableHead, TableRow, Paper, Chip, Box, TextField
} from "@mui/material";

const mockLogs = [
  { date: "2024-06-27 08:00", level: "info", message: "Sincronizare pornită." },
  { date: "2024-06-27 08:01", level: "error", message: "Conexiune eșuată la API Primavera." },
  { date: "2024-06-27 08:02", level: "info", message: "Retry programat." },
];

function LogsPage() {
  const [search, setSearch] = React.useState("");

  const filteredLogs = mockLogs.filter(
    log =>
      log.message.toLowerCase().includes(search.toLowerCase()) ||
      log.level.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <Box sx={{ maxWidth: "100%" }}>
      <Box display="flex" alignItems="center" justifyContent="space-between" mb={4}>
        <Typography variant="h5" fontWeight={600}>Loguri</Typography>
        <TextField
          label="Caută în loguri"
          size="small"
          value={search}
          onChange={e => setSearch(e.target.value)}
          sx={{ minWidth: 220 }}
        />
      </Box>
      <TableContainer component={Paper} sx={{ borderRadius: 3, boxShadow: 3 }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell><b>Data</b></TableCell>
              <TableCell><b>Tip</b></TableCell>
              <TableCell><b>Mesaj</b></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {filteredLogs.length === 0 ? (
              <TableRow>
                <TableCell colSpan={3} align="center">Nu există loguri.</TableCell>
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
                  <TableCell>{log.message}</TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}

export default LogsPage;
