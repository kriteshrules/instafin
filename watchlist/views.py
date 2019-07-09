from django.shortcuts import render
from .forms import WatchlistForm
from django.views.generic import ListView, DeleteView
from .models import WatchList
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from stocks.stockquote import getQuotes


class StockListView(ListView):
    template_name = 'watchlist/watchlist.html'
    model = WatchList
    context_object_name = 'watchlist'

    def get(self, request):
        form = WatchlistForm()
        current_user = request.user

        # symbol = []
        # target_price = []
        # comment = []
        #
        # watchlist = current_user.watchlist_set.all()
        # for i in watchlist:
        #     sym = i.stock_name
        #     symbol.append(sym)
        #     target = i.target_price
        #     target_price.append(target)
        #     com = i.comment
        #     comment.append(com)

        symbol = current_user.watchlist_set.values_list('stock_name', flat=True)
        target_price = current_user.watchlist_set.values_list('target_price', flat=True)
        comment = current_user.watchlist_set.values_list('comment', flat=True)
        pk = current_user.watchlist_set.values_list('pk', flat=True)

        q = getQuotes(symbol)
        q.run()

        mylist = zip(symbol, q.stocknamelist, q.closepricelist, target_price, q.yearhighlist, q.yearlowlist, comment, pk)

        context = {
            'form': form,
            'title': 'Watchlist',
            'mylist': mylist,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = WatchlistForm(request.POST)
        current_user = request.user

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            stock_name = form.cleaned_data['stock_name']
            target_price = form.cleaned_data['target_price']
            comment = form.cleaned_data['comment']
            form = WatchlistForm()
            messages.success(request, f'The stock has been added to your watchlist!')

        symbol = current_user.watchlist_set.values_list('stock_name', flat=True)
        target_price = current_user.watchlist_set.values_list('target_price', flat=True)
        comment = current_user.watchlist_set.values_list('comment', flat=True)
        pk = current_user.watchlist_set.values_list('pk', flat=True)

        q = getQuotes(symbol)
        q.run()

        mylist = zip(symbol, q.stocknamelist, q.closepricelist, target_price, q.yearhighlist, q.yearlowlist, comment, pk)

        args = {
            'form': form,
            'title': 'Watchlist',
            'stock_name': stock_name,
            'target_price': target_price,
            'comment': comment,
            'mylist': mylist
        }
        return render(request, self.template_name, args)


class DeleteView(SuccessMessageMixin, DeleteView):
    model = WatchList
    success_url = '/watchlist/'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        stock_name = self.object.stock_name
        request.session['stock_name'] = stock_name
        message = request.session['stock_name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)













