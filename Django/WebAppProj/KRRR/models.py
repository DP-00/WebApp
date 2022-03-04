#every time model is changed run:
#>python manage.py makemigrations appName

#command takes migration names and returns their SQL (doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django):
#>python manage.py sqlmigrate appName 0001

#to create those model tables in your database (run every time the model is changed)
#>python manage.py migrate

from django.db import models

class className(models.Model):
	someText = models.CharField(max_length = 256)
	someDate = models.DateTimeField('date published') #first parameter is defining human readable naem
	someInt = models.IntegerField(default=0)
	def __str__(self):
        	return self.some_text  # text which will represent the object

