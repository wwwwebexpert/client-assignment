from django import forms  
from clients.models import Client  
class ClientForm(forms.ModelForm):
    cusername = forms.CharField(max_length=100)
    cname = forms.CharField(max_length=30, required=False)
    cphone = forms.CharField(max_length=15)
    cemail = forms.EmailField(max_length=50)
    cstreet = forms.CharField(max_length=30, required=False)
    csuburb = forms.CharField(max_length=30, required=False)
    cstate = forms.CharField(max_length=30, required=False)
    cpostcode = forms.CharField(max_length=30, required=False)

    class Meta:
            model = Client
            fields = ('cusername', 'cname', 'cphone','cemail','cstreet', 'csuburb', 'cstate','cpostcode')


    def clean(self):
        cusername = self.cleaned_data.get("cusername")
        cemail = self.cleaned_data.get("cemail")
        cname = self.cleaned_data.get("cname")
        cphone = self.cleaned_data.get("cphone")
        cstreet = self.cleaned_data.get("cstreet")
        csuburb = self.cleaned_data.get("csuburb")
        cstate = self.cleaned_data.get("cstate")
        cpostcode = self.cleaned_data.get("cpostcode")
        if self.instance.id is not None:
            if Client.objects.filter(cusername=cusername).exclude(id=self.instance.id).exists():
                raise forms.ValidationError(u'Username "%s" is already in use.' % cusername)
        else:
            if Client.objects.filter(cusername=cusername).exists():
                raise forms.ValidationError(u'Username "%s" is already in use.' % cusername)

        return self.cleaned_data

    def save(self, commit=True):
        if commit:
            self.instance.save()
            self._save_m2m()
        else:
            self.save_m2m = self._save_m2m
        return self.instance