import React from "react";
import { Typography, Box, Button } from "@mui/material";
import { useSnackbar } from "notistack";

function SyncPage() {
  const { enqueueSnackbar } = useSnackbar();

  const handleSync = () => {
    enqueueSnackbar("Sincronizarea a pornit!", { variant: "info" });
    // Poți apela aici API-ul pentru sincronizare efectivă
  };

  return (
    <Box sx={{ maxWidth: "100%" }}>
      <Box display="flex" alignItems="center" justifyContent="space-between" mb={4}>
        <Typography variant="h5" fontWeight={600}>Sincronizare manuală</Typography>
      </Box>
      <Button variant="contained" onClick={handleSync}>
        PORNEȘTE SINCRONIZAREA
      </Button>
    </Box>
  );
}

export default SyncPage;
