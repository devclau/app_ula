from django.db import models

# Create your models here.
class Pregunta(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    respuesta = models.TextField()

    def __str__(self) -> str:
        return self.titulo

    def dic_preguntas(self):
        return {
            
            'titulo': self.titulo,
            'respuesta':self.respuesta
        }