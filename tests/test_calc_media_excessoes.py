import pytest
from escola.aluno import calcular_media

def test_calcular_media_lista_vazia():
    
    # Definindo a entrada
    entrada = []

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="não é permitido uma lista vazia"):
        calcular_media(entrada)

def test_calcular_media_enviando_string():
    
    # Definindo a entrada
    entrada = ""

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match="nota invalida"):
        calcular_media(entrada)

def test_calcular_media_string_lista():
    
    # Definindo a entrada
    entrada = [(3,8),20]

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match="não é permitido uma string na lista"):
        calcular_media(entrada) 

def test_calcular_media_num_negativo():
    
    # Definindo a entrada
    entrada = [-10.0]

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="limite da nota \[0, 10\]"):
        calcular_media(entrada) 

def test_calcular_media_num_maiordeDez():
    
    # Definindo a entrada
    entrada = [11.0]

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="limite da nota \[0, 10\]"):
        calcular_media(entrada) 