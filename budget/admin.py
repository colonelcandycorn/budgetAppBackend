from django.contrib import admin

# Register your models here.
from .models import Expenditure, Category, Income

admin.site.register(Expenditure)
admin.site.register(Category)
admin.site.register(Income)
