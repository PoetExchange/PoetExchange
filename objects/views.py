# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from academics.models import *
from django.http import HttpResponse
from django.template import RequestContext
from users.forms import LoginForm

def index(request):
	acDepts = AcademicDepartment.objects.all().order_by('dept_abrv')
	deptBooks = {}
	for dept in acDepts :
		deptBooks[dept.dept_abrv] = Book.objects.filter(book_dept=dept).order_by('-entry_date')[:5]
	context = {
			'logForm':LoginForm(),
			'acDepts':acDepts,
			'books' : deptBooks,
		}
	return render_to_response(
			'production/base_index.html',
			context,
			context_instance=RequestContext(request)
		)
		
def department(request, dept_abrv) :
	pass
