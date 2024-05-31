import pandas as pd
from scipy import stats

# Aqui eu coloquei os dados fornecidos na base de dados dos alunos. Integrei manualmente devido à uma dificuldade que tive em importar os dados do arquivo nessa IDE.
data_dict = {
    'Nota_Teste': [
        7.5, 8, 9, 7, 7.5, 6, 10, 7, 8, 8.5, 10, 9, 3, 7, 2, 4, 5, 3, 6, 5, 4, 2.5, 2, 2, 1.5, 5, 4, 8, 7, 8, 10, 7, 9, 7, 7.5, 8, 6, 8, 8, 8, 8, 7, 9, 7, 9, 7, 8, 9, 7, 8, 7.5
    ],
    'TipoEsc': [
        'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'pub', 'pub', 'pub', 'pub', 'pub', 'pub', 'pub', 'pub', 'pub', 'pub', 'pub', 'pub', 'pub', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'pub', 'pub', 'pub', 'pub', 'priv', 'priv', 'priv', 'pub'
    ]
}

data = pd.DataFrame(data_dict)

data['Nota_Teste'] = pd.to_numeric(data['Nota_Teste'], errors='coerce')
data['TipoEsc'] = data['TipoEsc'].astype('category')

print(data.head(50))

publica = data[data['TipoEsc'] == 'pub']['Nota_Teste']
privada = data[data['TipoEsc'] == 'priv']['Nota_Teste']

media_publica = publica.mean()
desvio_publica = publica.std()
min_publica = publica.min()
max_publica = publica.max()

media_privada = privada.mean()
desvio_privada = privada.std()
min_privada = privada.min()
max_privada = privada.max()

print(f'Escola Pública - Média: {media_publica:.2f}, Desvio Padrão: {desvio_publica:.2f}, Mínima: {min_publica:.2f}, Máxima: {max_publica:.2f}')
print(f'Escola Privada - Média: {media_privada:.2f}, Desvio Padrão: {desvio_privada:.2f}, Mínima: {min_privada:.2f}, Máxima: {max_privada:.2f}')

t_stat, p_value = stats.ttest_ind(publica, privada, equal_var=False) # equal_var=False para não assumir variâncias iguais

print(f'Testatística: {t_stat:.2f}, Valor-p: {p_value:.5f}')

alpha = 0.05
if p_value < alpha:
    print("Há uma diferença significativa nas médias das notas entre escolas públicas e privadas.")
else:
    print("Não há uma diferença significativa nas médias das notas entre escolas públicas e privadas.")
