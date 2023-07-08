'''
Views for the app
'''
from typing import Any, Dict

from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ToDoForm
from .models import Todo

# Create your views here.

class ListTodoView(ListView):
    '''
    To list all todos in db
    '''

    model = Todo
    template_name = 'todo/home.html'
    paginate_by = 10
    context_object_name = 'todos'


    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'None')
        order = self.request.GET.get('orderby', 'due_date')
        search_query = self.request.GET.get('search', '')

        if search_query != '':
            conditon1 = Q(title=search_query)
        else:
            conditon1 = Q()

        if filter_val != 'None':
            conditon2 = Q(status=filter_val)
        else:
            conditon2 = Q()

        new_context = Todo.objects.filter(conditon1 & conditon2).order_by(order)

        return new_context

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['current_date'] = timezone.localdate()
        context['filters'] = ['None', 'OPEN', 'WORKING', 'DONE', "OVERDUE"]
        context['selected_filter'] = self.request.GET.get('filter', 'None')
        context['orderby'] = self.request.GET.get('orderby', 'due_date')
        context['orderby_filters'] = ['due_date', 'title']
        return context

class TodoDetailView(DetailView):
    '''
    To list all todos in db
    '''
    model = Todo
    template_name = 'todo/todo_detail.html'
    context_object_name = 'todo'


class CreateToDoView(CreateView):
    '''
    Create a ToDo
    '''
    model = Todo
    template_name = 'todo/todo_form.html'
    form_class = ToDoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "create"
        return context

    def get_success_url(self) -> str:
        return reverse_lazy('detail',args=(self.object.id,))

class UpdateToDoView(UpdateView):
    '''
    Update a ToDo
    '''
    model = Todo
    template_name = 'todo/todo_form.html'
    form_class = ToDoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "update"
        return context

    def get_success_url(self) -> str:
        return reverse_lazy('detail',args=(self.object.id,))



class DeleteToDoView(DeleteView):
    '''
    Delete a ToDo
    '''
    model = Todo
    template_name = 'todo/todo_delete.html'
    success_url = '/'
