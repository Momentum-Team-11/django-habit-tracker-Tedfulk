from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from habit.models import Habit


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, "habit/login.html")


@login_required
def home(request):  # this will include our list of the decks. Kind of like list_books or list_albums in other projects
    habits = Habit.objects.all()
    return render(request, "habit/home.html", {"habits": habits})


@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(data=request.POST)
        if form.is_valid():
            user = form.save()

            return redirect("home")
    else:
        form = HabitForm()

        return render(request, "habit/add_habit.html", {'form': form})
# TODO All habits_list
# TODO Add, edit, delete habits from main page and from habits_list
# TODO update habit (post and save to database)
# TODO Nice to have sort habits
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