from django.contrib import admin
from .models import SubscriptionType, Membership

# Register your models here.


class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'price',
        'rating',
    )

    oredring = ('id')


admin.site.register(SubscriptionType, SubscriptionTypeAdmin)
admin.site.register(Membership, MembershipAdmin)
