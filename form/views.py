from django.shortcuts import redirect, render

from .forms import StudentForm


def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("https://joinmyquiz.com")
    else:
        form = StudentForm()

    return render(request, "form.html", {"form": form})
