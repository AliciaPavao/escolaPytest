def calcular_media(notas: list[float]) -> float:

    """"
    Calcula a média de uma lista de notas.

    Parâmetros:
    notas (list[float]): Lista de notas a serem calculadas.

    Retorna:
    float: A média das notas, arredondada para uma casa decimal.
    """
    # Validando se tem uma string
    if not isinstance(notas, list):
        raise TypeError("nota invalida")
    
    # Validando se tem uma string 2.0
    # if type(notas) != list:
    #     raise TypeError("nota invalida")
    
    # Validando se a lista é vazia
    if len(notas) == 0:
        raise ValueError("não é permitido uma lista vazia")

    # Validando se todos os elementos da lista são numeros (int e float)
    for nota in notas:
        if not isinstance(nota, (int, float)):
            raise TypeError("não é permitido uma string na lista")
        
        if nota > 10:
            raise ValueError("limite da nota [0, 10]")
        
        if nota < 0:
            raise ValueError("limite da nota [0, 10]")
    
    


    media = sum(notas) /len(notas)
    return round(media, 1)