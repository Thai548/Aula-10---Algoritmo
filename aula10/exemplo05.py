
print(' === Cálculo de Produtividade ===')

try:  # try quer dizer TENTE
    total_produzido = float(input('Valor total da venda: '))
    funcionarios= int(input('Total de Funcionários: '))
    media_por_funcionario= total_produzido / funcionarios


except Exception as e:
    print(f'Ops! Erro nos valores de entrada {e}')
except KeyboardInterrupt:
    print('Operação cancelada pelo usuário')

else: # Se não der erro execute o else!
    print(f'Média por funcionário: {media_por_funcionario:.2f}')
finally:  # Pode executar sempre, com erro ou não para finalizar a consulta
    print('Programa encerrado!')