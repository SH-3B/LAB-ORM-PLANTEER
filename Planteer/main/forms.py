from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your message here...'})
        }
class ContactMessageReplyForm(forms.Form):
    reply = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), label="Your Reply")