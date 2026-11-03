Sistema de Monitoramento de Reservatório de Água

Um sistema simples de monitoramento de um reservatório de água executado no terminal. O sistema exibe mensagens de alerta com cores diferentes conforme o nível de água do reservatório, facilitando a visualização rápida da situação da capacidade de armazenamento.

🎯 Objetivo

Fornecer alertas visuais em tempo real sobre o estado do reservatório através de cores no terminal, permitindo identificar rapidamente situações críticas ou de alerta.

📋 Requisitos

    Python 3.6 ou superior
    Biblioteca colorama para cores no terminal

🚀 Instalação

    Clone ou baixe o arquivo do projeto
    Instale a dependência necessária:

bash

#pip install colorama

💻 Como Usar

Execute o script diretamente:

bash

#sistema_monitor.py

O sistema executará automaticamente:

    Simulação de monitoramento: passa por todos os 5 níveis sequencialmente
    Teste de níveis específicos: valida níveis válidos (1, 3, 5) e inválidos (0, 6)

📊 Níveis de Água e Cores

Nível	Descrição	Cor	Mensagem

1	Muito Baixo (Crítico)	🔴 Vermelho	Alerta crítico - Intervenção urgente

2	Baixo	🟡 Amarelo	Atenção - Monitorar próximas horas

3	Médio	🟢 Verde	Normal - Sistema funcionando adequadamente

4	Alto	🔵 Ciano	Situação sob controle

5	Muito Alto (Alerta)	🔷 Azul	Alerta - Risco de transbordamento

🏗️ Estrutura do Código

Dados

    niveis_agua: Lista com descrição de cada nível
    mensagens_alerta: Lista com mensagens correspondentes
    `cores: Lista com cores da biblioteca colorama

Funções

obter_cor_e_mensagem(nivel)

Retorna a cor, mensagem e descrição baseado no nível (1 a 5).

    Valida se o nível está entre 1 e 5
    Retorna erro se o nível for inválido

exibir_status_reservatorio(nivel)

Exibe o status formatado no terminal com:

    Descrição do nível
    
    Mensagem de alerta colorida
    Percentual de capacidade do reservatório

simular_monitoramento()

Simula o funcionamento do sistema passando por todos os 5 níveis sequencialmente.

testar_niveis_especificos()

Testa níveis válidos e inválidos para validar o sistema de validação.

📝 Exemplo de Saída

══════════════════════════════════════════════════════════════════

[Nível 3 - Médio]
✓ Nível de água normal. Sistema funcionando adequadamente.
Capacidade do reservatório: 60%

══════════════════════════════════════════════════════════════════

🔧 Características

✅ Validação de entrada: Rejeita níveis fora do intervalo 1-5

✅ Cores de terminal: Utiliza colorama para compatibilidade multiplataforma

✅ Sem entrada do usuário: Usa valores predefinidos para simulação

✅ Bem comentado: Código estruturado e fácil de entender

✅ Reset de estilos: Restaura o estilo padrão do terminal após cada mensagem
