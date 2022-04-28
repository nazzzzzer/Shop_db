
from .models.mod import Category,Product
from .models.users import User
from django.contrib import admin
from .models.orders import Order, OrderItem


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)



