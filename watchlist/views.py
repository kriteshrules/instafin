from django.shortcuts import render, redirect
from .forms import WatchlistForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import WatchList
from django.contrib import messages
from django.contrib.auth.models import User

#@login_required
class StockListView(ListView):
    template_name = 'watchlist/watchlist.html'
    model = WatchList
    context_object_name = 'watchlists'

    def get(self, request):
        form = WatchlistForm()
        #current_user = request.user
        #user_id = current_user.id
        context = {
            'form': form,
            'title': 'Watchlist',
            'watchlist': WatchList.objects.all()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = WatchlistForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            stock_name = form.cleaned_data['stock_name']
            target_price = form.cleaned_data['target_price']
            comment = form.cleaned_data['comment']
            form = WatchlistForm()
            messages.success(request, f'The stock has been added to your watchlist!')

        args = {
            'form': form,
            'title': 'Watchlist',
            'stock_name': stock_name,
            'target_price': target_price,
            'comment': comment
        }
        return render(request, self.template_name, args)











