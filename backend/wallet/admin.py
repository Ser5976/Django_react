from django.contrib import admin

from wallet.models import Wallet, Currency


class WalletInline(admin.TabularInline):
    model = Wallet


class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'balance', 'currency')
    list_display_links = ('owner', 'balance',)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol' 'name', 'bid_usd', 'is_crypto', 'is_active')
    list_display = ('symbol', 'name',)


admin.site.register(Wallet, WalletAdmin)
admin.site.register(Currency, CurrencyAdmin)