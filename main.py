import os
import time
import matplotlib.pyplot as plt
import csv

# Função para ler a temperatura da CPU
def ler_temperatura_cpu():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as arquivo:
        temperatura_milicelsius = int(arquivo.read())
    temperatura_celsius = temperatura_milicelsius / 1000.0  # Converter para Celsius
    return temperatura_celsius

# Função para plotar o gráfico de temperatura
def plotar_grafico(temperaturas, intervalos):
    plt.plot(intervalos, temperaturas, label='Temperatura da CPU (°C)')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Temperatura (°C)')
    plt.title('Monitoramento de Temperatura da CPU')
    plt.legend()
    plt.grid(True)
    plt.show()

# Função para salvar dados em um arquivo CSV
def salvar_dados_csv(intervalos, temperaturas, arquivo='temperatura_cpu.csv'):
    with open(arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Tempo (s)', 'Temperatura (°C)'])  # Cabeçalho
        for intervalo, temperatura in zip(intervalos, temperaturas):
            writer.writerow([intervalo, temperatura])

# Função principal do monitoramento
def monitorar_temperatura_cpu(duracao=60, intervalo=5):
    temperaturas = []
    intervalos = []
    tempo_inicial = time.time()

    while time.time() - tempo_inicial < duracao:
        temperatura = ler_temperatura_cpu()
        temperaturas.append(temperatura)
        tempo_corrente = time.time() - tempo_inicial
        intervalos.append(tempo_corrente)

        print(f"Temperatura da CPU atual: {temperatura:.2f} °C")
        time.sleep(intervalo)

    # Salvar dados em CSV
    salvar_dados_csv(intervalos, temperaturas)
    
    # Plotar gráfico
    plotar_grafico(temperaturas, intervalos)

if __name__ == "__main__":
    duracao_monitoramento = 60  # Tempo de monitoramento em segundos
    intervalo_leitura = 5  # Intervalo entre leituras em segundos
    monitorar_temperatura_cpu(duracao_monitoramento, intervalo_leitura)
