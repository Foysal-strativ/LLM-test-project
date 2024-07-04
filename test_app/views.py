from rest_framework import views,status
from rest_framework.response import Response
from test_app.llm import get_ai_data
from test_app.serializers import PromptSerializer


class TestView(views.APIView):
    '''This is a test view'''

    def post(self, request):
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            response = get_ai_data(text)
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
