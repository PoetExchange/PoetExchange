# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from academics.models import Book
from django.http import HttpResponse

def index(request):
	return render_to_response('objects/index.html')
