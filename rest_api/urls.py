from django.urls import include, path
from rest_framework import routers
from .views import WalletViewSet, TransactionViewSet

router = routers.DefaultRouter()
router.register(r'wallets', WalletViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = router.urls

