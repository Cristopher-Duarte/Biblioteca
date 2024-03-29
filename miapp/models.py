from django.db import models

class Libro(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    isbn = models.CharField(max_length=45)
   
    def __str__(self):
        return self.nombre

class Ejemplar(models.Model):
    numeroejemplar = models.CharField(max_length=45)
    fechadecompra = models.DateField(null=False)
    Libro = models.ForeignKey('Libro',on_delete=models.CASCADE) 
    def __str__(self):
        return self.numeroejemplar +"-> " +str(self.Libro) 

class Prestamo(models.Model):
    fechaprestamo = models.DateField(null=False)
    nombrecliente = models.CharField(max_length=45)
    telefonocliente = models.CharField(max_length=45)
    estado = models.BooleanField(null=False)
    def __str__(self):
        return self.nombrecliente

class DetallelPrestamo(models.Model):
    Prestamo = models.ForeignKey('Prestamo',on_delete=models.CASCADE)
    Ejemplar = models.ForeignKey('Ejemplar',on_delete=models.CASCADE)
    fechadevolucion = models.DateField("Fecha de Devolucion",null=True)

    def __str__ (self):
        return "{0},{1}".format(self.Prestamo,self.Ejemplar)

