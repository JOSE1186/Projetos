# Importação de bibliotecas
import time

# Entrada de dados iniciais
umidade = int(input('Digite a umidade: '))
temperatura = int(input('Digite a temperatura ambiente: '))

# Verificação de clima de inverno
if (temperatura <= 20 and umidade >= 40):
    # Processo de desumidificação para clima de inverno
    print('Clima de inverno')
    time.sleep(1)
    
    print(f'Temperatura atual: {temperatura}°C')
    time.sleep(1)
    print(f'Umidade atual: {umidade}%')
    time.sleep(1)
    print('Desumidificador ON')
    time.sleep(2)

    # Verificação de temperatura > 15°C
    if (temperatura > 15):
        # Processo com apenas exaustor
        print('Exaustor ON')
        time.sleep(2)
        print('1...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('3...')
        time.sleep(1)
        print('4...')
        time.sleep(1)
        print('5...')
        time.sleep(1)
        print('Umidade menor que 5%')
        time.sleep(3)
        print('Desumidificação concluída')
        time.sleep(2)
    # Verificação de temperatura <= 15°C
    elif (temperatura <= 15):
        # Processo com exaustor e aquecimento
        print('Exaustor ON')
        time.sleep(1)
        print('Aquecimento ON')
        while temperatura < 100:
            temperatura += 10
            if temperatura > 100:
                temperatura = 100
            print(f'Temperatura atual: {temperatura}°C')
            time.sleep(1)
        print('Umidade menor que 5%')
        time.sleep(3)
        print('Aquecimento OFF')
        time.sleep(2)
        print('Exaustor OFF')
        time.sleep(2)
        print('1...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('3...')
        time.sleep(2)
        print('Desumidificação concluída')
        time.sleep(2)
        
# Processo para clima normal
else:
    # Mensagens de clima normal e início de cocção
    time.sleep(3)
    print('O clima não é de inverno')
    time.sleep(3)
    print('Prosseguir com a cocção')
    time.sleep(3)

# Processo de cocção
print('Iniciando cocção...')
time.sleep(2)

# Controle de umidade para cocção
umidade1 = int(input('Digite a umidade interna: '))

# Verificação de necessidade do exaustor
if umidade1 > 15:
    # Ativação do exaustor
    time.sleep(2)
    print('Exaustor ON')
    time.sleep(2)

# Controle de temperatura para cocção
temperatura1 = int(input('Digite a temperatura interna: '))
time.sleep(2)

# Verificação de faixas de temperatura
if temperatura1 < 200:
    # Processo de aquecimento até 380°C
    print('Aquecimento ON')
    time.sleep(2)
    temperatura_atual = temperatura1
    while temperatura_atual < 380:
        print(f'Temperatura atual: {temperatura_atual}°C')
        if temperatura_atual + 100 >= 380:
            temperatura_atual = 380
        else:
            temperatura_atual += 100
        time.sleep(2)
elif temperatura1 >= 380:
    # Manutenção da temperatura atual
    print('A temperatura já atingiu o valor desejado')
    temperatura_atual = temperatura1
else:
    # Processo de aquecimento controlado
    print('Aquecimento ON')
    temperatura_atual = temperatura1
    while temperatura_atual < 380:
        print(f'Temperatura atual: {temperatura_atual}°C')
        if temperatura_atual + 100 >= 380:
            temperatura_atual = 380
        else:
            temperatura_atual += 100
        time.sleep(2)

print(f'Temperatura final: {temperatura_atual}°C')
time.sleep(2)

# Finalização do processo de umidade
if umidade1 > 15:
    # Desligamento do exaustor
    print('Umidade interna menor que 5%')
    time.sleep(2)
    print('Exaustor OFF')
    time.sleep(2)

# Finalização do processo de cocção
# Aguarda confirmação do usuário
# Exibe mensagens finais
print('Insira o conteúdo para cocção')
time.sleep(2)
input('Pressione ENTER para finalizar')
time.sleep(2)
print('Cocção a 380°C por 3 horas')
time.sleep(2)
print('Cocção concluída')
time.sleep(2)

