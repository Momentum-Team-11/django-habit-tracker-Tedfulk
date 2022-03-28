from datetime import datetime
from django.forms import DateField
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from habit.models import Habit, Result, User
from .forms import HabitForm, ResultForm
from django.contrib import messages


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, "habit/login.html")


@login_required
def home(request):
    habits = Habit.objects.all()
    return render(request, "habit/home.html", {"habits": habits})


def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    results = Result.objects.all().order_by('-update_date').filter(habit_record_id=habit.id)
    form = HabitForm()
    return render(request, "habit/habit_detail.html", {"habit": habit, "results": results, "form": form}
                  )


def result_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    results = Result.objects.order_by('-update_date').filter(daily_record__gt=habit.goal)
    total = Result.objects.filter(habit_record_id=habit.id).count()
    count = Result.objects.filter(daily_record__gt=habit.goal).count()
    form = HabitForm()
    return render(request, "habit/result_detail.html", {"habit": habit, "results": results, "form": form, "count": count, "total": total}
                  )


@login_required
def add_habit(request):
    user = get_object_or_404(User)
    if request.method == 'POST':
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user_id = user.id
            habit.save()
            return redirect("home")
    else:
        form = HabitForm()

        return render(request, "habit/add_habit.html", {'form': form})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='home')

    return render(request, "habit/edit_habit.html", {
        "form": form,
        "habit": habit
    })


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='home')
    return render(request, "habit/delete_habit.html", {"habit": habit})


@login_required
def add_result(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = ResultForm()
    else:
        form = ResultForm(data=request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.habit_record_id = habit.id
            result.save()
            # messages.success(request, "Result added!")
            return redirect(to='habit_detail', pk=habit.pk)

    return render(request, "habit/add_result.html", {"form": form, "habit": habit})


@login_required
def edit_result(request, pk):
    result = get_object_or_404(Result, pk=pk)
    if request.method == 'GET':
        form = ResultForm(instance=result)
    else:
        form = ResultForm(data=request.POST, instance=result)
        if form.is_valid():
            habit_pk = result.habit_record.pk
            form.save()
            return redirect(to='habit_detail', pk=habit_pk)

    return render(request, "habit/edit_result.html", {
        "form": form,
        "result": result
    })


@login_required
def delete_result(request, result_pk):
    result = get_object_or_404(Result, pk=result_pk)
    if request.method == 'POST':
        habit_pk = result.habit_record.pk
        result.delete()
        return redirect(to='habit_detail', pk=habit_pk)
    return render(request, "habit/delete_result.html", {"result": result})


# my message not working in add_result??
# TODO update result to habit (post and save to database)
# TODO annotate() could help me get the number or of boolean values for results completed. 
# TODO display the days that the goal was met.  
# if habit isn't done that day then turn habit red or gray
# - Users should be able to create new habits and track those habits with trackers, or daily records (what you call it is up to you).
# - Each habit should have a name and a target or goal. What is this "target"? Each habit should have a daily number of some action you want to do. Some examples:
#     - I want to walk 1000 steps daily
#     - I want to write 100 lines of code daily
#     - I want to talk to 2 new people each day
#     - I want to read 200 pages daily
#     - I want to sleep 8 hours daily
# - Once you have habits, you should be able to make a daily record of your activity on each habit. That record should contain a date and a number for that date.
# - A user can only have **one record per day per habit**. You will need to use the [`constraints` option for models](https://docs.djangoproject.com/en/4.0/ref/models/constraints/) with `UniqueConstraint` to make the habit records unique by user, habit, and day.
# - Optimally, users can edit/update records and add records for previous days.
# - The URL for creating and updating a record should be the same and should use the habit primary key, year, month, and day in the URL. For example: `habit/1/2021/6/18`
#     - We want to do this so that we can have a single url that will work for a new record and will also allow changing an existing one.
#     - You'll want to look into the [`get_or_create()` method](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.get_or_create) for this.
#     - You can put the form for creating and updating on this page or elsewhere, as your user interface dictates.

# - On the detail page for a habit, you should be able to see all the records for that habit in an HTML table. Show the user whether they met their goal for that day visually somehow -- maybe via colors. Think about accessibility here -- how would a user that can't see know whether they met their goal each day? javascript??
# - Make your interface as easy to use as possible. Think about what makes the most sense to enter and review data quickly. Consider using a calendar to show records.
