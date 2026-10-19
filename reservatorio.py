from colorama import Fore, Style

# Lista armazenando os níveis e as situações do reservatório
niveis_reservatorio = [
    "Nível 1: Muito baixo (crítico)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito alto (alerta)"
]

def definir_cor_nivel(indice):
    """
    Função responsável por definir e retornar a cor da mensagem 
    conforme o nível informado (índice da lista).
    """
    if indice == 0:
        return Fore.RED
    elif indice == 1:
        return Fore.YELLOW
    elif indice == 2:
        return Fore.GREEN
    elif indice == 3:
        return Fore.CYAN
    elif indice == 4:
        return Fore.BLUE
    return Style.RESET_ALL

def simular_monitoramento():
    print("=== MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ===")
    
    # Exibe no terminal a situação atual de cada nível usando a lista e a função
    for i in range(len(niveis_reservatorio)):
        cor_escolhida = definir_cor_nivel(i)
        print(cor_escolhida + niveis_reservatorio[i])
        
    # Restaura o estilo padrão do terminal
    print(Style.RESET_ALL)

if __name__ == "__main__":
    simular_monitoramento()