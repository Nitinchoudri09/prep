from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resume, ResumeTemplate

@login_required
def dashboard(request):
    resumes = request.user.resumes.all().order_by('-updated_at')
    # Use categories requested by the user
    templates = ResumeTemplate.objects.all()
    
    context = {
        'resumes': resumes,
        'templates': templates,
    }
    return render(request, 'resume_builder/dashboard.html', context)

@login_required
def builder(request, resume_id=None):
    if resume_id:
        resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    else:
        # Create a blank resume if creating new
        resume = Resume.objects.create(user=request.user)
        return redirect('resume_builder:builder', resume_id=resume.id)
        
    context = {
        'resume': resume,
        'templates': ResumeTemplate.objects.all()
    }
    return render(request, 'resume_builder/builder.html', context)

@login_required
def delete_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    if request.method == 'POST':
        resume.delete()
    return redirect('resume_builder:dashboard')
