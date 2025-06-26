import React from "react";
import { Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Chip, Button, Box, CircularProgress } from "@mui/material";
import { useSnackbar } from "notistack";

function DashboardPage() {
  const [syncData, setSyncData] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const { enqueueSnackbar } = useSnackbar();

  // Fetch datele la montare componentă
  React.useEffect(() => {
    fetch("http://localhost:8000/sync/activities")
      .then(res => res.json())
      .then(data => {
        setSyncData(data); // data trebuie să fie un array de loguri de sync
        setLoading(false);
      })
      .catch(err => {
        enqueueSnackbar("Eroare la încărcarea sincronizărilor!", { variant: "error" });
        setLoading(false);
      });
  }, []);

  const handleManualSync = () => {
    enqueueSnackbar("Sincronizare manuală pornită!", { variant: "info" });
    // Opțional, poți face POST la /sync/activities să declanșezi sync-ul
  };

  return (
    <>
      <Box display="flex" alignItems="center" justifyContent="space-between" mb={2}>
        <Typography variant="h5">Status Sincronizări</Typography>
        <Button variant="contained" onClick={handleManualSync}>Sincronizare manuală</Button>
      </Box>
      {loading ? (
        <Box display="flex" justifyContent="center" alignItems="center" minHeight={200}>
          <CircularProgress />
        </Box>
      ) : (
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Data</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Mesaj</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {syncData.map((row, idx) => (
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
                    />
                  </TableCell>
                  <TableCell>{row.message}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </>
  );
}
export default DashboardPage;
