from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .forms import ItemForm
from barcode.writer import ImageWriter
from .models import Item
import barcode
import os,sys
# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        post = Item.objects.all()
        context = {
            'post': post,
        }
        return render(request, 'post_list.html', context)

class ItemCreateView(View):
    form_class = ItemForm
    initial = {'key': 'value'}
    template_name = 'item-create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            bcode = post.number
            ean = barcode.get('Code39', bcode, writer=ImageWriter())
            filename = ean.save('live-static/media-root/'+bcode)
            post.barcode = bcode + '.png'
            quantity = post.quantity
            unit_cost = post.unit_cost
            total_value = quantity * unit_cost
            post.total = total_value
            post.save()
            # return redirect('blog:post-detail', pk=post.pk)
        else:
            form = ItemForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)