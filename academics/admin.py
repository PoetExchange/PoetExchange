from academics.models import Book, AcademicClass, AcademicDepartment, Professor, AcademicClassProfile
from django.contrib import admin

class bookList(admin.ModelAdmin):
	#model = Book
	list_display = ('book_title','book_author','book_class','book_price','book_condition','additional_comments','entry_date')
	
class classList(admin.ModelAdmin):
	#model = AcademicClass
	list_display = ('class_dept','class_number','class_professor')


class deptList(admin.ModelAdmin):
	#model = AcademicDepartment
	list_display = ('dept_name','dept_abrv')

class profList(admin.ModelAdmin):
	#model = Professor
	list_display = ('first_name', 'last_name', 'department')

class profRateList(admin.ModelAdmin):
	#model = ProfRatingsTable
	list_display = ('rating_code', 'professor','user','rating','rating_code')

admin.site.register(Book,bookList)
admin.site.register(AcademicClass,classList)
admin.site.register(AcademicDepartment,deptList)
admin.site.register(Professor,profList)
admin.site.register(AcademicClassProfile)



