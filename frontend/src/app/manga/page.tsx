'use client';

import React from 'react';
import { Container, Typography, Box, TextField, Button, Card, CardMedia, CardContent } from '@mui/material';

export default function MangaPage() {
  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Box sx={{ mb: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom>
          Manga Search
        </Typography>
        <Typography variant="subtitle1" color="text.secondary" paragraph>
          Search for manga using the AniList API
        </Typography>
        
        <Box component="form" sx={{ mt: 3, display: 'flex', gap: 2 }}>
          <TextField 
            fullWidth
            label="Search manga..."
            variant="outlined"
          />
          <Button variant="contained" color="secondary" sx={{ px: 4 }}>
            Search
          </Button>
        </Box>
      </Box>
      
      <Box sx={{ mt: 4 }}>
        <Typography variant="h4" gutterBottom>
          Popular Manga
        </Typography>
        
        <Box sx={{ 
          display: 'grid', 
          gridTemplateColumns: {
            xs: '1fr',
            sm: 'repeat(2, 1fr)',
            md: 'repeat(3, 1fr)',
            lg: 'repeat(4, 1fr)'
          },
          gap: 3,
          mt: 2
        }}>
          {/* This would be populated from the API */}
          {[1, 2, 3, 4, 5, 6, 7, 8].map((item) => (
            <Card key={item} sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
              <CardMedia
                component="img"
                height="240"
                image={`https://picsum.photos/seed/${item + 100}/300/400`}
                alt="Placeholder manga image"
              />
              <CardContent sx={{ flexGrow: 1 }}>
                <Typography gutterBottom variant="h6" component="div">
                  Manga Title {item}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Short description about this manga series. This would come from the API.
                </Typography>
              </CardContent>
            </Card>
          ))}
        </Box>
      </Box>
    </Container>
  );
}
