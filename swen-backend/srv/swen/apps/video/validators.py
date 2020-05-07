from django import forms

class UploadForm(forms.Form):
    LANG_CHOICES = [ ('en-US' , 'en-US'), ('fr-FR' , 'fr-FR')  ]
    video_url    = forms.URLField(max_length=250)
    language     = forms.ChoiceField(choices=LANG_CHOICES)
    video_name   = forms.CharField(max_length=20)

class InfoForm(forms.Form):
    video_id     = forms.CharField(max_length=20)

class SearchForm(forms.Form):
    LANG_CHOICES = [ ('en-US' , 'en-US'), ('fr-FR' , 'fr-FR')  ]
    language     = forms.ChoiceField(choices=LANG_CHOICES)
    query        = forms.CharField(max_length=20)