from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import ListItem
from .forms import ListItemForm

def index(request):
    items = ListItem.objects.all()
    return render(request, 'listapp/index.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ListItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ListItemForm()
    return render(request, 'listapp/add_item.html', {'form': form})

def edit_item(request, item_id):
    item = get_object_or_404(ListItem, id=item_id)
    if request.method == 'POST':
        form = ListItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ListItemForm(instance=item)
    return render(request, 'listapp/edit_item.html', {'form': form})

def delete_item(request, item_id):
    item = get_object_or_404(ListItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'listapp/delete_item.html', {'item': item})

