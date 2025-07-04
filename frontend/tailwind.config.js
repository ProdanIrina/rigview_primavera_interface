export default {
    content: [
      "./index.html",
      "./src/**/*.{js,jsx,ts,tsx}",
    ],
    theme: {
      extend: {
        colors: {
          border: "hsl(var(--color-border) / <alpha-value>)",
          input: "hsl(var(--color-input) / <alpha-value>)",
          ring: "hsl(var(--color-ring) / <alpha-value>)",
          background: "hsl(var(--color-background) / <alpha-value>)",
          foreground: "hsl(var(--color-foreground) / <alpha-value>)",
          primary: "hsl(var(--color-primary) / <alpha-value>)",
          "primary-foreground": "hsl(var(--color-primary-foreground) / <alpha-value>)",
          secondary: "hsl(var(--color-secondary) / <alpha-value>)",
          "secondary-foreground": "hsl(var(--color-secondary-foreground) / <alpha-value>)",
          destructive: "hsl(var(--color-destructive) / <alpha-value>)",
          "destructive-foreground": "hsl(var(--color-destructive-foreground) / <alpha-value>)",
          muted: "hsl(var(--color-muted) / <alpha-value>)",
          "muted-foreground": "hsl(var(--color-muted-foreground) / <alpha-value>)",
          accent: "hsl(var(--color-accent) / <alpha-value>)",
          "accent-foreground": "hsl(var(--color-accent-foreground) / <alpha-value>)",
          card: "hsl(var(--color-card) / <alpha-value>)",
          "card-foreground": "hsl(var(--color-card-foreground) / <alpha-value>)",
        },
        borderRadius: {
          lg: "var(--radius)",
          md: "calc(var(--radius) - 2px)",
          sm: "calc(var(--radius) - 4px)",
        },
      },
    },
    plugins: [],
  }
  