from rest_framework import serializers
from django.db.models import Sum
from .models import Category, Expenditure, Income
from .validators import validate_decimal_greater_than_zero, unique_categories


class CategorySerializer(serializers.ModelSerializer):
    budgeted = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[validate_decimal_greater_than_zero])
    name = serializers.CharField(max_length=100, validators=[unique_categories])
    total = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "budgeted",
            "path",
            "total",
        ]

    def get_total(self, obj):
        user = obj.user
        total = obj.expenses.filter(user=user).aggregate(Sum("amount"))["amount__sum"]
        return total if total else 0

class ExpenditureSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[validate_decimal_greater_than_zero])
    class Meta:
        model = Expenditure
        fields = [
            "id",
            "name",
            "category",
            "description",
            "amount",
            "date_of_expense",
        ]
        read_only_fields = [
            "user",
        ]
class IncomeSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[validate_decimal_greater_than_zero])

    class Meta:
        model = Income
        fields = [
            "id",
            "name",
            "user",
            "description",
            "amount",
            "date_of_income",
        ]