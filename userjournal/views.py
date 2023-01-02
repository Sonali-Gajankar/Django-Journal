from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import JournalEntry
from .forms import JournalEntryForm

# Create your views here.

def home(request):
    return render(request, 'userjournal/home.html')


def journalhome(request):
    if not request.user.is_authenticated:
        return render(request, "userjournal/home.html")
    return redirect('user-journal')


class UserJournalView(LoginRequiredMixin, generic.ListView):
    template_name = "userjournal/journal_home.html"
    context_object_name = 'user_entry'
    paginate_by = 5

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return JournalEntry.objects.filter(author=self.request.user).order_by('-date_added')


class JournalCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "userjournal/journal_form.html"
    model = JournalEntry
    fields = ['title', 'journal_entry']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class JournalUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    form_class = JournalEntryForm
    template_name = "userjournal/journal_form.html"
    model = JournalEntry

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        entry = self.get_object()
        if entry.author == self.request.user:
            return True
        return False


class JournalDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = JournalEntry
    template_name = "userjournal/journal_entry_delete.html"
    success_url = '/'

    def test_func(self):
        entry = self.get_object()
        if entry.author == self.request.user:
            return True
        return False
