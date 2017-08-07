from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pos_app.models import Items, Receipts_Items
from pos_app.serializers import ItemsSerializer
import json

class ItemsList(APIView):

    def get(self, request):
        if request.user.is_authenticated():
            retrieve = request.GET.get('retrieve', '')
            items = Items.objects.all()
            if retrieve == 'msi':
                max, msi = 0, 0
                for item in items:
                    sum = 0
                    for i in Receipts_Items.objects.filter(item=item):
                        print(str(i.total_item_amount))
                        sum += i.total_item_amount
                        if sum > max:
                            max = sum
                            msi = i.item
                        else:
                            pass
                res_data = {}
                res_data['item'] = msi.name
                res_data['sold times'] = max
                return Response(str(res_data))

            elif retrieve == 'items':
                serializer = ItemsSerializer(items, many=True)
                return Response(serializer.data)
        else:
            return Response('authentication needed !')

    def post(self, request):
        if request.user.is_authenticated():
            code = request.POST.get('code', '')
            name = request.POST.get('name', '')
            price = request.POST.get('price', '')
            stock_amount = request.POST.get('stock_amount', '')

            try:
                item_obj = Items.objects.create(code=code, name=name, price=price, stock_amount=stock_amount)
                item_obj.save()
                return Response('add successfully', status=status.HTTP_201_CREATED)
            except:
                return Response('error')
        else:
            return Response('authentication needed !')

    def put(self, request):
        if request.user.is_authenticated():
            code = request.POST.get('code', '')
            stock_amount = request.POST.get('stock_amount', '')
            item_obj = Items.objects.filter(code=code)

            if not item_obj:
                return Response('no such item')
            else:
                try:
                    item_obj.update(stock_amount=stock_amount)
                    return Response('updated successfully', status=status.HTTP_201_CREATED)
                except:
                    return Response('error')
        else:
            return Response('authentication needed !')

    def delete(self, request):
        if request.user.is_authenticated():
            code = request.GET.get('code', '')
            item_obj = Items.objects.filter(code=code)

            if not item_obj:
                return Response('no such item')
            else:
                try:
                    item_obj.delete()
                    return Response('deleted successfully', status=status.HTTP_201_CREATED)
                except:
                    return Response('error')
        else:
            return Response('authentication needed !')
        
