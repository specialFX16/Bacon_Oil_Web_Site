from django.shortcuts import render

# Import http functionality
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import render_to_string

# Import models
from django.db import models
from django.contrib.auth.models import User
from webapp.models import *

# Import helper functions
from django.contrib.auth import authenticate as auth_func
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django import forms

def home(request):
    """
    Default controller for handling requests to /
    This method only serves the index.html file.
    """
    return render_to_response('index.html', {}, RequestContext(request))

def about(request):
    """
    Controler for handeling the about page
    """

    return render_to_response('about.html', {}, RequestContext(request))

def contact(request):
    """
    Controler for handleing the contact page
    """

    return render_to_response('contact.html', {}, RequestContext(request))
