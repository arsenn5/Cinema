from django.http import HttpResponse
from django.views.generic import ListView, FormView
from .forms import ParserForm
from .models import ParserModel


class ParserFilmView(ListView):
    model = ParserModel
    template_name = "parser/film_list.html"

    def get_queryset(self):
        return ParserModel.objects.all()


class ParserFormView(FormView):
    template_name = "parser/start_parser.html"
    form_class = ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse("<h1>Данные взяты......</h1>")
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)
