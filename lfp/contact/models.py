from django.db import models
from django.forms import ModelForm

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField()
	phone=models.IntegerField()
	message=models.TextField(max_length=200)
	companyName=models.CharField(max_length=80)
	subject=models.CharField(max_length=80)

	def __unicode__(self): #__str__ in python3
		return self.name

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'message','companyName','subject'] #or fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
        	self.fields[field].widget.attrs.update({'class' : 'form-control'})
