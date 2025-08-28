import json
import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

# These would be set in your Django settings.py
ANILIST_CLIENT_ID = getattr(settings, 'ANILIST_CLIENT_ID', '')
ANILIST_CLIENT_SECRET = getattr(settings, 'ANILIST_CLIENT_SECRET', '')
ANILIST_REDIRECT_URI = getattr(settings, 'ANILIST_REDIRECT_URI', '')

# AniList API endpoints
ANILIST_AUTH_URL = "https://anilist.co/api/v2/oauth/authorize"
ANILIST_TOKEN_URL = "https://anilist.co/api/v2/oauth/token"
ANILIST_API_URL = "https://graphql.anilist.co"

def get_auth_url():
    """
    Generate the AniList authorization URL
    """
    return f"{ANILIST_AUTH_URL}?client_id={ANILIST_CLIENT_ID}&redirect_uri={ANILIST_REDIRECT_URI}&response_type=code"

def exchange_code_for_token(code):
    """
    Exchange authorization code for an access token
    """
    payload = {
        "grant_type": "authorization_code",
        "client_id": ANILIST_CLIENT_ID,
        "client_secret": ANILIST_CLIENT_SECRET,
        "redirect_uri": ANILIST_REDIRECT_URI,
        "code": code
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    response = requests.post(
        ANILIST_TOKEN_URL,
        headers=headers,
        data=json.dumps(payload)
    )
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        return None

def get_user_info(access_token):
    """
    Get user information from AniList using the access token
    """
    query = """
    query {
        Viewer {
            id
            name
            avatar {
                large
            }
        }
    }
    """
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    
    response = requests.post(
        ANILIST_API_URL,
        headers=headers,
        json={"query": query}
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
        
def search_anime(search_query, page=1, per_page=10):
    """
    Search for anime using AniList GraphQL API without authentication
    This endpoint doesn't require OAuth2 or access tokens
    """
    query = """
    query ($search: String, $page: Int, $perPage: Int) {
        Page(page: $page, perPage: $perPage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
                perPage
            }
            media(search: $search, type: ANIME, sort: POPULARITY_DESC) {
                id
                title {
                    romaji
                    english
                    native
                }
                coverImage {
                    large
                }
                description
                episodes
                averageScore
                genres
                seasonYear
                format
                status
            }
        }
    }
    """
    
    variables = {
        "search": search_query,
        "page": page,
        "perPage": per_page
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    
    response = requests.post(
        ANILIST_API_URL,
        headers=headers,
        json={"query": query, "variables": variables}
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
        
def search_manga(search_query, page=1, per_page=10):
    """
    Search for manga using AniList GraphQL API without authentication
    This endpoint doesn't require OAuth2 or access tokens
    """
    query = """
    query ($search: String, $page: Int, $perPage: Int) {
        Page(page: $page, perPage: $perPage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
                perPage
            }
            media(search: $search, type: MANGA, sort: POPULARITY_DESC) {
                id
                title {
                    romaji
                    english
                    native
                }
                coverImage {
                    large
                }
                description
                chapters
                volumes
                averageScore
                genres
                startDate {
                    year
                }
                format
                status
            }
        }
    }
    """
    
    variables = {
        "search": search_query,
        "page": page,
        "perPage": per_page
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    
    response = requests.post(
        ANILIST_API_URL,
        headers=headers,
        json={"query": query, "variables": variables}
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
