from django.test import TestCase, override_settings
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Wallet, Transaction

class TransactionTestCase(TestCase):
    def setUp(self):
        wallet = Wallet.objects.create(label="Test Wallet")

class WalletTestCase(TestCase):
    def setUp(self):
        self.wallet = Wallet.objects.create(label="Test Wallet")
        self.n_of_txs = 10
        self.tx_amount = 100.00
        for i in range(self.n_of_txs):
            Transaction.objects.create(
                wallet=self.wallet,
                txid=f'txid_{i}',
                amount=self.tx_amount
            )

    def test_wallet_balance_is_sum_of_txs(self):
        self.assertEqual(self.wallet.balance, self.n_of_txs * self.tx_amount)


@override_settings(
    REST_FRAMEWORK={
        'DEFAULT_PAGINATION_CLASS': 'rest_framework_json_api.pagination.JsonApiPageNumberPagination',
        'PAGE_SIZE': 5
    }
)
class WalletViewSetTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(5):
            Wallet.objects.create(label=f'Wallet_{i}')

    def test_pagination(self):
        response = self.client.get(reverse('wallet-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)

    def test_sorting(self):
        response = self.client.get(reverse('wallet-list'), {'sort': '-label'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['label'], 'Wallet_4')

    def test_filtering(self):
        response = self.client.get(reverse('wallet-list'), {'label__icontains': 'Wallet_1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(wallet['label'] == 'Wallet_1' for wallet in response.data['results']))
