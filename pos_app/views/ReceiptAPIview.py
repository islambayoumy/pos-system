from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pos_app.models import Items, Receipt, Receipts_Items
from pos_app.serializers import ReceiptsSerializer, ReceiptsItemsSerializer

class ReceiptList(APIView):

    def get(self, request):
        if request.user.is_authenticated():
            receipts = Receipt.objects.all()
            serializer = ReceiptsSerializer(receipts, many=True)
            return Response(serializer.data)
        else:
            return Response('authentication needed !')

    def post(self, request):
        if request.user.is_authenticated():
            try:
                receipt_obj = Receipt.objects.create()
                receipt_obj.save()
                response_str = 'add successfully | receipt_id = ' + str(receipt_obj.pk)
                return Response(response_str, status=status.HTTP_201_CREATED)
            except:
                return Response('error')
        else:
            return Response('authentication needed !')

    def put(self, request):
        if request.user.is_authenticated():
            id = request.POST.get('receipt_id', '')
            paid_amount = request.POST.get('paid_amount', '')
            receipt_obj = Receipt.objects.get(pk=id)

            if not receipt_obj:
                return Response('no such receipt')
            else:
                try:
                    if float(paid_amount) == receipt_obj.paid_amount:
                        print(receipt_obj)
                        Receipt.objects.filter(pk=id).update(is_paid=True)
                        return Response('receipt paid successfully', status=status.HTTP_201_CREATED)
                    else:
                        return Response('Payment amount needs to be the same as receipt total amount')
                except:
                    return Response('error')
        else:
            return Response('authentication needed !')

    def delete(self, request):
        if request.user.is_authenticated():
            id = request.GET.get('id', '')
            receipt_obj = Receipt.objects.filter(pk=id)

            if not receipt_obj:
                return Response('no such receipt')
            else:
                try:
                    receipt_obj.delete()
                    return Response('deleted successfully', status=status.HTTP_201_CREATED)
                except:
                    return Response('error')
        else:
            return Response('authentication needed !')
        

class ReceiptsItemsList(APIView):

    def get(self, request):
        if request.user.is_authenticated():
            id = request.GET.get('receipt_id', '')
            receipts_items = Receipts_Items.objects.filter(receipt=id)
            serializer = ReceiptsItemsSerializer(receipts_items, many=True)
            return Response(serializer.data)
        else:
            return Response('authentication needed !')

    def post(self, request):
        if request.user.is_authenticated():
            receipt = request.POST.get('receipt_id', '')
            item = request.POST.get('item_id', '')
            item_amount = request.POST.get('item_amount', '')

            receipts = Receipt.objects.get(pk=receipt)
            items = Items.objects.get(pk=item)
            if int(item_amount) > items.stock_amount:
                return Response('item amount must be less than stock amount')
            else:
                paid_amount_per_item = float(item_amount) * items.price
                try:
                    receipts_items_obj = Receipts_Items.objects.create(receipt=receipts, item=items, total_item_amount=item_amount, paid_amount_per_item=paid_amount_per_item)
                    receipts_items_obj.save()
                    
                    # updating item stock amount
                    try:
                        new_stock_amount = items.stock_amount - float(item_amount)
                        Items.objects.filter(pk=item).update(stock_amount=new_stock_amount)
                        
                        # updating item total receipt payment
                        try:
                            receipts_items = Receipts_Items.objects.filter(receipt=receipt)
                            sum = 0.0
                            for i in receipts_items:
                                sum += i.paid_amount_per_item
                            Receipt.objects.filter(pk=receipt).update(paid_amount=sum)
                            return Response('add successfully', status=status.HTTP_201_CREATED)
                        except:
                            return Response('error updating receipt paid amount')

                    except:
                        return Response('error updating stock amount')
                        
                except:
                    return Response('error')
        else:
            return Response('authentication needed !')

    def delete(self, request):
        if request.user.is_authenticated():
            receipt_id = request.GET.get('receipt_id', '')
            item_id = request.GET.get('item_id', '')
            receipt_item_obj = Receipts_Items.objects.filter(receipt=receipt_id,item=item_id)

            if not receipt_item_obj:
                return Response('no such receipt item')
            else:
                try:
                    receipt_item_obj.delete()
                    return Response('deleted successfully', status=status.HTTP_201_CREATED)
                except:
                    return Response('error')
        else:
            return Response('authentication needed !')
        
