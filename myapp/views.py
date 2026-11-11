from django.shortcuts import get_object_or_404, redirect, render
from .forms import ItemForm
from .models import Item

# 1. READ: List all items
def item_list(request):
  items = Item.objects.all()
  return render(request, 'myapp/item_list.html', {'items': items})


# 2. CREATE: Add a new item
def item_create(request):
  if request.method == 'POST':
    form = ItemForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('item_list')
  else:
    form = ItemForm()
  return render(request, 'myapp/item_form.html', {'form': form})


# 3. UPDATE: Edit an existing item
def item_update(request, pk):
  item = get_object_or_404(Item, pk=pk)
  if request.method == 'POST':
    form = ItemForm(request.POST, instance=item)
    if form.is_valid():
      form.save()
      return redirect('item_list')
  else:
    form = ItemForm(instance=item)
  return render(request, 'myapp/item_form.html', {'form': form})


# 4. DELETE: Remove an item
def item_delete(request, pk):
  item = get_object_or_404(Item, pk=pk)
  if request.method == 'POST':
    item.delete()
    return redirect('item_list')
  return render(request, 'myapp/item_confirm_delete.html', {'item': item})