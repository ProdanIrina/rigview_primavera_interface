import React from "react";
import {
  Typography, Table, TableBody, TableCell, TableContainer,
  TableHead, TableRow, Paper, Chip, Button, Box, CircularProgress
} from "@mui/material";
import { useSnackbar } from "notistack";

function DashboardPage() {
  const [syncData, setSyncData] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const { enqueueSnackbar } = useSnackbar();

  React.useEffect(() => {
    fetch("http://localhost:8000/sync/activities")
      .then(res => res.json())
      .then(data => { setSyncData(data); setLoading(false); })
      .catch(err => { enqueueSnackbar("Eroare la încărcarea sincronizărilor!", { variant: "error" }); setLoading(false); });
  }, []);

  const handleManualSync = () => {
    enqueueSnackbar("Sincronizare manuală pornită!", { variant: "info" });
  };

  return (
    <Box sx={{ maxWidth: "100%" }}>
      <Box display="flex" alignItems="center" justifyContent="space-between" mb={4}>
        <Typography variant="h5" fontWeight={600}>Status Sincronizări</Typography>
        <Button variant="contained" onClick={handleManualSync}>Sincronizare manuală</Button>
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
                <TableCell><b>Status</b></TableCell>
                <TableCell><b>Mesaj</b></TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {syncData.length === 0 ? (
                <TableRow>
                  <TableCell colSpan={3} align="center">Nu există sincronizări.</TableCell>
                </TableRow>
              ) : (
                syncData.map((row, idx) => (
                  <TableRow key={idx}>
                    <TableCell>{row.date || row.timestamp}</TableCell>
                    <TableCell>
                      <Chip
                        label={
                          row.status === "success"
                            ? "Succes"
                            : row.status === "error"
                            ? "Eroare"
                            : "În curs"
                        }
                        color={
                          row.status === "success"
                            ? "success"
                            : row.status === "error"
                            ? "error"
                            : "warning"
                        }
                        sx={{ minWidth: 90, fontWeight: 600 }}
                      />
                    </TableCell>
                    <TableCell>{row.message}</TableCell>
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
export default DashboardPage;
