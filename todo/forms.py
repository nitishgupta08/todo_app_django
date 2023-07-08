'''
Forms for the app
'''

from django.core.exceptions import ValidationError
from django.forms import (
    CheckboxInput,
    DateInput,
    ModelForm,
    RadioSelect,
    SelectMultiple,
    Textarea,
    TextInput,
)
from django.utils import timezone

from .models import Todo


class ToDoForm(ModelForm):
    '''
    Todo Form
    '''

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']
        if due_date < timezone.localdate():
            raise ValidationError("Due date cannot be before current date.")

        return due_date

    class Meta:
        '''
        Meta class
        '''
        model = Todo
        fields = ['title', 'description', 'tags', 'status', 'due_date', 'high_priority']

        widgets = {
            'title': TextInput(attrs={"class":"form-control"}),
            'due_date': DateInput(attrs={"class":"form-control", "placeholder": 'YYYY-MM-DD'}),
            'description': Textarea(attrs={"class":"form-control","rows":5, "maxlength":1000}),
            'status': RadioSelect(attrs={"class":"radio-inline"}),
            'tags': SelectMultiple(attrs={"class":"form-select"}),
            'high_priority': CheckboxInput(attrs={"class":"form-check-input"}),




        }
