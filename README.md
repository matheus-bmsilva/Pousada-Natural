# Pousada Natural
🏨 Pousada Natural - Sistema de Simulação de Estadia
Este projeto consiste em um aplicativo em Python para simulação de custos de estadia em uma pousada, permitindo ao usuário calcular o valor total da hospedagem com base no tipo de apartamento, número de hóspedes e período de permanência.

✨ Funcionalidades
-Seleção do tipo de apartamento: Simples ou Duplex
-Cálculo personalizado: Valores variam de acordo com o número de pessoas (1 a 6)
-Cálculo de diárias: Com base nas datas de entrada e saída
-Interface amigável: Mensagens coloridas e validação robusta de entrada
-Experiência interativa: Possibilidade de realizar múltiplas simulações sem reiniciar o programa

🛠️ Tecnologias Utilizadas
Python 3
Módulos nativos:
-os para limpeza de terminal
-locale para formatação monetária
-datetime para manipulação de datas
-Sistema de cores personalizado (arquivo Cores.py)

📁 Estrutura do Projeto
text
Pousada_Natural/
├── Pousada_Natural.py    # Arquivo principal do sistema
├── Cores.py              # Módulo com definições de cores para terminal
└── README.md             # Documentação do projeto

🚀 Como Usar
1. Execute o script principal:

bash
python Pousada_Natural.py


2.Siga as instruções no terminal para:
-Escolher o tipo de apartamento
-Informar o número de hóspedes
-Inserir datas de entrada e saída

3.Visualize o resultado com o valor total formatado em Real brasileiro (R$)

💡 Destaques do Código
-Validação completa de entradas do usuário
-Tratamento de exceções para datas e números
-Interface visual organizada e profissional
-Código modularizado com funções específicas
