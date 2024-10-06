from django.shortcuts import render, get_object_or_404
from .models import ToDoList, item
from .forms import CreateNewList
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request, id):
    # Fetches the id of a specific ToDoList
    ls = get_object_or_404(ToDoList, id=id)

    # Checks if the retrieved ToDoList belongs to the logged-in User
    if ls in request.user.todolist.all():
        if request.method == "POST":
            if request.POST.get("save"):  # Check for save action
                for item in ls.item_set.all():
                    if request.POST.get("c" + str(item.id)):
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif request.POST.get("newItem"):  # Check for adding a new item
                txt = request.POST.get("new")  # Get the new item text

                if txt and len(txt) > 2:  # Ensure the new item text is valid
                    ls.item_set.create(text=txt, complete=False)
                    print(f"Added new item: {txt}")  # Debugging output
                else:
                    print("Invalid item text, must be longer than 2 characters.")

        # Render the list.html template with the specific ToDoList
        return render(request, "main/list.html", {"ls": ls})

    # If the user doesn't own the ToDoList, render the view.html template
    return render(request, "main/view.html", {})


@login_required
def home(request):
    return render(request, "main/home.html")


@login_required
def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)      # fetches data from CreateNewList form defined in forms.py

        if form.is_valid():         # checks if the form is valid, the conditions for valid form is defined in forms.py
            n = form.cleaned_data["name"]       # Cleans the data, here specifically name
            t = ToDoList(name = n, user = request.user)     # Creates a to-do-llst using the name given by user
            t.save()

        return HttpResponseRedirect(f"/list/{t.id}/")     # Redirects the user to the detail view of the newly created to-do list

    else:
        form = CreateNewList()

    return render(request, "main/create.html", {"form" : form})


@login_required
def view(request):
    return render(request, "main/view.html", {})


@login_required
def delete_task(request, item_id):
    if request.method == 'POST':
        task = get_object_or_404(item, id=item_id)
        todo_list_id = task.todolist.id  # Get the associated ToDoList id before deletion
        task.delete()
        return redirect('index', id=todo_list_id)
    else:
        return redirect('index', id=todo_list_id)  # Redirect for non-POST requests


@login_required
def delete_list(request, id):
    todo_list = get_object_or_404(ToDoList, id=id)
    
    if request.method == 'POST':
        todo_list.delete()
        return redirect('view')