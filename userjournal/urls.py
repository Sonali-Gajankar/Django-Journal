from django.urls import path
from .views import journalhome, UserJournalView, JournalCreateView, JournalUpdateView, JournalDeleteView

urlpatterns = [
    path('', journalhome, name='journal-home'),
    path('journal/', UserJournalView.as_view(), name='user-journal'),
    path('create/', JournalCreateView.as_view(), name='create'),
    path('update/<int:pk>', JournalUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', JournalDeleteView.as_view(), name='delete'),
]