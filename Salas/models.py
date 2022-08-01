from django.db import models

# Create your models here.
class Sede(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 50, unique=True, null=False, blank=True )
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add= True)

    def __str__(self) :
        fila = self.nombre 
        return fila
        #otra manera de hacer algo parecido
        #return f'{self.nombre} -> {self.calle}'

class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    
    tipoSala =[
        ('g','Génesis'),
        ('p','Piscis'),
        ('h1','Híbrida_Tipo_1'),
        ('h2','Híbrida_Tipo_2'),
        ('pi','Pile'),
        ('a3','A3')
    ]
    tipoDeSalas = models.CharField(max_length=2, choices=tipoSala, default= 'p')
    sede = models.ForeignKey(Sede, null=False, blank=False, on_delete=models.CASCADE)
    piso = models.IntegerField(default= 1)
    capacidad = models.PositiveIntegerField()

    estado =[
        ('O','Operativa'),
        ('M', 'Mantención'),
        ('B', 'Baja')
    ]
    estadoSala = models.CharField(max_length=1, choices = estado, default = 'Operativa')

    siNo = [
        ('S', 'Si'),
        ('N', 'No')
    ]
    wifi = models.CharField(max_length=1, choices=siNo, default ='No')
    
    tipoCable = [
        ('H','HDMI'),
        ('V','VGA')
    ]
    cableProfesor = models.CharField(max_length=1, choices= tipoCable, default= 'V')
    
    tipoCajaVideo= [
        ('p', 'Pared'),
        ('m','Meson'),
        ('n', 'No tiene')
    ]
    tipoCaja = models.CharField(max_length=1, choices = tipoCajaVideo, default = 'p' )
    
    def __str__(self) :
        salaFila = self.nombre
        return salaFila


class Computador(models.Model):
    id = models.AutoField(primary_key=True)
    sistemaOperativo = models.CharField(max_length=20, verbose_name="Sistema Operativo")
    ip = models.CharField(max_length=50,verbose_name= "Dirección IP", unique=True)
    mac =  models.CharField(max_length=20, verbose_name = "Dirección MAC",unique= True)
    mascaraSubRed = models.CharField(max_length=50, verbose_name = "Máscara Sub-Red", blank= True)
    fechaInstalacion = models.DateField(verbose_name="Fecha Instalación",blank= True)
    procesador = models.CharField(max_length=50, verbose_name = "Procesador")
    memoriRam = models.CharField(max_length=50, verbose_name = "Memoria Ram")
    
    estado =[
        ('O','Operativo'),
        ('M', 'Mantención'),
        ('B', 'Baja')
    ]
    estadoPC = models.CharField(max_length=1, choices= estado, default='Operativo', verbose_name = "Estado")
    sala =models.ForeignKey(Sala, null=False, blank= False, on_delete=models.CASCADE)


    def __str__(self) :
        fila = "sistemaOperativo: " + self.ip + " - " + self.mac
        return fila
""""
class Procesador(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20)
    socket = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    computador =models.ForeignKey(Computador, null=False, blank= False, on_delete=models.CASCADE)

class memoriaRam(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20)
    capacidad = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    frecuencia = models.CharField(max_length=20)
    computador =models.ForeignKey(Computador, null=False, blank= False, on_delete=models.CASCADE)
"""
class Monitor(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20)
    serie = models.CharField(max_length=50, blank= True)
    modelo = models.CharField(max_length=20, blank= True)
    fechaInstalacion = models.DateField(verbose_name="Fecha Instalación",blank= True)
    tamañoMonitor = [
        ('a', 17),
        ('b', 18),
        ('c', 19),
        ('d', 20 ),
        ('f', 21),
        ('g', 22)
    ]
    tamaño = models.CharField(max_length = 1,choices = tamañoMonitor, default ="a")

    estado =[
        ('O','Operativo'),
        ('M', 'Mantención'),
        ('B', 'Baja')
    ]
    estadoMonitor = models.CharField(max_length=1, choices= estado, default='Operativo')
    sala =models.ForeignKey(Sala, null=False, blank= False, on_delete=models.CASCADE)

class Proyector(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20)
    serie = models.CharField(max_length=50)
    modelo = models.CharField(max_length=20)
    horasLampara = models.PositiveIntegerField()
    fechaInstalacion = models.DateField()

    siNo = [
        ('S', 'Si'),
        ('N', 'No')
    ]
    #verificar CAMPO controlRemoto = models.BooleanField(defauld=True)
    controlRemoto = models.CharField(max_length=1, choices= siNo, default = 'Si')
    estado =[
        ('O','Operativo'),
        ('M', 'Mantención'),
        ('B', 'Baja')
    ]
    estadoProyector = models.CharField(max_length=1, choices= estado, default='Operativo')
    sala =models.ForeignKey(Sala, null=False, blank= False, on_delete=models.CASCADE)

class Sonido(models.Model):
    id = models.AutoField(primary_key=True)
    cantidadParlantes = models.PositiveIntegerField()
    sistemaSonido = [
        ('1', 'Amplificador'),
        ('2', 'SubWoofer'),
        ('3', 'Parlantes'),
        ('4', 'No Posee')
    ]
    tipoSistemaSonido = models.CharField(max_length=1,choices = sistemaSonido, default = 'Amplificador')
    sala =models.ForeignKey(Sala, null=False, blank= False, on_delete=models.CASCADE)

class Telon(models.Model):
    id = models.AutoField(primary_key=True)
    tipoTelon=[
        ('a', 'Manual'),
        ('b', 'Mecanico')
    ]
    telon = models.CharField(max_length=1, choices=tipoTelon, default = "a")
    sala =models.ForeignKey(Sala, null=False, blank= False, on_delete=models.CASCADE)
    estado =[
        ('O','Operativo'),
        ('M', 'Mantención'),
        ('B', 'Baja')
    ]
    estadoTelon = models.CharField(max_length=1, choices= estado, default='Operativo')