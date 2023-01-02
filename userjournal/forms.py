from django import forms
from .models import JournalEntry


class JournalEntryForm(forms.ModelForm):
    # To make date added as read only
    date_added = forms.DateTimeField(disabled=True)

    class Meta:
        model = JournalEntry
        fields = ['title', 'journal_entry', 'date_added']
