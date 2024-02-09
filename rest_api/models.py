from django.db import models

class Wallet(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=200)

    @property
    def balance(self):
        return self.transactions.all().aggregate(models.Sum('amount'))['amount__sum'] or 0.00

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    wallet = models.ForeignKey(Wallet, related_name='transactions', on_delete=models.CASCADE)
    txid = models.CharField(max_length=200, unique=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
