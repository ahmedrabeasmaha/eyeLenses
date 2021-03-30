from django import forms
from django.contrib.auth import authenticate
from .models import Revealed, Store


class loginForm(forms.Form):
    username = forms.CharField(label='', min_length=4, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'User name', 'class':'form-control'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if username is '':
            raise forms.ValidationError("من فضلك ادخل اسم المستخدم")
        elif password is '':
            raise forms.ValidationError("من فضلك ادخل كلمة السر")
        return user


class RevealedSearchForm(forms.Form):
    name = forms.CharField(required=False, max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'الاسم',
        })

class RevealedForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d-%m-%Y', ])
    revealDate = forms.DateField(input_formats=['%d-%m-%Y', ])

    class Meta:
        model = Revealed
        exclude = ['status', 'delStatus', 'ann']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'التاريخ',
            'readonly': '',
        })
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'اسم العميل',
        })
        self.fields['eye'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'مواصفات الشنبر',
        })
        self.fields['lens'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'نوع العدسه',
        })
        self.fields['given'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'المدفوع',
        })
        self.fields['reminder'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'الباقى',
        })
        self.fields['docName'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'اسم الطبيب',
        })
        self.fields['revealDate'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'التاريخ',
            'readonly': '',
        })
        self.fields['rSphN'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_rSphN")',
            'onfocusout': 'FocusOut("id_rSphN")',
            'onclick': 'FocusClickIn("id_rSphN")',
        })
        self.fields['rCylN'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_rCylN")',
            'onfocusout': 'FocusOut("id_rCylN")',
            'onclick': 'FocusClickIn("id_rCylN")',
        })
        self.fields['rAxisN'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_rAxisN")',
            'onfocusout': 'FocusOut("id_rAxisN")',
            'onclick': 'FocusClickIn("id_rAxisN")',
        })
        self.fields['lSphN'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_lSphN")',
            'onfocusout': 'FocusOut("id_lSphN")',
            'onclick': 'FocusClickIn("id_lSphN")',
        })
        self.fields['lCylN'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_lCylN")',
            'onfocusout': 'FocusOut("id_lCylN")',
            'onclick': 'FocusClickIn("id_lCylN")',
        })
        self.fields['lAxisN'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_lAxisN")',
            'onfocusout': 'FocusOut("id_lAxisN")',
            'onclick': 'FocusClickIn("id_lAxisN")',
        })
        self.fields['rSphF'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_rSphF")',
            'onfocusout': 'FocusOut("id_rSphF")',
            'onclick': 'FocusClickIn("id_rSphF")',
        })
        self.fields['rCylF'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_rCylF")',
            'onfocusout': 'FocusOut("id_rCylF")',
            'onclick': 'FocusClickIn("id_rCylF")',
        })
        self.fields['rAxisF'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_rAxisF")',
            'onfocusout': 'FocusOut("id_rAxisF")',
            'onclick': 'FocusClickIn("id_rAxisF")',
        })
        self.fields['lSphF'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_lSphF")',
            'onfocusout': 'FocusOut("id_lSphF")',
            'onclick': 'FocusClickIn("id_lSphF")',
        })
        self.fields['lCylF'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_lCylF")',
            'onfocusout': 'FocusOut("id_lCylF")',
            'onclick': 'FocusClickIn("id_lCylF")',
        })
        self.fields['lAxisF'].widget.attrs.update({
            'class': 'form-control',
            'value': '--',
            'onfocusin': 'FocusClickIn("id_lAxisF")',
            'onfocusout': 'FocusOut("id_lAxisF")',
            'onclick': 'FocusClickIn("id_lAxisF")',
        })
        self.fields['paName'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'الاسم',
        })

    def clean_date(self):
        data = self.cleaned_data['date']
        if data is '':
            raise forms.ValidationError("من فضلك تاكد من التاريخ")
        return data

    def clean_name(self):
        data = self.cleaned_data['name']
        if data is '':
            raise forms.ValidationError("من فضلك تاكد من الاسم")
        return data

    def clean_revealDate(self):
        data = self.cleaned_data['revealDate']
        if data is '':
            raise forms.ValidationError("من فضلك تاكد من تاريخ الكشف")
        return data

    def clean_paName(self):
        data = self.cleaned_data['paName']
        if data is '':
            raise forms.ValidationError("من فضلك تاكد من تاريخ الاسم")
        return data

    def clean_given(self):
        data = self.cleaned_data['given']
        try:
            float(data)
        except ValueError:
            raise forms.ValidationError("من فضلك تاكد من الباقى")
        else:
            if float(data) < 0:
                raise forms.ValidationError("من فضلك تاكد من الباقى")
        try:
            int(data)
        except ValueError:
            raise forms.ValidationError("من فضلك تاكد من الباقى")
        else:
            if int(data) < 0:
                raise forms.ValidationError("من فضلك تاكد من الباقى")
        return data

    def clean_reminder(self):
        data = self.cleaned_data['reminder']
        try:
            float(data)
        except ValueError:
            raise forms.ValidationError("من فضلك تاكد من الباقى")
        else:
            if float(data) < 0:
                raise forms.ValidationError("من فضلك تاكد من الباقى")
        try:
            int(data)
        except ValueError:
            raise forms.ValidationError("من فضلك تاكد من الباقى")
        else:
            if int(data) < 0:
                raise forms.ValidationError("من فضلك تاكد من الباقى")
        return data


class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'اسم الشنبر',
        })
        self.fields['img'].widget.attrs.update({
            'class': 'custom-file-input',
            'readonly': '',
        })
        self.fields['code'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'كود الشنبر',
        })
        self.fields['quan'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'الكميه',
        })

    def clean_quan(self):
        data = self.cleaned_data['quan']
        try:
            int(data)
        except ValueError:
            raise forms.ValidationError("من فضلك تاكد من الكميه")
        else:
            if int(data) < 0:
                raise forms.ValidationError("من فضلك تاكد من الكميه")
        return data


class StoreSearchForm(forms.ModelForm):
    name = forms.CharField(required=False, max_length=200)
    code = forms.CharField(required=False, max_length=200)

    class Meta:
        model = Store
        fields = ['name', 'code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'اسم الشنبر',
        })
        self.fields['code'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'كود الشنبر',
        })
