from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pos_app.models import Items
from pos_app.serializers import ItemsSerializer


class ItemsList(APIView):

    def get(self, request):
        if request.user.is_authenticated():
            #userId = request.GET.get('userId')
            items = Items.objects.all()
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
            code = request.POST.get('code', '')
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
        
