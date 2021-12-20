from django.contrib import admin
from .models import Payment, Cart, TransactionReport

admin.site.register(Payment)
admin.site.register(Cart)
admin.site.register(TransactionReport)