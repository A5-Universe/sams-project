from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    return render(request, 'login.html')

def add_student(request):
    return render(request, 'add-student.html')

def delete_student(request):
    return render(request, 'delete-student.html')

def edit_attendance(request):
    return render(request, 'edit-attendance.html')

def mark_attendance(request):
    return render(request, 'mark-attendance.html')

def view_attendance(request):
    return render(request, 'view-attendance.html')
