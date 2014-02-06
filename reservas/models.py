from django.db import models

class Vehiculo(models.Model):
    codigo = models.CharField(max_length=20,unique=True)
    patente = models.CharField(max_length=20,null=True)
    marca = models.CharField(max_length=30,null=True)
    modelo = models.CharField(max_length=20,null=True)
    anio = models.PositiveSmallIntegerField(null=True)
    capacidad = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Vehiculos"

    def __unicode__(self):
        return u'%s %s' % (self.codigo, self.patente)
    
class Chofer(models.Model):
    dni = models.PositiveIntegerField(unique=True)
    licencia = models.PositiveIntegerField()
    vencimiento = models.DateField(null=True)
    nombre = models.CharField(max_length=100,null=True)
    fecha_nacimiento = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Choferes"

    def __unicode__(self):
        return u'%s %s' % (self.dni, self.nombre)

class Viaje(models.Model):
    fecha_hora = models.DateTimeField(unique=True)
    vehiculo = models.ForeignKey(Vehiculo)
    chofer = models.ForeignKey(Chofer)
    ocupados = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Viajes"

    def __unicode__(self):
        return u'%s %s %s %s' % (self.fecha_hora, self.vehiculo, self.chofer, self.ocupados)

class Pasajero(models.Model):
    dni = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,unique=True)
    clave = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Pasajeros"

    def __unicode__(self):
        return u'%s' % (self.email)

class Reserva(models.Model):
    pasajero = models.ForeignKey(Pasajero)
    viaje = models.ForeignKey(Viaje)
    
    class Meta:
        verbose_name_plural = "Reservas"
        
    def __unicode__(self):
        return u'usuario: %s - fecha: %s - hora: %s' % (self.pasajero, self.viaje.fecha_hora.strftime('%Y-%m-%d'), self.viaje.fecha_hora.strftime('%H:%M'))