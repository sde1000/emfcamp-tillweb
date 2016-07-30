from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings

from quicktill.models import *

from sqlalchemy import distinct

def frontpage(request):
    s = settings.TILLWEB_DATABASE()
    pub = settings.TILLWEB_PUBNAME
    lines = s.query(StockLine)\
             .order_by(StockLine.name)\
             .all()

    stock = s.query(StockType)\
            .filter(StockType.remaining > 0)\
            .order_by(StockType.dept_id)\
            .order_by(StockType.manufacturer)\
            .order_by(StockType.name)\
            .all()
            
    return render(request, "whatson.html",
                  {"pubname": pub,
                   "lines": [
                       (l.name, l.sale_stocktype.format(),
                        l.sale_stocktype.pricestr)
                       for l in lines
                       if l.stockonsale or l.linetype == 'continuous'],
                   "stock": [(s.format(), s.remaining, s.unit.name)
                             for s in stock],
                  })

def locations(request):
    s = settings.TILLWEB_DATABASE()
    locations = [x[0] for x in s.query(distinct(StockLine.location))
                 .order_by(StockLine.location).all()]
    return JsonResponse({'locations': locations})

def location(request, location):
    s = settings.TILLWEB_DATABASE()
    lines = s.query(StockLine)\
             .filter(StockLine.location == location)\
             .order_by(StockLine.name)\
             .all()

    return JsonResponse({'location': [
        {"line": l.name,
         "description": l.sale_stocktype.format(),
         "price": l.sale_stocktype.saleprice,
         "price_for_units": l.sale_stocktype.saleprice_units,
         "unit": l.sale_stocktype.unit.name}
        for l in lines if l.stockonsale or l.linetype == "continuous"]})

def stock(request):
    s = settings.TILLWEB_DATABASE()
    stock = s.query(StockType)\
             .filter(StockType.remaining > 0)\
             .order_by(StockType.dept_id)\
             .order_by(StockType.manufacturer)\
             .order_by(StockType.name)\
             .all()
    return JsonResponse({'stock': [{
        'description': s.format(),
        'remaining': s.remaining,
        'unit': s.unit.name
        } for s in stock]})
