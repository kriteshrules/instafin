from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .forms import PortfolioForm
from django.views.generic import ListView, DeleteView
from .models import Portfolio
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from stocks.stockquote import getQuotes
from django.db.models import Q
import json
from django.http import HttpResponse
from stocks.models import BSEStocks, NSEStocks

User = get_user_model()

class ChartsView(ListView):
    template_name = 'analytics/chartshome.html'
    model = Portfolio
    context_object_name = 'portfolio'

    def get(self, request):
        form = PortfolioForm()
        current_user = request.user

        symbol = current_user.portfolio_set.values_list('stock_name', flat=True)
        purchase_price = current_user.portfolio_set.values_list('purchase_price', flat=True)
        purchase_quantity = current_user.portfolio_set.values_list('purchase_quantity', flat=True)
        comment = current_user.portfolio_set.values_list('comment', flat=True)
        pk = current_user.portfolio_set.values_list('pk', flat=True)

        q = getQuotes(symbol)
        q.run()

        mylist = zip(symbol, q.stocknamelist, q.closepricelist, purchase_price, purchase_quantity, q.yearhighlist, q.yearlowlist, comment, pk)

        context = {
            'form': form,
            'title': 'Analytics',
            'mylist': mylist,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = PortfolioForm(request.POST)
        current_user = request.user

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            stock_name = form.cleaned_data['stock_name']
            purchase_price = form.cleaned_data['purchase_price']
            purchase_quantity = form.cleaned_data['purchase_quantity']
            comment = form.cleaned_data['comment']
            form = PortfolioForm()
            messages.success(request, f'The stock has been added to your portfolio!')

        symbol = current_user.portfolio_set.values_list('stock_name', flat=True)
        purchase_price = current_user.portfolio_set.values_list('purchase_price', flat=True)
        purchase_quantity = current_user.portfolio_set.values_list('purchase_quantity', flat=True)
        comment = current_user.portfolio_set.values_list('comment', flat=True)
        pk = current_user.portfolio_set.values_list('pk', flat=True)

        q = getQuotes(symbol)
        q.run()

        mylist = zip(symbol, q.stocknamelist, q.closepricelist, purchase_price, purchase_quantity, q.yearhighlist,
                     q.yearlowlist, comment, pk)

        args = {
            'form': form,
            'title': 'Analytics',
            'mylist': mylist,
            'stock_name': symbol,
            'purchase_price': purchase_price,
            'purchase_quantity': purchase_quantity,
            'comment': comment,
        }
        return render(request, self.template_name, args)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        defaultLabels = ["Feb", "March", "April", "May", "June", "July"]
        defaultData = [-0.7,2.2, -0.4, 1.5, 3.2, 1.3]
        sectors = ["Auto", "IT", "Pharma", "Banks", "Metals", "Energy", "Oil & Petro"]
        sectorsData = [15, 10, 8, 35, 15, 5, 12]
        holdings = ["HUL", "Infosys", "Vedanta", "HDFC Bank", "Maruti"]
        holdingsPercent = [28, 13, 12, 8, 7]
        stocklist = ["HUL", "Infosys", "Vedanta", "HDFC Bank", "Maruti", "HPCL", "Tata Steel"]
        positivesent = [0.7, 0.6, 0.9, 0.8, 0.5, 0.4, 0.7]
        negativesent = [0.3, 0.4, 0.1, 0.2, 0.5, 0.6, 0.3]

        data = {
            "defaultLabels": defaultLabels,
            "defaultData": defaultData,
            "sectors": sectors,
            "sectorsData": sectorsData,
            "holdings": holdings,
            "holdingsPercent": holdingsPercent,
            "stocklist": stocklist,
            "positivesent": positivesent,
            "negativesent": negativesent
        }
        return Response(data)

class DeleteView(SuccessMessageMixin, DeleteView):
    model = Portfolio
    success_url = '/analytics/'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        stock_name = self.object.stock_name
        request.session['stock_name'] = stock_name
        message = request.session['stock_name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)


def search(request,s):
    res = []
    try:
        q= NSEStocks.objects.filter( Q(Symbol__istartswith=s ) )
        for i in q:
            s=s.upper()
            Symbol=i.Symbol.capitalize()
            if( Symbol.startswith(s) ):
                res.append(Symbol)
        print(res)

    except Exception as e:
        print("Error",e)

    return HttpResponse(json.dumps({"res":res}),content_type="application/json")