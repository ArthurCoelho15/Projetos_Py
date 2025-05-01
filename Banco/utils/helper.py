from datetime import date
from datetime import datetime

# Transformando data para string.
def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')

# Transformando string para data.
def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')

# Transformando um valor de real para o formato de contabilidade, com 2 casas decimais.
def formata_float(valor: float) -> str:
    return f'R$ {valor:,.2f}'
