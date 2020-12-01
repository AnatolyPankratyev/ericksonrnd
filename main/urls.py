from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about', views.about_coaching_view, name='about'),
    path('basic-course', views.basic_course_view, name='basic-course'),
    path('science-and-art', views.science_and_art_view, name='science-and-art'),
    path('contacts', views.contacts_view, name='contacts'),
    path('for-business', views.for_business_view, name='for-business'),
    path('management-coaching', views.management_coaching_view, name='management-coaching'),
    path('mentoring', views.mentoring_view, name='mentoring'),
    path('professional-community', views.professional_community_view, name='professional-community'),
    path('training-programs', views.training_programs_view, name='training-programs'),
]
