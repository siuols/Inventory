from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .forms import ItemCodeForm
from barcode.writer import ImageWriter
import barcode
from .models import ItemCode
import os,sys
# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        post = ItemCode.objects.all()
        context = {
            'post': post,
        }
        return render(request, 'post_list.html', context)

class ItemCreateView(View):
    form_class = ItemCodeForm
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
            post.save()
            # return redirect('blog:post-detail', pk=post.pk)
        else:
            form = ItemCodeForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)