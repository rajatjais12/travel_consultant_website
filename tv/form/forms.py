from django import forms
class log_in_f(forms.ModelForm):
	class Meta:
		model=log_in_m
		#widget={'password':forms.PasswordInput(),}
    #name = forms.CharField(max_length=150, db_index=True)
    #email= forms.EmailField(max_length=150, db_index=True)
    #password = forms.CharField(min_length=8,max_length=32, widget=forms.PasswordInput)
