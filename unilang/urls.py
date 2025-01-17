from django.urls import path

from . import views

app_name = 'unilang'
urlpatterns = [
    # main page
    path('', views.index, name='index'),
    # display all the languages
    path('languages/', views.languages, name='languages'),
    # display all the words
    path('languages/<int:language_id>/', views.language, name='language'),
    # new language
    path('new_language/', views.new_language, name='new_language'),
    # new word
    path('new_word/<int:language_id>/', views.new_word, name='new_word'),
    # delete languages
    path('delete_languages', views.delete_languages, name='delete_languages'),
    # delete words specific to one language
    path('delete_words/<int:language_id>/', views.delete_words, name='delete_words'),
    # test page
    path('test/<int:language_id>/', views.test, name='test'),
    path('test/<int:language_id>/<int:word_id>/', views.test, name='test_word'),
]