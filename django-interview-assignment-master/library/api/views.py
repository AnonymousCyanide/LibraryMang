from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def get_Data(request):
    book = {
        'id' : 'xyz',
        'title': 'abc',
        'status' : 'Borrowed',
        'Return_Date' : 'yyyy-mm-dd'
    }
    return Response(book)
