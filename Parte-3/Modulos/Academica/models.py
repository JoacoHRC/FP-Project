from django.db import models
from django.contrib.auth.models import User

# DATABASE DE LAS TAREAS
class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

# DATABASES que no se usaron en la funcionalidad del aplicativo, uso didactico
class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)
    def __str__(self):
        txt= "{0} (Tiempo Estimado:{1}año(s))"
        return txt.format(self.nombre,self.duracion)

class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
    
    def __str__(self):
        txt = " {0}/ Carrera: {1} / {2}"
        if self.vigencia:
            estadoEstudiante = "Vigente"
        else:
            estadoEstudiante = "De Baja"
        return txt.format(self.nombreCompleto(), self.carrera,estadoEstudiante)  

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=40)
    creditos = models.PositiveIntegerField()  # Cambié a PositiveIntegerField
    docente = models.CharField(max_length=100)
    def __str__(self):
        txt ="{0}({1})/ Docente: {2}"
        return txt.format(self.nombre, self.codigo,self.docente)  




class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        txt = "{0} matricula{1} en el curso {2} / Fecha: {3}"
        if self.estudiante.sexo == "F":
            letraSexo = "a"
        else:
            letraSexo = "o"
        fecMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(),letraSexo,self.curso,fecMat)

    