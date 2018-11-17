from rest_framework import generics 
from .serializers import ActivitySerializer
from .models import Activity

class CreateView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def perform_create(self,serializer):
        serializer.save() # saves the post method 
        


