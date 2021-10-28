from restaurant_sys.models import *

def create_bill(dict):
    bill=bill_order(cus_phone=dict['cus_phone'],finish=False)
    bill.save()
    for d in dict.keys():
        if d !='csrfmiddlewaretoken' and d!="cus_phone" and d!="restname":
            b_i=bill_item(item_name=dish.objects.get(name=d),amount=dict[d])
            b_i.save()
            bill.bill_item.add(b_i)
    bill.save()#for updating the bill