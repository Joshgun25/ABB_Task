from django import forms

# Upload File Form
class UploadFileForm(forms.Form):
    file = forms.FileField()

# URL Form
class URLForm(forms.Form):
    url = forms.URLField(label='Website URL', required=True)