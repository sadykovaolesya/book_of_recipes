from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View, ListView, DetailView
from django.urls import reverse_lazy

from book.models import Author, Recipe, RecipeIngredient, Ingredient
from .forms import UserLoginForm, UserRegistrationForm, AddRecipe, IngredientFormset
from django.db.models import Count
from django.db.models import Prefetch


class LoginUserView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm


class RegistrationView(CreateView):
    model = Author
    form_class = UserRegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')


class PaginatedFilterViews(View):
    def get_context_data(self, **kwargs):
        context = super(PaginatedFilterViews, self).get_context_data(**kwargs)
        if self.request.GET:
            querystring = self.request.GET.copy()
            if self.request.GET.get('page'):
                del querystring['page']
            context['querystring'] = querystring.urlencode()
        return context


class RecipeList(PaginatedFilterViews, ListView):
    model = Recipe
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self, **kwargs):
        recipe_ingredient = Prefetch('recipe_ingredient', RecipeIngredient.objects.prefetch_related('ingredient'))
        title = self.request.GET.get('title')
        if title:
            return Recipe.objects.prefetch_related(recipe_ingredient).filter(title__istartswith=title)
        ingredients = self.request.GET.getlist('check')

        if ingredients:

            recipes = RecipeIngredient.objects.filter(ingredient__in=ingredients).values('recipe').annotate(
                cnt=Count('id')).filter(cnt__gt=len(ingredients) - 1).values('recipe')

            return Recipe.objects.prefetch_related(recipe_ingredient).filter(pk__in=recipes)

        elif 'id_author' in self.kwargs:

            return Recipe.objects.prefetch_related(recipe_ingredient).filter(author=self.kwargs['id_author'])
        else:

            return Recipe.objects.prefetch_related(recipe_ingredient).all()


class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'recipe.html'

    def get_object(self, queryset=None):
        recipe_ingredient = Prefetch('recipe_ingredient', RecipeIngredient.objects.prefetch_related('ingredient'))
        return Recipe.objects.select_related().prefetch_related(recipe_ingredient).get(id=self.kwargs['pk'])


class RecipeCreate(CreateView):
    model = Recipe
    form_class = AddRecipe
    template_name = 'add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = IngredientFormset(queryset=RecipeIngredient.objects.none())
        return context

    def post(self, request):
        formset = IngredientFormset(data=self.request.POST)
        form = self.form_class(request.POST, request.FILES)

        if formset.is_valid() and form.is_valid():
            return self.form_valid(formset, form)
        return render(request, self.template_name, {'form': form, 'formset': formset})

    def form_valid(self, formset, form):

        form.instance.author = self.request.user
        form.save()

        instances = formset.save(commit=False)

        for instance in instances:
            instance.recipe = form.save()
            instance.save()

        return HttpResponseRedirect('/')