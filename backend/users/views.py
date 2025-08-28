from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from .anilist_auth import get_auth_url, exchange_code_for_token, get_user_info

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

def login_with_anilist(request):
    """
    Redirect user to AniList for authorization
    """
    auth_url = get_auth_url()
    return HttpResponseRedirect(auth_url)

@require_http_methods(["GET"])
def anilist_callback(request):
    """
    Handle the callback from AniList after user authorization
    """
    code = request.GET.get('code')
    
    if not code:
        return JsonResponse({"error": "Authorization code not provided"}, status=400)
    
    # Exchange the code for an access token
    access_token = exchange_code_for_token(code)
    
    if not access_token:
        return JsonResponse({"error": "Failed to obtain access token"}, status=400)
    
    # Get user info from AniList
    user_info = get_user_info(access_token)
    
    if not user_info or 'data' not in user_info:
        return JsonResponse({"error": "Failed to get user information"}, status=400)
    
    anilist_user = user_info['data']['Viewer']
    anilist_id = str(anilist_user['id'])
    username = anilist_user['name']
    
    # Check if user already exists
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # Create a new user
        user = User.objects.create(
            username=username,
            name=username,
            email=f"{username}@anilist.temp"  # Placeholder email
        )
        user.set_unusable_password()  # User will authenticate through AniList
        user.save()
    
    # Log the user in
    login(request, user)
    
    # Store access token in session
    request.session['anilist_token'] = access_token
    
    # Redirect to profile page or homepage
    return HttpResponseRedirect(reverse('home'))

def profile(request):
    """
    User profile page
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
        
    return render(request, 'users/profile.html', {'user': request.user})