from django.views.generic import ListView

# Create your views here.
class SnackListView(ListView):
    template_name = "snacks_list.html"
    model =