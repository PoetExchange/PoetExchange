# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from academics.models import *
from django.http import HttpResponse
from django.template import RequestContext
from objects.functions import whoAmI

def bookIndex(request):
	book_list = Book.objects.all().order_by('entry_date')
	return render_to_response('academics/books.html',{'book_list':book_list})

	#book_list = Book.objects.all().order_by('entry_date')
	#output = ', '.join([p.book_title for p in book_list])
	#return HttpResponse(output)

def bookDetail(request,book_id):
	b = get_object_or_404(Book, pk = book_id)
	return render_to_response('academics/detail.html',{'book':b})

def deptDetail(request, slug) :
	uagent = whoAmI(request.META['HTTP_USER_AGENT'])
	d = get_object_or_404(AcademicDepartment, dept_abrv = slug)
	c = d.academicclass_set.all().order_by('class_number')
	context = {
				'classes':c,
				'dept':d,
				'uagent':uagent,
			}
	return render_to_response(
							'production/base_dept-detail.html', 
							context, 
							context_instance=RequestContext(request)
						)
