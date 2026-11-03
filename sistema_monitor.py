# ============================================================================
# SISTEMA DE MONITORAMENTO DE NÍVEIS DE ÁGUA DO RESERVATÓRIO
# ============================================================================

from colorama import Fore, Back, Style, init

# Inicializa colorama para compatibilidade com diferentes sistemas
init(autoreset=True)

# ============================================================================
# ESTRUTURAS DE DADOS
# ============================================================================

# Descrição dos níveis
niveis_agua = [
    "Nível 1 - Muito Baixo (Crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito Alto (Alerta)"
]

# Mensagens de alerta para cada nível
mensagens_alerta = [
    " ALERTA CRÍTICO! Água em nível muito baixo. Intervenção urgente necessária!",
    " ATENÇÃO! Nível de água baixo. Monitorar próximas horas.",
    " Nível de água normal. Sistema funcionando adequadamente.",
    " Nível de água alto. Situação sob controle.",
    " ALERTA! Nível de água muito alto. Risco de transbordamento!"
]

# Cores correspondentes a cada nível
cores = [
    Fore.RED,      # Nível 1: Vermelho
    Fore.YELLOW,   # Nível 2: Amarelo
    Fore.GREEN,    # Nível 3: Verde
    Fore.CYAN,     # Nível 4: Ciano
    Fore.BLUE      # Nível 5: Azul
]

# ============================================================================
# FUNÇÕES
# ============================================================================

def obter_cor_e_mensagem(nivel):
    """Retorna cor e mensagem baseado no nível (1 a 5)."""
    
    if nivel < 1 or nivel > 5:
        return Fore.RED, " ERRO: Nível inválido!", "Nível desconhecido"
    
    indice = nivel - 1
    return cores[indice], mensagens_alerta[indice], niveis_agua[indice]


def exibir_status_reservatorio(nivel):
    """Exibe o status do reservatório com cor correspondente."""
    
    cor, mensagem, descricao = obter_cor_e_mensagem(nivel)
    percentual = (nivel / 5) * 100
    
    print("\n" + "=" * 70)
    print(cor + f"[{descricao}]" + Style.RESET_ALL)
    print(cor + mensagem + Style.RESET_ALL)
    print(f"Capacidade do reservatório: {percentual:.0f}%")
    print("=" * 70 + "\n")


def simular_monitoramento():
    """Simula o monitoramento passando por todos os 5 níveis."""
    
    print("\n═══════════════════════════════════════════════════════════════════")
    print("║        SISTEMA DE MONITORAMENTO DE RESERVATÓRIO DE ÁGUA          ║")
    print("═══════════════════════════════════════════════════════════════════\n")
    
    print("Iniciando simulação de monitoramento...\n")
    
    for nivel in range(1, 6):
        exibir_status_reservatorio(nivel)


def testar_niveis_especificos():
    """Testa níveis específicos incluindo valores inválidos."""
    
    print("\n═══════════════════════════════════════════════════════════════════")
    print("║               TESTE DE NÍVEIS ESPECÍFICOS                         ║")
    print("═══════════════════════════════════════════════════════════════════\n")
    
    niveis_teste = [1, 3, 5, 0, 6]
    
    print("Testando níveis: 1, 3, 5, 0 (inválido), 6 (inválido)\n")
    
    for nivel in niveis_teste:
        exibir_status_reservatorio(nivel)


# ============================================================================
# EXECUÇÃO PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    simular_monitoramento()
    print("\n" + "─" * 70 + "\n")
    testar_niveis_especificos()
    print("\n✓ Simulação concluída com sucesso!")
    print("✓ Todos os estilos foram restaurados para o padrão do terminal.\n")
