from django.shortcuts import render, redirect

from trading.utils import populate_trades
# from .models import Account

from .utils import main, fetch_all_traders, get_trader, get_trader_by_email

def allTraders(request):
    # item = Account.objects.get(id=1)
    # print(item.email)
    main()
    
    context = {"traders": fetch_all_traders()}
    return render(request, 'trading/admin.html', context)


def getTrader(request, id):
    trader = get_trader(id)
    profit = trader[1]['profit']
    loss = trader[1]['loss']
    # for item in trader:
    #     print(item)
    #     print('x')
    #     # profit = item.profit
    #     # loss = item.loss
    context = {"trades": [profit, loss]}
    return render(request, 'trading/trader.html', context)

def get_trader_login(request):
    if request.method == 'POST':
        email = request.POST['login']
        trader = get_trader_by_email(email)
        if trader:
            id = trader[0]['_id']
            return redirect('getTrader', id=id)
        # else:
        #     return redirect('login')
    return render(request, 'trading/login.html')


