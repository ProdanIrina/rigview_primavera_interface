import React from "react";
import { Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Chip, Box, TextField } from "@mui/material";

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
    <>
      <Box display="flex" alignItems="center" justifyContent="space-between" mb={2}>
        <Typography variant="h5">Loguri</Typography>
        <TextField label="Caută în loguri" size="small" value={search} onChange={e => setSearch(e.target.value)} />
      </Box>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Data</TableCell>
              <TableCell>Tip</TableCell>
              <TableCell>Mesaj</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {filteredLogs.map((log, idx) => (
              <TableRow key={idx}>
                <TableCell>{log.date}</TableCell>
                <TableCell>
                  <Chip
                    label={log.level === "error" ? "Eroare" : "Info"}
                    color={log.level === "error" ? "error" : "info"}
                  />
                </TableCell>
                <TableCell>{log.message}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  );
}
export default LogsPage;
