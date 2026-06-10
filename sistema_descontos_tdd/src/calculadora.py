def calcular_valor_final(valor: float, desconto_especial: bool = False) -> float:
    if not isinstance(valor, (int, float)):
        raise TypeError("Valor deve ser numérico")
    
    if valor < 0:
        raise ValueError("Valor não pode ser negativo")
    
    if valor <= 75:
        resultado = float(valor)
    elif valor <= 250:
        resultado = valor * 0.92
    elif valor <= 800:
        resultado = valor * 0.85
    else:
        resultado = valor * 0.75
        
    if desconto_especial:
        resultado = resultado * 0.90

    return round(resultado, 2)


def processar_lista_valores(lista: list) -> dict:
    if not lista:
        return {"media": 0, "total": 0}
    
    resultados = [calcular_valor_final(v) for v in lista]
    
    return {
        "total_original": round(sum(lista), 2),
        "total_final": round(sum(resultados), 2),
        "economia": round(sum(lista) - sum(resultados), 2)
    }