from rest_framework import serializers
from Books.models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta :
        model = Book
        fields = '__all__'

class BorrowedSerializer(serializers.ModelSerializer):
    class Meta :
        model = Borrowed
        fields = '__all__'