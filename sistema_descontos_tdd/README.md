# 💰 Sistema de Cálculo de Preços com Descontos em Escala

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Pytest](https://img.shields.io/badge/Pytest-9.0.3-green?style=for-the-badge&logo=pytest)
![TDD](https://img.shields.io/badge/TDD-Quality%20Assurance-red?style=for-the-badge)

## 📌 Sobre

Sistema desenvolvido para aplicar descontos progressivos em valores numéricos, seguindo uma escala pré-definida de faixas. O projeto foi construído utilizando a metodologia **Test-Driven Development (TDD)** garantindo robustez e confiabilidade nos cálculos.

## 👨‍💻 Desenvolvedor

**Aluno:** Heverton Xavier  
**Curso:** Quality Assurance (QA)

## ⚙️ Funcionalidades

- ✅ Cálculo de desconto baseado em faixas de valor
- ✅ Benefício especial para clientes selecionados
- ✅ Processamento em lote de múltiplos valores
- ✅ Validação de entradas (tipos e valores negativos)
- ✅ Tratamento robusto de erros

## 📐 Regras de Cálculo

O sistema avalia o valor de entrada e aplica as seguintes regras:

| Faixa (R$) | Desconto | Fórmula |
|:---|:---:|:---|
| 0 a 75 | 0% | Valor original |
| 75.01 a 250 | 8% | Valor × 0.92 |
| 250.01 a 800 | 15% | Valor × 0.85 |
| Acima de 800 | 25% | Valor × 0.75 |

### ✨ Benefício Adicional

Quando o parâmetro `desconto_especial` é ativado, aplica-se **10% de desconto extra** sobre o valor já descontado.

## 📦 Estrutura do Projeto

lab_qa_software/
├── src/
│ └── calculadora.py # Lógica principal do sistema
├── tests/
│ ├── test_calculadora.py # Testes automatizados
│ └── test_avance_calculadora.py # Testes avançados
├── requirements.txt # Dependências do projeto
└── README.md # Documentação
text


## 🚀 Como Executar

### Pré-requisitos

- Python 3.13 ou superior
- Virtual Environment (recomendado)

### Passos

1. **Criar e ativar ambiente virtual**
python -m venv venv
venv\Scripts\activate     # Windows
===============================================
2. **Instalar dependências**
pip install -r requirements.txt
===============================================
3. **Executar os testes**
pytest -v
