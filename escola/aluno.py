def calcular_media(notas: list[float]) -> float:
    media = sum(notas) /len(notas)
    return round(media, 1)