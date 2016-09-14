from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class pregunta(models.Model):
    pregunta_text = models.CharField(max_length=200)
    pub_fecha = models.DateTimeField('date published')
    def __str__(self):
        return self.pregunta_text

class respuesta(models.Model):
    pregunta = models.ForeignKey(pregunta, on_delete=models.CASCADE)
    respuesta_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.respuesta_text
  