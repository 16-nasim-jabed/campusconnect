from django import forms

from .models import Student


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "student_id", "department", "email")

    def clean_student_id(self):
        student_id = self.cleaned_data["student_id"]
        if (
            Student.objects.filter(student_id=student_id)
            .exclude(pk=self.instance.pk)
            .exists()
        ):
            raise forms.ValidationError("This student ID is already registered.")
        return student_id

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
