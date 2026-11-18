from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentRegistrationForm
from .models import Student


def home(request):
    student = Student.objects.first()
    students = Student.objects.all()

    context = {
        "student_name": student.name,
        "university": "BAIUST",
        "department": student.department,
        "is_enrolled": True,
        "courses": [
            "Database Management System",
            "Computer Networks",
            "Software Engineering",
            "Cyber Security",
        ],
        "students": students,
    }

    return render(request, "core/home.html", context)


def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = StudentRegistrationForm()

    return render(request, "core/register.html", {"form": form})


def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentRegistrationForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = StudentRegistrationForm(instance=student)
    return render(
        request, "core/update_student.html", {"form": form, "student": student}
    )


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect("home")

    return render(request, "core/delete_student.html", {"student": student})
