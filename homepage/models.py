from django.db import models

class Kategori(models.Model):
    kategori = models.CharField(max_length=20)
    def __str__(self):
        return self.kategori

class Modul(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.IntegerField(default=0)
    kategori = models.ManyToManyField(Kategori)
    banner_img = models.FileField(upload_to='images/modul/', default=None)
    def __str__(self):
        return self.nama