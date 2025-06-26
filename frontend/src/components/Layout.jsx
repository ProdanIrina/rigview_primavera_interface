import React from "react";
import { AppBar, Toolbar, Typography, Box, CssBaseline, Drawer, List, ListItem, ListItemIcon, ListItemText, IconButton, Tooltip } from "@mui/material";
import { Dashboard, ListAlt, Sync, Logout } from "@mui/icons-material";
import { Link, Outlet, useNavigate } from "react-router-dom";

const drawerWidth = 220;

const menuItems = [
  { text: "Dashboard", icon: <Dashboard />, path: "/dashboard" },
  { text: "Sync", icon: <Sync />, path: "/sync" },
  { text: "Loguri", icon: <ListAlt />, path: "/logs" },
];

function Layout() {
  const navigate = useNavigate();

  const handleLogout = () => {
    // aici ștergi tokenul, sesiunea, etc.
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <AppBar position="fixed" sx={{ zIndex: 1201 }}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            <img src="/logo.png" alt="Logo" height="40" style={{ verticalAlign: "middle", marginRight: 12 }} />
            RigView–Primavera Interface
          </Typography>
          <Tooltip title="Deconectare">
            <IconButton color="inherit" onClick={handleLogout}>
              <Logout />
            </IconButton>
          </Tooltip>
        </Toolbar>
      </AppBar>
      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: "border-box" }
        }}
      >
        <Toolbar />
        <List>
          {menuItems.map((item) => (
            <ListItem button component={Link} to={item.path} key={item.text}>
              <ListItemIcon>{item.icon}</ListItemIcon>
              <ListItemText primary={item.text} />
            </ListItem>
          ))}
        </List>
      </Drawer>
      <Box component="main" sx={{ flexGrow: 1, p: 3, ml: `${drawerWidth}px` }}>
        <Toolbar />
        <Outlet /> {/* aici se randează paginile din router */}
      </Box>
    </Box>
  );
}

export default Layout;
