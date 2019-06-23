from django.shortcuts import render
from .forms import WatchlistForm
from django.views.generic import ListView
from .models import WatchList
from django.contrib import messages

class StockListView(ListView):
    template_name = 'watchlist/watchlist.html'
    model = WatchList
    context_object_name = 'watchlists'

    def get(self, request):
        form = WatchlistForm()
        current_user = request.user
        context = {
            'form': form,
            'title': 'Watchlist',
            'watchlist': current_user.watchlist_set.all()
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











