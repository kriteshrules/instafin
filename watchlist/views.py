from django.shortcuts import render
from .forms import WatchlistForm
from django.views.generic import ListView, DeleteView
from .models import WatchList
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
import json
from stocks.models import BSEStocks
from django.db.models import Q


class StockListView(ListView):
    template_name = 'watchlist/watchlist.html'
    model = WatchList
    context_object_name = 'watchlist'

    def get(self, request):
        form = WatchlistForm()
        current_user = request.user
        context = {
            'form': form,
            'title': 'Watchlist',
            'watchlist': current_user.watchlist_set.all(),
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
            'comment': comment,
            'watchlist': request.user.watchlist_set.all()
        }
        return render(request, self.template_name, args)


class DeleteView(SuccessMessageMixin, DeleteView):
    model = WatchList
    success_url = '/watchlist/'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        stock_name = self.object.stock_name
        request.session['stock_name'] = stock_name  # name will be change according to your need
        message = request.session['stock_name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)


def search(request, s):
    res = []
    print("in search", s)
    try:
        q = BSEStocks.objects.filter(Q(Symbol__istartswith=s) | Q(CompanyName__istartswith=s))
        for i in q:
            s = s.upper()
            CompanyName = i.CompanyName.capitalize()
            Symbol = i.Symbol.capitalize()
            if (CompanyName.startswith(s)):
                res.append(CompanyName)
            if (Symbol.startswith(s)):
                res.append(Symbol)
        print(res)

    except Exception as e:
        print("Error", e)

    return HttpResponse(json.dumps({"res": res}), content_type="application/json")













