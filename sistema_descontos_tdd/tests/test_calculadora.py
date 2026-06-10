import pytest
from src.calculadora import calcular_valor_final, processar_lista_valores

@pytest.mark.parametrize("entrada, especial, saida", [
    (0, False, 0.0),
    (50, False, 50.0),
    (75, False, 75.0),
    (76, False, 69.92),
    (200, False, 184.0),
    (250, False, 230.0),
    (251, False, 213.35),
    (800, False, 680.0),
    (801, False, 600.75),
    (1000, False, 750.0),
    (100, True, 82.8),
    (300, True, 229.5),
    (1000, True, 675.0),
])
def test_calculos_parametrizados(entrada, especial, saida):
    assert calcular_valor_final(entrada, especial) == saida

def test_valor_negativo():
    with pytest.raises(ValueError, match="não pode ser negativo"):
        calcular_valor_final(-50)

@pytest.mark.parametrize("invalido", ["cem", None, [10], {}])
def test_tipo_invalido(invalido):
    with pytest.raises(TypeError, match="deve ser numérico"):
        calcular_valor_final(invalido)

def test_processar_lista_vazia():
    assert processar_lista_valores([]) == {"media": 0, "total": 0}

def test_processar_lista_completa():
    resultado = processar_lista_valores([100, 200, 300])
    assert "total_original" in resultado
    assert "total_final" in resultado
    assert "economia" in resultado