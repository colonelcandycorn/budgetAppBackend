from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Category

def validate_decimal_greater_than_zero(value):
    if value <= 0:
        raise serializers.ValidationError("Amount must be greater than zero.")

unique_categories = UniqueValidator(queryset=Category.objects.all())