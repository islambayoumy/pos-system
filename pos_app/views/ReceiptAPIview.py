from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pos_app.models import Items, Receipt
from pos_app.serializers import ReceiptsSerializer

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
            receipt_obj = Receipt.objects.filter(pk=id)

            if not receipt_obj:
                return Response('no such receipt')
            else:
                try:
                    receipt_obj.update(paid_amount=paid_amount)
                    return Response('updated successfully', status=status.HTTP_201_CREATED)
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
        
