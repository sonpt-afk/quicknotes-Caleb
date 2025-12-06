from django.http import HttpResponse, Http404, JsonResponse
from .models import  Note
from quicknotes.serializers import NoteSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

def home(request):
    return HttpResponse("Welcome Home!")

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data})
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"data": serializer.data})

# def notes(request):
#     data = Note.objects.all()
#     return render(request, 'quicknotes/index.html', {'notes':data, 'form': NoteForm})

# def note(request, note_id):
#     data = get_object_or_404(Note, pk=note_id)
#     return render(request, 'quicknotes/note.html', {'note':data})