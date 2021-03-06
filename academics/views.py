# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from academics.models import *
from django.http import HttpResponse
from django.template import RequestContext
from objects.functions import whoAmI

def bookIndex(request):
	book_list = Book.objects.all().order_by('entry_date')
	return render_to_response('academics/books.html',{'book_list':book_list})

def deptDetail(request, slug) :
	d = get_object_or_404(AcademicDepartment, dept_abrv = slug)
	c = d.academicclass_set.all().order_by('class_number')
	b = d.book_set.all().order_by('-entry_date')
	context = {
				'classes':c,
				'dept':d,
				'books':b,
			}
	return render_to_response(
							'production/base_deptDetail.html', 
							context, 
							context_instance=RequestContext(request)
						)

def classDetail(request, deptSlug, classSlug) :
	c = get_object_or_404(AcademicClass, ac_slug=classSlug)
	b = c.book_set.all().order_by('-entry_date')
	dept_courses = c.class_dept.academicclass_set.all().order_by('class_number')
	context = {
			'class':c,
			'books':b,
			'dept':c.class_dept,
			'dept_courses':dept_courses,
			}
	if c.class_professor :
		prof_courses = c.class_professor.academicclass_set.all().order_by('class_number')
		context['prof_courses']=prof_courses
	return render_to_response(
			'production/base_classDetail.html', 
			context, 
			context_instance=RequestContext(request),
			)

def bookDetail(request, deptSlug, classSlug, bookSlug) :
	b = get_object_or_404(Book, book_slug = bookSlug)
	context = {
			'dept':b.book_dept,
			'class':b.book_class,
			'book':b
			}
	return render_to_response(
			'production/base_bookDetail.html', 
			context,
			context_instance = RequestContext(request),
			)
