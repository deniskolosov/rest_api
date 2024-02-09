from rest_framework import viewsets
from .serializers import WalletSerializer, TransactionSerializer
from .models import Wallet, Transaction
from rest_framework_json_api import django_filters
from rest_framework_json_api import filters


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all().order_by('id')
    serializer_class = WalletSerializer
    filter_backends = [django_filters.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
       'label': ('icontains',),
   }

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('id')
    serializer_class = TransactionSerializer
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_fields = ['wallet', 'txid', 'amount']
