'use client';

import { Geist, Geist_Mono, Roboto_Slab } from "next/font/google";
import "./globals.css";
import ResponsiveAppBar from "@/components/navbar/ResponsiveAppBar";
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

const robotoSlab = Roboto_Slab({
  variable: "--font-roboto-slab",
  subsets: ["latin"],
  weight: ["300", "400", "500", "700"],
});

// Create a theme instance
const theme = createTheme({
  palette: {
    primary: {
      main: '#556cd6',
    },
    secondary: {
      main: '#19857b',
    },
  },
  typography: {
    fontFamily: geistSans.style.fontFamily,
    // Define specific variants to use Roboto Slab
    h1: {
      fontFamily: 'var(--font-roboto-slab)',
    },
    h2: {
      fontFamily: 'var(--font-roboto-slab)',
    },
    h3: {
      fontFamily: 'var(--font-roboto-slab)',
    },
    h4: {
      fontFamily: 'var(--font-roboto-slab)',
    },
    h5: {
      fontFamily: 'var(--font-roboto-slab)',
    },
    h6: {
      fontFamily: 'var(--font-roboto-slab)',
    },
  },
});

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${robotoSlab.variable} antialiased`}
      >
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <ResponsiveAppBar />
          <main>{children}</main>
        </ThemeProvider>
      </body>
    </html>
  );
}
