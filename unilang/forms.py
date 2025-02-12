from django import forms

from .models import Language, Word

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['text']
        labels = {'text': ''}


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word']
        labels = {'word': ''}


class LanguageDeletionForm(forms.Form):
    languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label=""
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['languages'].queryset = Language.objects.filter(owner=user)


class WordsDeletionForm(forms.Form):
    words = forms.ModelMultipleChoiceField(
        queryset=Word.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label=""
    )

    def __init__(self, *args, **kwargs):
        language = kwargs.pop('language', None)
        super().__init__(*args, **kwargs)
        if language:
            self.fields['words'].queryset = Word.objects.filter(language=language)


