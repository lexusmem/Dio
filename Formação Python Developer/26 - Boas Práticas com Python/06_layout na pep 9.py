# 79 caracteres por linha
# dois espaços nas classes e funções de fora da classe
import sqlalchemy
import datetime
# importações de bibliotecas por linhas
# import datetime, sqlalchemy - Errado

# quebra de linha para múltiplos imports
from datetime import (
    datetime,
    time,
    tzinfo,
    timezone
)

# Indentação
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # errado

matriz = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
