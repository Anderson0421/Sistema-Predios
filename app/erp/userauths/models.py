from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

from app.settings import MEDIA_URL, STATIC_URL


def validate_dni_length(value):
    if len(str(value)) != 8:
        raise ValidationError(
            ('El DNI debe tener exactamente 8 dígitos.'),
            code='invalid_dni_length'
        )


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DNI = models.PositiveIntegerField(blank=True, null=True, unique=True,validators=[validate_dni_length])
    image = models.ImageField(upload_to='users/', default='users/default.png', null=True, blank=True)
    nombres = models.CharField(max_length=200, null=True, blank=True)
    apellidos = models.CharField(max_length=200, null=True, blank=True)
    verified = models.BooleanField(default=False, null=True, blank=True)
    #Contribuyente attrs
    cod_contri_rentas = models.PositiveIntegerField(unique=True, null=True, blank=True, verbose_name='Codigo de rentas :')
    cod_predial_rentas = models.PositiveIntegerField(unique=True, null=True, blank=True)
    persona_juridica = models.BooleanField(default=False)
    ruc = models.PositiveIntegerField(blank=True, null=True)
    telefono = models.PositiveIntegerField(blank=True, null=True)
    Deudas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.DNI)

    def contar_deudas_pendientes(self):
        # Contar las deudas pendientes asociadas a este contribuyente
        cantidad_deudas_pendientes = Deuda.objects.filter(contribuyente=self, estado='pendiente').count()
        return cantidad_deudas_pendientes




ESTADO_CHOICES = (
    ('pendiente', 'Pendiente'),
    ('cancelado', 'Cancelado'),
    ('vencido', 'vencido'),
)


class Predio(models.Model):
    cuc = models.CharField(max_length=50, unique=True)
    cod_ref_catastral = models.CharField(max_length=13)
    departamento = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    distrito = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    manzana = models.CharField(max_length=50)
    lote = models.CharField(max_length=50)
    propietario = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)





    def __str__(self):
        return self.cuc

class Deuda(models.Model):
    contribuyente = models.ForeignKey(Profile, on_delete=models.CASCADE)
    deuda = models.BooleanField()
    monto_deuda = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_edit = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')  # Agregamos el campo de estado
    # Puedes agregar más campos relacionados con la deuda, como fecha, descripción, etc.

    def __str__(self):
        return f"Deuda de {self.contribuyente} - Monto: {self.monto_deuda}"

    def save(self, *args, **kwargs):
        # Verificar el estado antes de guardar la deuda
        if self.estado == 'pendiente':
            if not self.id:
                self.contribuyente.Deudas = self.contribuyente.contar_deudas_pendientes() + 1
        elif self.estado == 'cancelado':

            self.contribuyente.Deudas = self.contribuyente.contar_deudas_pendientes() - 1

        self.contribuyente.save()
        super().save(*args, **kwargs)


class Construccion(models.Model):
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    numero_piso = models.PositiveIntegerField()
    material_estructural_predominante = models.CharField(max_length=50)
    estado_conservacion = models.CharField(max_length=50)
    estado_construccion = models.CharField(max_length=50)

    def __str__(self):
        return f"Construcción en {self.predio} - Piso {self.numero_piso}"

