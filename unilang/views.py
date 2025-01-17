from django.shortcuts import render, redirect
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Language, Word
from .forms import LanguageForm, LanguageDeletionForm, WordsDeletionForm


def index(request):
    return render(request, 'unilang/index.html')


@login_required
def languages(request):
    languages = Language.objects.filter(owner=request.user).order_by('date_added')
    context = {'languages': languages}
    return render(request, 'unilang/languages.html', context)


@login_required
def language(request, language_id):
    language = Language.objects.get(id=language_id)
    if language.owner != request.user:
        raise Http404

    words = Word.objects.filter(language=language).order_by('date_added')
    context = {'language': language, 'words': words}
    return render(request, 'unilang/language.html', context)


@login_required
def new_language(request):
    if request.method != 'POST':
        form = LanguageForm()
    else:
        form = LanguageForm(data=request.POST)
        if form.is_valid():
            new_language = form.save(commit=False)
            new_language.owner = request.user
            new_language.save()
        return redirect('unilang:languages')

    context = {'form': form}
    return render(request, 'unilang/new_language.html', context)


@login_required
def new_word(request, language_id):
    language = Language.objects.get(id=language_id)
    if language.owner != request.user:
        raise Http404

    WordformSet = modelform_factory(Word, fields=('word', 'translation'))

    if request.method != 'POST':
        form = WordformSet()
    else:
        form = WordformSet(data=request.POST)
        if form.is_valid():
            new_word = form.save(commit=False)
            new_word.language = language
            new_word.save()
            return redirect('unilang:language', language_id=language_id)

    context = {'language': language, 'form': form}
    return render(request, 'unilang/new_word.html', context)


@login_required
def delete_languages(request):
    languages = Language.objects.all()

    if request.method != 'POST':
        form = LanguageDeletionForm()
    else:
        form = LanguageDeletionForm(data=request.POST)
        if form.is_valid():
            selected_languages = form.cleaned_data['languages']
            selected_languages.delete()
            return redirect('unilang:languages')

    context = {'form': form, 'languages': languages}
    return render(request, 'unilang/delete_languages.html', context)


@login_required
def delete_words(request, language_id):
    language = Language.objects.get(id=language_id)
    if language.owner != request.user:
        raise Http404

    words = language.word_set.all()

    if request.method != 'POST':
        form = WordsDeletionForm(language=language)
    else:
        form = WordsDeletionForm(data=request.POST, language=language)
        if form.is_valid():
            selected_words = form.cleaned_data['words']
            selected_words.delete()
            return redirect('unilang:language', language_id=language_id)

    context = {'language': language, 'form': form, 'words': words}
    return render(request, 'unilang/delete_words.html', context)


@login_required
def test(request, language_id, word_id=None):
    language = Language.objects.get(id=language_id)
    if language.owner != request.user:
        raise Http404

    words = Word.objects.filter(language=language)

    if word_id:
        current_word = Word.objects.get(id=word_id)
    else:
        current_word = words.first()

    next_word = words.filter(id__gt=current_word.id).first()

    if not words.exists():
        context = {'current_word': None, 'next_word': None, 'language': language}
        return render(request, 'unilang/test.html', context)

    context = {'current_word': current_word, 'next_word': next_word, 'language': language}
    return render(request, 'unilang/test.html', context)