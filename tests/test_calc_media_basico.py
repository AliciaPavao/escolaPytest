from escola.aluno import calcular_media

def test_calcular_media_entrada_basica_sem_erro():
    # Defina as entradas     
    entrada = [10.0, 5.0, 6.0, 1.0]

    # Executa o código
    resultado = calcular_media(entrada)

    # Checa a saída
    assert resultado == 5.5