from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import StudySchedule
from .forms import StudyScheduleForm


@login_required
def home(request):
    schedules = StudySchedule.objects.filter(
        user=request.user
    ).order_by('date', 'start_time')

    return render(request, 'scheduler/home.html', {
        'schedules': schedules,
    })


@login_required
def schedule_create(request):
    if request.method == 'POST':
        form = StudyScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user
            schedule.save()
            messages.success(request, 'Study session added.')
            return redirect('home')
    else:
        form = StudyScheduleForm()

    return render(request, 'scheduler/schedule_form.html', {
        'form': form,
        'title': 'Add Study Session',
    })


@login_required
def schedule_update(request, pk):
    schedule = get_object_or_404(StudySchedule, pk=pk, user=request.user)

    if request.method == 'POST':
        form = StudyScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Study session updated.')
            return redirect('home')
    else:
        form = StudyScheduleForm(instance=schedule)

    return render(request, 'scheduler/schedule_form.html', {
        'form': form,
        'title': 'Edit Study Session',
    })


@login_required
def schedule_delete(request, pk):
    schedule = get_object_or_404(StudySchedule, pk=pk, user=request.user)

    if request.method == 'POST':
        schedule.delete()
        messages.success(request, 'Study session deleted.')
        return redirect('home')

    return render(request, 'scheduler/schedule_confirm_delete.html', {
        'schedule': schedule,
    })


@login_required
def schedule_toggle_status(request, pk):
    schedule = get_object_or_404(StudySchedule, pk=pk, user=request.user)

    if request.method == 'POST':
        schedule.status = 'completed' if schedule.status == 'pending' else 'pending'
        schedule.save()

    return redirect('home')