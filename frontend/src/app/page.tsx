'use client';

import React from 'react';
import { Container, Typography, Box, Button, Paper } from '@mui/material';

export default function HomePage() {
  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Box 
        sx={{ 
          py: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          textAlign: 'center'
        }}
      >
        <Typography variant="h2" component="h1" gutterBottom>
          Welcome to MangaSh1r0
        </Typography>
        
        <Typography variant="h5" color="text.secondary" paragraph>
          Your place for tracking anime and manga - powered by AniList API
        </Typography>
        
        <Box sx={{ mt: 4 }}>
          <Button variant="contained" color="primary" size="large" href="/anime" sx={{ mx: 1 }}>
            Browse Anime
          </Button>
          <Button variant="outlined" color="primary" size="large" href="/manga" sx={{ mx: 1 }}>
            Browse Manga
          </Button>
        </Box>
      </Box>
      
      <Box sx={{ 
        mt: 4, 
        display: 'flex', 
        flexDirection: { xs: 'column', md: 'row' },
        gap: 4
      }}>
        <Box sx={{ flex: 1 }}>
          <Paper elevation={3} sx={{ p: 3, height: '100%' }}>
            <Typography variant="h5" gutterBottom>
              Track Your Progress
            </Typography>
            <Typography paragraph>
              Keep track of your anime and manga progress, rate titles, and create your personalized watchlist.
            </Typography>
          </Paper>
        </Box>
        <Box sx={{ flex: 1 }}>
          <Paper elevation={3} sx={{ p: 3, height: '100%' }}>
            <Typography variant="h5" gutterBottom>
              Discover New Content
            </Typography>
            <Typography paragraph>
              Find new anime and manga based on your interests and what's popular in the community.
            </Typography>
          </Paper>
        </Box>
      </Box>
    </Container>
  );
}
