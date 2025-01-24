# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps).
# Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input("Informe o tamanho do arquivo para download (em MB): "))
velocidade_internet = float(input("Informe a velocidade da Internet (em Mbps): "))

# Convertendo velocidade de Mbps para MBps (1 byte = 8 bits)
velocidade_em_MBps = velocidade_internet / 8

# Calculando o tempo de download em segundos e convertendo para minutos
tempo_download_em_segundos = tamanho_arquivo / velocidade_em_MBps
tempo_download_em_minutos = tempo_download_em_segundos / 60

# Exibindo o resultado com duas casas decimais
print(f"Tempo aproximado de download do arquivo: {tempo_download_em_minutos:.2f} minutos.")
