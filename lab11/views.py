from django.http import HttpResponse
from django.shortcuts import render
from lab11.models import Course, Student

def course_search_ajax(request):
    if request.method == "POST":
        cid = request.POST.get("cname")
        students = Student.objects.all()
        student_list = []

        for student in students:
            if student.enrolment.filter(id=cid).exists():
                student_list.append(student)

        if len(student_list) == 0:
            return HttpResponse("<h1>No Students enrolled</h1>")
        
        return render(request, "selected_students.html", {"student_list": student_list})

    else:
        courses = Course.objects.all()
        return render(request, "course_search_aj.html", {"courses": courses})
