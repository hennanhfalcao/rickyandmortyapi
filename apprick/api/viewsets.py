from rest_framework import viewsets
from .serializers import RickAndMortySerializer, RickAndMorty
import requests
from rest_framework.response import Response
from urllib.parse import quote
from rest_framework import status

class RickAndMortyViewSet(viewsets.ModelViewSet):
    queryset = RickAndMorty.objects.all()
    serializer_class = RickAndMortySerializer


    def create(self, request):

        nome_personagem = request.data.get("nome", '')
        nome_codificado = quote(nome_personagem.lower())

        try:
            requisicao = request.get(f"https://rickandmortyapi.com/api/character/?name={nome_codificado}")
        except request.RequestException as e:
                return requests.Response({"aviso":f"Erro ao acessar a API externa:{e}"})
        
        json = requisicao.json()

        if"results" in json and len(json['results']) > 0:
            personagem = json['results'][0]
        else: return requests.Response({"aviso":f"Personagem não encontrado"})

        nome = personagem.get("name",'')
        genero = personagem.get('gender', '')
        status = personagem.get("status", '')
        especie = personagem.get('species', '')
        origem = personagem.get("origin", {}.get("name",''))
        localizacao = personagem.get("location", {}.get("name",''))

        personagem_criado = {
            "nome": nome,
            "genero": genero,
            "status": status,
            "especie": especie,
            "origem": origem,
            "localizacao":localizacao,
        }


        meu_serializador = RickAndMortySerializer(data=personagem_criado)

        if meu_serializador.is_valid():
            
            personagem_validation = RickAndMorty.objects.all.filter(nome=nome)
            personagem_existe = personagem_validation.exists()

            if personagem_existe:
                return Response({"aviso":"Personagem já existe!"})
            
            meu_serializador.save()
            return Response ({"aviso":"Personagem criado com sucesso!"})

        else:
            return Response({"aviso":"Esse personagem não é válido!"})