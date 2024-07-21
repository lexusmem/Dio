'''
Etapas processo ETL

Extract - Extração:

Identificação das fontes de dados: O primeiro passo é mapear todas as fontes de dados que serão utilizadas no processo, como bancos de dados, sistemas de CRM, ERP, arquivos em nuvem, APIs e feeds de dados.
Definição dos dados a serem extraídos: É crucial determinar quais dados específicos são necessários para atender aos objetivos do processo. Isso pode envolver consultas em SQL, APIs ou outras ferramentas de extração.
Estabelecimento de um cronograma de extração: Defina a frequência com que os dados serão extraídos das fontes de origem, considerando a taxa de atualização e a necessidade de dados em tempo real.
Implementação da extração: Utilize ferramentas ou scripts adequados para extrair os dados de cada fonte, garantindo fidelidade e segurança durante o processo.

Transform - Transformação:

Limpeza de dados: Corrija erros, inconsistências e duplicatas nos dados extraídos para garantir sua qualidade e confiabilidade.
Padronização de dados: Converta os dados para um formato comum, como datas, unidades e medidas, facilitando a integração e análise.
Enriquecimento de dados: Adicione informações complementares de outras fontes para ampliar o valor dos dados e torná-los mais úteis para análise.
Tratamento de dados ausentes: Lidar com valores ausentes de forma adequada, como imputação ou exclusão, para minimizar o impacto na análise.
Validação de dados: Verifique se os dados transformados estão consistentes com as regras de negócio e livres de erros.
Transformações complexas: Utilize funções e regras de negócio mais complexas para preparar os dados para a análise desejada, como cálculos, agregações e segmentações.

Load - Carregamento:

Escolha do destino: Defina o local onde os dados transformados serão armazenados, como um data warehouse, data lake ou outro repositório de dados.
Seleção do método de carregamento: Escolha o método de carregamento mais adequado, como carga total, carga incremental ou carga em tempo real, considerando o volume de dados e a frequência de atualização.
Implementação do carregamento: Utilize ferramentas ou scripts adequados para carregar os dados no destino escolhido, garantindo a integridade e confiabilidade do processo.
Gerenciamento de conflitos: Estabeleça regras para lidar com conflitos de dados, como duplicatas ou atualizações simultâneas, para garantir a consistência do repositório.
Verificação de carga: Valide se os dados foram carregados corretamente no destino e se estão de acordo com as expectativas.
'''

# Vantagens ETL
# garantia significativa de qualidade dos dados
# funcionalidade de exceção
# desenvolvimento das cargas
# manutenção das cargas
# metainformações
# performance
# transferência
# conectividade
# reinicialização
# segurança e estabilidade
