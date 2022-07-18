from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from Books.models import Book
from api.serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_Data(request):
    books = Book.objects.all()
    ser = BookSerializer(books,many = True)
    return Response(ser.data)

@api_view(['POST'])
def add_book(request):
    ser = BookSerializer(data = request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data , 200)
    return Response(403)

