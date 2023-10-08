from django.shortcuts import render

from trading.utils import populate_trades
# from .models import Account

from .utils import main, fetch_all_traders, get_trader, generate_time

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

