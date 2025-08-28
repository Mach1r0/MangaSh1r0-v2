# MangaSh1r0-v2

A manga and anime tracking application built with Django and AniList API integration.

## Project Structure

- `/backend` - Django backend with AniList API integration
- `/frontend` - (Future) Frontend application

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Features

- AniList API Integration
- Anime/Manga search
- User authentication via AniList OAuth
- Track your anime and manga progress
