import pytest
from src.calculadora import calcular_valor_final

def test_limite_setenta_cinco():
    assert calcular_valor_final(75) == 75

def test_acima_limite_primeira_faixa():
    assert calcular_valor_final(76) == 69.92

def test_negativo_lanca_erro():
    with pytest.raises(ValueError):
        calcular_valor_final(-1)

def test_zero_retorna_zero():
    assert calcular_valor_final(0) == 0

def test_desconto_especial_cem():
    assert calcular_valor_final(100, True) == 82.8

def test_maior_faixa():
    assert calcular_valor_final(900, False) == 675.0