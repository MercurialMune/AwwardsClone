from django import forms
from .models import Projects, Profile


class UploadForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('project_name','project_photo','description','github_repo','url',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','user_id',)
