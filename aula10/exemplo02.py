# Este for é pra usr quando tiver erro


for i in range(5):
    total_produzido = float(input('Valor total da venda: '))
    funcionarios= int(input('Total de Funcionários: '))


    media_por_funcionario= total_produzido / funcionarios
    print(f'Média por funcionário: {media_por_funcionario:.2f}')


#------------------------------#

# For com try: Não para de executar, se lança um erro

for i in range(5):
    try:  # try quer dizer TENTE
        total_produzido = float(input('Valor total da venda: '))
        funcionarios= int(input('Total de Funcionários: '))


        media_por_funcionario= total_produzido / funcionarios
        print(f'Média por funcionário: {media_por_funcionario:.2f}')
    except ValueError:
        print('Digite apenas números.')
    except ZeroDivisionError:
        print('Funcionário não pode ser Zero.')
