from flask_sqlalchemy import SQLAlchemy

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class User(models.Model):
    first_name = models.CharField(max_length = 16, blank=False)
    second_name = models.CharField(max_length = 32, blank=False)
    middle_name = models.CharField(max_length = 32, blank=True)
    access_role = models.ForeignKey('Role', on_delete=models.PROTECT)
    password = models.CharField(max_length = 32, blank=False)
    email = models.CharField(max_length = 256, blank=False)

class Role(models.Model):
    role_name = models.CharField(max_length = 16, blank=False)
    
class Test(models.Model):
    test_name = models.CharField(max_length = 32, blank=False)
    type = models.CharField(max_length = 16, blank=True)
    results = models.IntegerField(default=0)

class Results(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    test = models.ForeignKey('Test', on_delete=models.CASCADE)