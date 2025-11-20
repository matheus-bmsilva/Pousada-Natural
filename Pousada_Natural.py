# Atividade - Pousada
# Engenharia de Software - 1º B
# Pablo RGM 11251505821
# Matheus RGM 11252100741 

#bibliotecas  
import os
import locale
import Cores
from datetime import datetime
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#variável interativa  

tit='''
========================================================================
   ___                        __       _  __     __         ___       __
  / _ \___  __ _____ ___ ____/ /__ _  / |/ /__ _/ /___ __  / _ \___ _/ /
 / ___/ _ \/ // (_-</ _ `/ _  / _ `/ /    / _ `/ __/ // / / , _/ _ `/ / 
/_/   \___/\_,_/___/\_,_/\_,_/\_,_/ /_/|_/\_,_/\__/\_,_/ /_/|_|\_,_/_/  

========================================================================                                              
'''
def form():
    os.system("cls"),
    print(Cores.verde_negrito),
    print(tit),
    print(Cores.resetar)
reset="S"  
 

#tabela de preços  

simples=[20,28,35,42,48,53] 

duplex=[25,34,42,50,57,63]  

#loop  

while reset in ["S","s"]:  

    #validação de entrada  
    form()
    #tipo de apartamento 
    
    def validar_tipo():
        while True:
            tipo = input('🏢 - Informe o tipo de apartamento [Simples/Duplex]: ').capitalize().strip()
            if tipo in ["Simples", "Duplex", "simples", "duplex"]:
                return tipo
            else:
                print("\n❌ O apartamento deve ser [Simples] ou [Duplex]")
                input(f"{Cores.ITALIC}{Cores.vermelho_claro}Pressione Enter para tentar novamente...{Cores.resetar}")

    #Quantidade de pessoas
      
    def validar_pessoas():
        while True:
            try:
                person = int(input('👥 - Informe a quantidade de pessoas (1 a 6): '))
                if 1 <= person <= 6:
                    return person
                else:
                    print("❌ Informe um número válido de pessoas (1 a 6)")
            except ValueError:
                print("❌ Digite apenas números inteiros!")
                input(f"{Cores.ITALIC}{Cores.vermelho_claro}Pressione Enter para tentar novamente...{Cores.resetar}")

    #validação de quantidade de dias

    def validar_datas():
        formato_data = "%d/%m/%Y"
        while True:
            try:
                dia1 = input('📅 - Informe a data de entrada (dd/mm/aaaa): ')
                dia2 = input('📅 - Informe a data de saída (dd/mm/aaaa): ')
                conv1 = datetime.strptime(dia1, formato_data)
                conv2 = datetime.strptime(dia2, formato_data)
                if conv2 <= conv1:
                    print("❌ A data de saída deve ser depois da data de entrada!")
                    input(f"{Cores.ITALIC}{Cores.vermelho_claro}Pressione Enter para tentar novamente...{Cores.resetar}")
                else:
                    return conv1, conv2
            except ValueError:
                print("❌ A data deve estar no formato dd/mm/aaaa.")
                input(f"{Cores.ITALIC}{Cores.vermelho_claro}Pressione Enter para tentar novamente...{Cores.resetar}")
       
    #validação e processamento  
    
    tipo = validar_tipo()
    pessoas = validar_pessoas()
    entrada, saida = validar_datas()
    day = (saida - entrada).days
  
    if tipo in ['Simples', 'simples']:
        L1= simples[pessoas-1]
        valor= L1*day

    elif tipo in ['Duplex', 'duplex']:
        L2= duplex[pessoas-1]
        valor= L2*day



    #saída de dados  
    
    while True:  
        form()
        print(f'🏢 - Tipo de suíte:{tipo} \n'  
        f'👥 - Total de pessoas: {pessoas} \n'  
        f'📅 - Quantidade de dias: {day} \n'  
        f'💲 - Total a pagar: {locale.currency(valor)}\n'
        f'{Cores.verde_negrito}========================================================================{Cores.resetar}') 
        reset=input('📊 - Deseja fazer uma nova simulação de preço? \n' '(S/N)\n\n')
        if reset not in ["S", "N", "s", "n"]:  
           print(f'{Cores.ITALIC}{Cores.vermelho_claro}❌ Resposta inválida. É necessário inserir S ou N.{Cores.resetar}')  
        else:
            break     

os.system("cls")
print("\nFim do programa.")
input("Pressione Enter para finalizar..") 


 

 