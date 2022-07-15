from rest_framework import serializers
from Books.models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta :
        model = Book
        fields = '__all__'