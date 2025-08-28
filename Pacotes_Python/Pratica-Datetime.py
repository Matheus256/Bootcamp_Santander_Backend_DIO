from datetime import timedelta, datetime

#tabelacom o porte do carro e o tempo de lavagem
tabela = {
    "P": 30,
    "M": 45,
    "G": 60,
}

porte_do_carro = "P"
data_atual = datetime.now() 
data_estimada = data_atual + timedelta(minutes = tabela[porte_do_carro])

print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

#Outro exemplo do uso de timedelta
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours = 1)
print(resultado.time())

#Ajuste na formatação do datetime
data_hora_atual = datetime.now()
mascara_ptbr = "%d/%m/%Y"

print(data_hora_atual.strftime(mascara_ptbr))

mascara_ptbr = "%d/%m/%Y %a"

print(data_hora_atual.strftime(mascara_ptbr))

#Converter string pra data
data_hora_str = "2025-10-20 10:20"
mascara_en = "%Y-%m-%d %H:%M"

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)

#Trabalhando com timezones
import pytz

data_oslo = datetime.now(pytz.timezone("Europe/Oslo"))
print(data_oslo)

data_sao_paulo = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(data_sao_paulo)

#Outra maneira de tratar timezones
from datetime import timezone
data_oslo = datetime.now(timezone(timedelta(hours = 2)))
print(data_oslo)

data_sao_paulo = datetime.now(timezone(timedelta(hours = -3)))
print(data_sao_paulo)