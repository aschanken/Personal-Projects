# Create your views here.
from forum.models import Forums
from forum.models import forum_top_level_display, forum_model_display, forum_post_display
from django.shortcuts import render, redirect

def root(request):
    return render(request, 'index.html', forum_top_level_display())

def forum_display(request, get_forum):
    return render(request, 'forum_display.html', forum_model_display(get_forum))

def thread_display(request, get_thread):
    return render(request, 'thread_display.html', forum_post_display(get_thread))