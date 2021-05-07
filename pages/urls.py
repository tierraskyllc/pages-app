from django.urls import path

from .views import AboutPageView, HomePageView, RafaelPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('rafael/', RafaelPageView.as_view(), name='rafael')
]
