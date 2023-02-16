from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.SmallIntegerField()
    image = models.ImageField(upload_to='students', blank=True)

    #upload_to bir yere kaydetmesini istiyorsak

    def __str__(self):
        return f'{self.first_name} {self.last_name}'









#?------------- blank=True , null=True ----------------
    # blank=True, serializer ile ilgilidir, yani boş bırakılabilir,
    # null=True, DB ile ilgilidir, yani boş bırakılabilir ve DB null kayıt edilir,
    #! eğer sadece  blank=True varsa veri boş gelebilir, ama DB kayıt edilmeden önce
    #! bir işlem/hesaplama vs. yapılıp DB boş/null gitmesini önlemek gerekir.