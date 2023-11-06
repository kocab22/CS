from csinterface.models import Company, Part, PriceBid
from django.db import connection
from pprint import pprint
import sys

def run():

    def is_venv():
        return (hasattr(sys, 'real_prefix') or
                (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))
    if is_venv():
        print('inside virtualenv or venv')
    else:
        print('outside virtualenv or venv')
    # bids = PriceBid.objects.all().values()
    # companies = Company.objects.all().values()
    # print(companies)
    # print(bids)


    # for company in companies:
    #     bid_count = PriceBid.objects.filter(company=company).count()

    #     print(company, '   nabidek celkem   ', bid_count)

# funguje!
    # price_bid = PriceBid.objects.first()
    # parts = price_bid.parts.all()
    # for part in parts:
    #     print(part.number)


# _____________________________________________________________________
    # def get_parts(number):
    #     try:

    #         price_bid = PriceBid.objects.get(number=number)
    #         parts = price_bid.parts.all()

    #         return list(parts)
    #     except PriceBid.DoesNotExist:
    #         return []
    
    # parts_list = get_parts('number')
    # for parts in parts_list:
    #     print(parts.number)

    # _____________________________________________________________________
# funguje
    # t = PriceBid.objects.get(number = 123)
    # parts = t.parts.all()
    # for part in parts:
    #     print(part.number)
    #     print(part.description)
    #     print(part.price)
