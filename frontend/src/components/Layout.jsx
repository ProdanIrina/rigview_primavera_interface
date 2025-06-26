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
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <AppBar position="fixed" sx={{ zIndex: 1201 }}>
        <Toolbar
          variant="dense"
          sx={{
            minHeight: 56,
            display: "flex",
            alignItems: "center",
            px: 2,
          }}
        >
          <Box display="flex" alignItems="center" sx={{ flexGrow: 1 }}>
            <img
              src="/logo.png"
              alt="Logo"
              height="40"
              style={{
                background: "white",
                borderRadius: 8,
                padding: 3,
                marginRight: 18,
                boxShadow: "0 0 6px #0002",
                marginTop: 8,        // mai jos
                marginBottom: 4,     // spațiu jos
                display: "block",
              }}
            />
            <Typography
              variant="h6"
              sx={{
                fontSize: 26,
                fontWeight: 500,
                lineHeight: 1.1,
                mt: 1, // puțin mai sus față de logo
              }}
            >
              RigView–Primavera Interface
            </Typography>
          </Box>
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
        <Toolbar variant="dense" sx={{ minHeight: 56 }} />
        <List>
          {menuItems.map((item) => (
            <ListItem button component={Link} to={item.path} key={item.text}>
              <ListItemIcon>{item.icon}</ListItemIcon>
              <ListItemText primary={item.text} />
            </ListItem>
          ))}
        </List>
      </Drawer>
      <Box component="main" sx={{ flexGrow: 1, pl: 0, pr: 2, pt: 3, ml: '22px' }}>
        <Toolbar variant="dense" sx={{ minHeight: 56 }} />
        <Outlet />
      </Box>
    </Box>
  );
}

export default Layout;
