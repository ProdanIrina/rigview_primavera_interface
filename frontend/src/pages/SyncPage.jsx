import React from "react";
import { Typography, Button, Box } from "@mui/material";
import { useSnackbar } from "notistack";

function SyncPage() {
  const { enqueueSnackbar } = useSnackbar();

  const handleSync = () => {
    enqueueSnackbar("Sincronizare pornită!", { variant: "info" });
    // Aici poți face efectiv request-ul de sync
  };

  return (
    <Box>
      <Typography variant="h5" mb={2}>Sincronizare manuală</Typography>
      <Button variant="contained" onClick={handleSync}>Pornește sincronizarea</Button>
    </Box>
  );
}
export default SyncPage;
