from django.db import models

class RickAndMorty(models.Model):
    
    nome = models.CharField(
        "Origem do Personagem:", 
        max_length=255,
        blank=True
    )

    genero = models.CharField(
        "Gênero do Personagem:", 
        max_length=255,
        blank=True
    )
    
    status = models.CharField(
        "Status do Personagem:", 
        max_length=255,
        blank=True
    )

    especie = models.CharField(
        "Origem do Personagem:", 
        max_length=255,
        blank=True
    )
    
    origem = models.CharField(
        "Origem do Personagem:", 
        max_length=255,
        blank=True
    )
    localizacao = models.CharField(
        "Localização do Personagem:", 
        max_length=255,
        blank=True
    )

    class Meta:
        verbose_name = "Personagem"
        verbose_name_plural = "Personagens"
    
    def __str__(self):
        return f"{self.fact}"