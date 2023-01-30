from django.shortcuts import render
from django.http import JsonResponse
from .models import Note
from django.contrib.auth import authenticate, login, logout as logout_request
from django.contrib.auth.models import User
from django.middleware.csrf import get_token


def home(request):
    return JsonResponse({
        "user": request.user.username if request.user.is_authenticated else None
    })
    
def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})
    

def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    done = False
    if user is not None:
        login(request, user)
        done = True
    return JsonResponse({"done": done})

def logout(request):
    logout_request(request)

def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('password')
    user = User(username=username, password=password, email=email)
    user.save()
    login(request, user)
    return JsonResponse({
        "done": True
    })



def search_notes(request):
    query = request.POST.get('query')
    notes_from_title = Note.objects.filter(title__contains=query)
    notes_from_content = Note.objects.filter(content__contains=query)
    notes = set()
    for n in notes_from_title:
        notes.add(n)
    for n in notes_from_content:
        notes.add(n)
        
    data = {"notes":[]}
    
    for note in notes:
        data['notes'].append(note.json())
        
    return JsonResponse(data)
    
        
    
def notes(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(owner = request.user)
        data = {"notes":[]}
        for note in notes:
            data['notes'].append(note.json())
            
        return JsonResponse(data)
    return JsonResponse({})
    
def new_note(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    if request.user.is_authenticated:
        note = Note(title=title, content=content, owner=request.user)
        note.save()
    return JsonResponse({})
    
def update_note(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    content = request.POST.get('content')
    if request.user.is_authenticated:
        note = Note.objects.filter(id=id).first()
        if note is not None and note.owner == request.user:
            note.title = title
            note.content = content
            note.save()
    return JsonResponse({})
    
def delete_note(request):
    id = request.POST.get('id')
    if request.user.is_authenticated:
        note = Note.objects.filter(id=id).first()
        if note is not None and note.owner == request.user:
            note.delete()
    return JsonResponse({})
    

def get_note(request):
    id = request.POST.get('id')
    if request.user.is_authenticated:
        note = Note.objects.filter(id=id).first()
        if note is not None and note.owner == request.user:
            return JsonResponse(note.json())
    return JsonResponse({})

    
