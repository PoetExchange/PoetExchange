# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from academics.models import Book
from django.http import HttpResponse

def bookIndex(request):
	book_list = Book.objects.all().order_by('entry_date')
	return render_to_response('academics/books.html',{'book_list':book_list})

	#book_list = Book.objects.all().order_by('entry_date')
	#output = ', '.join([p.book_title for p in book_list])
	#return HttpResponse(output)

def detail(request,book_id):
	b = get_object_or_404(Book, pk = book_id)
	return render_to_response('academics/detail.html',{'book':b})
