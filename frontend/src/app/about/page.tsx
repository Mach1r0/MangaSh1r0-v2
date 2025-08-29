'use client';

import React from 'react';
import { Container, Typography, Box, Paper, Divider } from '@mui/material';

export default function AboutPage() {
  return (
    <Container maxWidth="md" sx={{ mt: 4, mb: 8 }}>
      <Box sx={{ mb: 6, textAlign: 'center' }}>
        <Typography variant="h2" component="h1" gutterBottom>
          About MangaSh1r0
        </Typography>
        <Typography variant="subtitle1" color="text.secondary">
          Your personal anime and manga tracking companion
        </Typography>
      </Box>

      <Paper elevation={3} sx={{ p: 4 }}>
        <Typography variant="h5" gutterBottom>
          Our Mission
        </Typography>
        <Typography paragraph>
          MangaSh1r0 aims to provide anime and manga enthusiasts with a seamless way to track, discover, 
          and enjoy their favorite content. Built with a passion for Japanese media and a love for technology, 
          our platform connects to the AniList API to bring you up-to-date information and personal tracking tools.
        </Typography>

        <Divider sx={{ my: 4 }} />

        <Typography variant="h5" gutterBottom>
          Features
        </Typography>
        <Typography paragraph>
          <strong>Anime & Manga Tracking:</strong> Keep track of what you've watched and read, including your progress and ratings.
        </Typography>
        <Typography paragraph>
          <strong>Search & Discover:</strong> Find new anime and manga based on your interests and what's popular.
        </Typography>
        <Typography paragraph>
          <strong>AniList Integration:</strong> Connect with your AniList account to sync your lists and data.
        </Typography>

        <Divider sx={{ my: 4 }} />

        <Typography variant="h5" gutterBottom>
          Technology Stack
        </Typography>
        <Typography paragraph>
          <strong>Frontend:</strong> Next.js with TypeScript and Material UI
        </Typography>
        <Typography paragraph>
          <strong>Backend:</strong> Django REST Framework
        </Typography>
        <Typography paragraph>
          <strong>API:</strong> AniList GraphQL API
        </Typography>

        <Divider sx={{ my: 4 }} />

        <Typography variant="h5" gutterBottom>
          Contact
        </Typography>
        <Typography>
          Have questions or suggestions? Reach out to us on GitHub or through the contact form.
        </Typography>
      </Paper>
    </Container>
  );
}
