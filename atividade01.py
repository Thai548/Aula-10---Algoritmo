# Desenvolva um programa que simule um caixa eletronico
#O sistema deve iniciar com um saldo de R$1000,00 e solicitar ao usuário o valor que de deseja sacar.
#Após a tenativa de saque, exibe mensagens adequadas informando o resultado da operação e finalize o programa.

# * Utilize a estrutura de tratamentos de erros.

print(' === Caixa Eletrônico ===')

try:
    caixa = 1000
    valor_saque= float(input('Informe o valor que deseje sacar: '))
    
    saldo= caixa - valor_saque
    print (f'Saque efetuado! Saldo restante: {saldo}')

except KeyboardInterrupt:
    print('Operação cancelada pelo usuário')
except (ValueError, TypeError):
    print('Valor inválido.')


else: 
    if valor_saque > caixa:
        print('Saldo insuficiente')
    elif valor_saque <= 1:
        print ('Saque somente a partir de R$2.00')
    else:
        saldo -= valor_saque
        print('\n Saque realizado com sucesso')
        print (f'Saldo em conta R$ {saldo:.2f}')
        
finally:  
    print('Operação encerrada!')
