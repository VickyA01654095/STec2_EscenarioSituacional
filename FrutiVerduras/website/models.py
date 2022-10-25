from django.db import models

# Create your models here.

class Vendedor(models.Model):
    nombres = models.TextField(unique=False, blank=True, null=True)
    apellido_paterno = models.TextField(unique=False, blank=True, null=True)
    apellido_materno = models.TextField(unique=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rfc = models.TextField(unique=False, blank=True, null=True)
    nombre_comercio = models.TextField(unique=False, blank=True, null=True)
    tipo = models.TextField(unique=False, blank=True, null=True)
    tel_fijo = models.IntegerField(unique=False, blank=True, null=True)
    tel_movil = models.IntegerField(unique=False, blank=True, null=True)
    horario_laboral = models.TextField(unique=False, blank=True, null=True)
    ubicacion = models.TextField(unique=False, blank=True, null=True)
    password = models.TextField(unique=False, blank=True, null=True)
    correo_e = models.TextField(unique=False, blank=True, null=True)
    calificacion = models.FloatField(blank=True,null=True)

    class Meta:
        db_table = 'Vendedor'


class Producto(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    nombre = models.TextField(unique=False, blank=True, null=True)
    fecha_caducidad = models.DateTimeField(blank=False, null=True)
    estado_actual = models.FloatField(blank=True,null=True)
    precio = models.FloatField(blank=True,null=True)
    disponibilidad = models.FloatField(blank=True,null=True)
    en_promocion = models.BooleanField(blank=True, null=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Producto'

class Comprador(models.Model):
    nombres = models.TextField(unique=False, blank=True, null=True)
    apellido_paterno = models.TextField(unique=False, blank=True, null=True)
    apellido_materno = models.TextField(unique=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tel_movil = models.IntegerField(unique=False, blank=True, null=True)
    password = models.TextField(unique=False, blank=True, null=True)
    correo_e = models.TextField(unique=False, blank=True, null=True)

    class Meta:
        db_table = 'Comprador'

class Mensaje(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    mensaje = models.TextField(unique=False, blank=True, null=True)

    class Meta:
        db_table = 'Mensaje'

class Chat(models.Model):
    mensaje = models.ForeignKey(Mensaje, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Chat'

class Producto_apartado(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tiempo_apartado = models.DateTimeField(blank=False, null=True)
    precio = models.FloatField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Producto_apartado'


