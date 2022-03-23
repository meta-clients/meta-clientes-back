from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ClientModel(BaseModel):
    name = models.CharField('name', max_length=255)
    email = models.EmailField('email',max_length=255)
    phone = models.CharField('celular', max_length=13)
    birthdate = models.DateField()
    has_child = models.BooleanField(default=False)
    number_of_children = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ChildrenModel(BaseModel):
    GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female'),
        ('no-binary','No Binary')
    ]
    gender = models.CharField(max_length=9, choices=GENDER_CHOICES)
    clother_size = models.CharField(max_length=4)
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE, related_name='children_id')