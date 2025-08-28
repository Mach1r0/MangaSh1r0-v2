from django.shortcuts import render
from django.http import JsonResponse
from .anilist_auth import search_anime, search_manga

def anime_search_view(request):
    """
    View to search for anime using AniList API without authentication
    """
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    
    if not query:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'results': []})
        return render(request, 'anime/search.html')
    
    results = search_anime(query, page=page)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(results)
    
    return render(request, 'anime/search.html', {
        'results': results,
        'query': query,
        'page': page
    })

def manga_search_view(request):
    """
    View to search for manga using AniList API without authentication
    """
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    
    if not query:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'results': []})
        return render(request, 'manga/search.html')
    
    results = search_manga(query, page=page)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(results)
    
    return render(request, 'manga/search.html', {
        'results': results,
        'query': query,
        'page': page
    })
