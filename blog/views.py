from django.shortcuts import render
from .forms import StudentForm

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'blog/results.html', {'data': data})
    else:
        form = StudentForm()
    
    return render(request, 'blog/form.html', {'form': form})