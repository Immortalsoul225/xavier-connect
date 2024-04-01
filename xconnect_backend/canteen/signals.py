from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from django.db.models import Q, Sum
from .models import Items, Cart, Menu


@receiver(post_save, sender=Items)
def update_cart_total(sender, instance, **kwargs):
    cart = Cart.objects.get(pk=instance.cart_id.pk)
    sum_total = Sum("price", filter=Q(cart_id=instance.cart_id.pk))
    total = Items.objects.aggregate(sum_total=sum_total)
    cart.total = total["sum_total"]
    cart.save()


@receiver(pre_delete, sender=Items)
def menu_update(sender, instance, **kwargs):
    item = Items.objects.get(pk=instance.pk)
    cart = Cart.objects.get(pk=instance.cart_id.pk)
    cart.total = 0
    cart.save()
    menu = Menu.objects.get(pk=item.menu_id.pk)
    menu.avail_quantity += item.quantity
    menu.save()
