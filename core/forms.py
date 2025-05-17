from django import forms
from .models import JobApplication, ContactMessage

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'resume']


##### Contact form ###################

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Your Name',
                'autocomplete': 'off'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Your Email',
                'autocomplete': 'off'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Your Message',
                'rows': 5,
                'style': 'resize: vertical;'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['style'] = 'margin-bottom: 15px;'

########### end contact form ###########