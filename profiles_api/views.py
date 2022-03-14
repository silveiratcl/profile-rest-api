from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Returns a list od APIView features"""
        an_apiview = [
                      'Uses HTTP methods as function (get, post, patch, put, delete)',
                      'Is similar to a traditional Django View',
                      'Gives you the most control over you applications logic',
                      'Is mapped manually ti URLs',
        ]
        
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
        
        