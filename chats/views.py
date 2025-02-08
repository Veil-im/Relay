from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CreateChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"message": "Chat created"})


