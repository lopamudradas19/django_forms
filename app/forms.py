from django import forms
c=[('python','PYTHON'),('SQL','SQL'),('DJango','django')]
g=[('male','MALE'),('female','FEMALE')]
class SignUpForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    pw=forms.CharField(widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g)
    course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)