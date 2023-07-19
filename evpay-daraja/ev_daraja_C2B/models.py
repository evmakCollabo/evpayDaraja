from django.db import models

class User(models.Model):
    email = models.CharField(max_length=128, null=False)
    password = models.CharField(max_length=128, null=False)
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    mobile_number = models.CharField(max_length=20, null=True, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.mobile_number} - {self.email}"

class TransactionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.CharField(max_length=20)
    trans_ref = models.CharField(max_length=20, primary_key=True)
    amount = models.IntegerField()
    source_from = models.CharField(max_length=50)
    pay_end = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=14)
    codex = models.CharField(max_length=50)
    custom_reference = models.CharField(max_length=50, null=True, blank=True)
    callback_url = models.CharField(max_length=100, null=True, blank=True)
    callback_response = models.CharField(max_length=100, null=True, blank=True)
    product = models.CharField(max_length=50, null=True, blank=True)
    value1 = models.CharField(max_length=250, null=True, blank=True)
    mno_ref = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction: {self.trans_ref} - User: {self.user.first_name} - Amount: {self.amount}"
