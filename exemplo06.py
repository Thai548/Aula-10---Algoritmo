# Calcula média de notas
#Não sabemos quantos, mas todos terão 4 notas sempre

def calcula_media(lista_notas):
    tot = sum(lista_notas)   # Função soma do python
    med = tot / len(lista_notas)
    return tot, med 

 
contador = 1 
#resposta = 'S'
while True:
    print(f'Aluno {contador}')
    aluno = input('Nome do Aluno: ')

    notas = []
    try:
        for i in range(4):
            nota= float (input('Informe a nota: '))
            notas.append(nota)
    except ValueError:
        print('Erro: Informe apenas valores válidos!')
    else:
        total, media = calcula_media(notas)

        print('\nResultado')
        print(f'Aluno: {aluno}')
        print(f'Total de pontos: {total}')
        print(f'Média: {media:.2f}')

    finally:
        print('Processo encerrado para o aluno')

# Causa de parada do loop
    opcao = input('Deseja calcular outro aluno ? ').strip().upper()  #A resposta automáticamente sairá em Maiúsculo
    if opcao != 'S':       # Se respostaa for diferente de sim ...
        break

    contador += 1 
print ('\nPrograma Encerradp')

    
    
    
     

