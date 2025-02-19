from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import Cow, MilkRecord
from .forms import CowForm, MilkRecordForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

@login_required
def cow_list(request):
  cows = Cow.objects.filter(is_deleted=False)
  return render(request, 'cows/cow_list.html', {'cows': cows})

@login_required
def cow_detail(request, pk):
    cow = get_object_or_404(Cow, pk=pk)
    milk_records = MilkRecord.objects.filter(cow=cow).order_by('-date')
    return render(request, 'cows/cow_detail.html', {'cow': cow, 'milk_records': milk_records})

@login_required
def cow_new(request):
    if request.method == "POST":
        form = CowForm(request.POST)
        if form.is_valid():
            cow = form.save()
            return redirect('cow_detail', pk=cow.pk)
    else:
        form = CowForm()
    return render(request, 'cows/cow_edit.html', {'form': form})

@login_required
def cow_edit(request, pk):
    cow = get_object_or_404(Cow, pk=pk)
    if request.method == "POST":
        form = CowForm(request.POST, instance=cow)
        if form.is_valid():
            cow = form.save()
            return redirect('cow_detail', pk=cow.pk)
    else:
        form = CowForm(instance=cow)
    return render(request, 'cows/cow_edit.html', {'form': form})

@login_required
def deleted_cows(request):
    deleted_cows = Cow.objects.filter(is_deleted=True)
    return render(request, 'cows/deleted_cow_list.html', {'deleted_cows': deleted_cows})


@login_required
def cow_delete(request, pk):
    cow = get_object_or_404(Cow, pk=pk)
    if request.method == 'POST':
        reason = request.POST.get('reason')
        if reason:
            cow.is_deleted = True
            cow.deletion_reason = reason
            cow.save()
            return redirect('cow_list')
        else:
            return HttpResponse("A reason for deletion is required.", status=400)
    return render(request, 'cows/cow_confirm_delete.html', {'cow': cow})

@login_required
def add_milk_record(request, cow_id):
    cow = get_object_or_404(Cow, pk=cow_id)
    if request.method == "POST":
        form = MilkRecordForm(request.POST)
        if form.is_valid():
            milk_record = form.save(commit=False)
            milk_record.cow = cow
            milk_record.save()
            return redirect('cow_detail', pk=cow.pk)
    else:
        form = MilkRecordForm()
    return render(request, 'cows/add_milk_record.html', {'form': form, 'cow': cow})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('cow_list')
    else:
        form = UserCreationForm()
    return render(request, 'cows/register.html', {'form': form})


