![analytics image (flat)](https://raw.githubusercontent.com/vitr/google-analytics-beacon/master/static/badge-flat.gif)
![analytics](https://www.google-analytics.com/collect?v=1&cid=555&t=pageview&ec=repo&ea=open&dp=/red_basica/readme&dt=&tid=UA-4677001-16)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EL-BID_red_basica&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EL-BID_red_basica)
---
[![en](https://img.shields.io/badge/lang-en-green.svg)](README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](README.pt.md)
[![es](https://img.shields.io/badge/lang-es-green.svg)](README.es.md)

# Apresentação

O saniHUB RedBasica é um software livre desenvolvido para apoiar o traçado e dimensionamento de redes coletoras de esgoto sanitário. Oferece ferramentas especializadas para o projeto de sistemas do tipo condominial. O software funciona como um plugin para o QGIS, um Sistema de Informação Geográfica (SIG) gratuito e poderoso.

Recomenda-se sempre utilizar a versão estável atual (LTR), que pode ser consultada no site: [https://qgis.org/en/site/](https://qgis.org/en/site/).

O software foi desenvolvido originalmente para o Banco Interamericano de Desenvolvimento (BID), a Agência Espanhola de Cooperação Internacional para o Desenvolvimento (AECID) e a Latin America Investment Facility – European Union (LAIF) com finalidade educativa e para promover o acesso livre a ferramentas modernas para projeto de redes coletoras de esgoto sanitário.

# Funcionalidades

O plugin aproveita uma grande quantidade de ferramentas essenciais já existentes no QGIS, como ferramentas de desenho, georreferenciamento, tabelas de atributos, entre outras, e adiciona funcionalidades para facilitar e automatizar o processo de projeto de redes coletoras de esgoto.

As ferramentas desenvolvidas pelo plugin incluem:

- Criação de camadas vetoriais pré-configuradas (trechos, nós,...) para o desenvolvimento do projeto;
- Nomeação dos coletores (manual ou automática);
- Vinculação entre camadas vetoriais e seus atributos;
- Estilos e rótulos personalizados para cada camada;
- Verificação de eventuais inconsistências do projeto;
- Janelas de exibição dos atributos do trecho selecionado e outras informações do projeto;
- Ferramenta para cálculos e dimensionamento de redes coletoras de esgoto diretamente no QGIS, com todos os parâmetros de cálculo editáveis;
- Importação dos resultados dos cálculos hidráulicos de volta para o layout do QGIS;
- Exportação dos resultados da rede dimensionada para o software EPA SWMM;
- Exibição do resultado do dimensionamento no layout do projeto;
- Visualização do perfil da rede projetada;
- Possibilidade de exportar dados de traçado para cálculos hidráulicos em outras planilhas ou softwares externos e posterior importação dos resultados.

A ligação entre os módulos do QGIS e a aplicação de cálculo é simplificada usando as ferramentas do plugin. Caso o usuário deseje exportar para uso externo (planilhas ou softwares), isso pode ser feito através das funções de exportação e importação de arquivos separados por vírgula (“.csv”), contendo informações básicas para dimensionamento, como: nomes dos coletores, nomes dos trechos, extensões dos trechos, tipologia do traçado, cotas do terreno, anotações auxiliares feitas pelo usuário durante o projeto, etc.

Tanto a aplicação de cálculo interna quanto a planilha de cálculo fornecida (RedBasica) estão baseadas na norma brasileira "Projeto de Redes Coletoras de Esgoto Sanitário" (NBR 9649), incluindo o cálculo de tensão trativa. Contudo, os parâmetros de cálculo podem ser livremente ajustados pelo usuário para se adequar às características locais.

# Instalação do Plugin

Para instalar o plugin saniHUB RedBasica, o usuário deve:

1. Baixar o arquivo disponível no [LINK](https://github.com/sanihub/red_basica/archive/refs/heads/dev.zip);
2. Utilizando o [QGIS LTR](https://qgis.org/download/), abrir o menu **Complementos > Gerenciar e Instalar Complementos**, selecionar a opção **Instalar do Zip** e especificar o local onde o instalador está localizado em seu computador, conforme mostrado na figura:
   ![Instalação do Plugin](https://raw.githubusercontent.com/leonazareth/sanibid_redbasica/refs/heads/master/Images/01%20Manual_Instalacao_Complemento_4.jpg)

# Tutoriais, Cursos e Manuais

Atualmente, o manual completo para a versão 1.0, que inclui a aplicação de cálculo no QGIS, está em desenvolvimento. Além disso, existe um curso disponível no [canal do YouTube](https://www.youtube.com/playlist?list=PL1UvLzB7MU_YAU45sXd9zy0UOV3_hkMPH) com traduções para Inglês, Espanhol e Francês. Este curso também está sendo atualizado para incluir novas funcionalidades.

# Lista de Atributos

O usuário pode escolher entre utilizar uma camada vetorial já existente (com uma rede já traçada) ou criar uma nova e traçá-la utilizando as ferramentas de desenho do QGIS.

Os atributos padrão utilizados pelo plugin estão listados abaixo com suas respectivas funções.

### Atributos da camada vetorial de trechos

| Nome          | Descrição                                                                                   | Tipo    | Tamanho | Precisão | Unidade |
|---------------|---------------------------------------------------------------------------------------------|---------|---------|----------|---------|
| `aux_pav_1`   | Tipo de pavimento da rua (ex: asfalto = 1; paralelepípedo = 2; bloco de concreto = 3)       | string  | 10      | -        | -       |
| `aux_pav_2`   | Tipo de pavimento da calçada, mesma lógica do pavimento rua                                | string  | 10      | -        | -       |
| `aux_pos`     | Anotação de posição preferencial do trecho (0 = rua, 1 = calçada)                          | string  | 10      | -        | -       |
| `aux_Prof_f`  | Auxilio de profundidade exigida no ponto de jusante do trecho atual                        | string  | 80      | -        | -       |
| `aux_Prof_i`  | Auxilio de profundidade exigida no ponto de montante do trecho atual                       | string  | 80      | -        | -       |
| `aux01`       | Auxiliar genérico                                                                           | string  | 10      | -        | -       |
| `aux02`       | Auxiliar genérico                                                                           | string  | 10      | -        | -       |
| `aux03`       | Auxiliar genérico                                                                           | string  | 10      | -        | -       |
| `Caida_p2`    | Dispositivo de queda no ponto de jusante do trecho                                          | string  | 80      | -        | -       |
| `Caida_p2_h`  | Altura do dispositivo de queda no ponto de jusante do trecho                               | string  | 80      | -        | m       |
| `DN`          | Diâmetro nominal do coletor                                                                | string  | 80      | -        | mm      |
| `h_col_p1`    | Profundidade do coletor no ponto de montante (inicial) do trecho                           | string  | 80      | -        | m       |
| `h_col_p2`    | Profundidade do coletor no ponto de jusante (final) do trecho                              | string  | 80      | -        | m       |
| `h_tap_p1`    | Profundidade da camada de cobertura do coletor no ponto de montante (inicial) do trecho    | string  | 80      | -        | m       |
| `h_tap_p2`    | Profundidade da camada de cobertura do coletor no ponto de jusante (final) do trecho       | string  | 80      | -        | m       |
| `Id_Col`      | Nome do coletor                                                                             | string  | 10      | -        | -       |
| `Id_TRM_(n)`  | Nome do trecho de coletor (nome e número do trecho atual)                                  | string  | 10      | -        | -       |
| `L`           | Extensão do trecho                                                                          | real    | 10      | 2        | m       |
| `LABEL_VIS`   | Auxílio visibilidade rótulos (1 = visível, 0 = oculto)                                      | inteiro | -       | -        | -       |
| `LABEL_X`     | Auxílio coordenada X rótulo                                                                | real    | 10      | 6        | m       |
| `LABEL_Y`     | Auxílio coordenada Y rótulo                                                                | real    | 10      | 6        | m       |
| `Mat_col`     | Material da tubulação                                                                      | string  | 80      | -        | -       |
| `n`           | Coeficiente de Manning do trecho                                                          | string  | 80      | -        | -       |
| `Q_f`         | Vazão de final de plano adotada do trecho                                                 | string  | 80      | -        | l/s     |
| `Q_i`         | Vazão de início de plano adotada do trecho                                                | string  | 80      | -        | l/s     |
| `Qmax_f`      | Vazão máxima de final de plano no trecho                                                  | string  | 80      | -        | l/s     |
| `Qmax_i`      | Vazão máxima de início de plano no trecho                                                 | string  | 80      | -        | l/s     |
| `Qmed_f`      | Vazão média de final de plano no trecho                                                   | string  | 80      | -        | l/s     |
| `Qmed_i`      | Vazão média de início de plano no trecho                                                  | string  | 80      | -        | l/s     |
| `Qr_f`        | Vazão de fim de plano recorrente projetada no trecho                                       | string  | 80      | -        | l/s     |
| `Qr_i`        | Vazão de início de plano recorrente projetada no trecho                                    | string  | 80      | -        | l/s     |
| `S`           | Declividade da tubulação                                                                  | string  | 80      | -        | m/m     |
| `Trativa_f`   | Tensão trativa no final de plano do trecho                                                | string  | 80      | -        | Pa      |
| `Trativa_i`   | Tensão trativa no início de plano do trecho                                               | string  | 80      | -        | Pa      |
| `V_f`         | Velocidade de escoamento no final do plano                                                | string  | 80      | -        | m/s     |
| `V_i`         | Velocidade de escoamento no final do plano                                                | string  | 80      | -        | m/s     |
| `Vc_f`        | Velocidade crítica de escoamento no final do plano                                        | string  | 80      | -        | m/s     |
| `Vc_i`        | Velocidade crítica de escoamento no início do plano                                       | string  | 80      | -        | m/s     |
| `X_f`         | Coordenada X no ponto final do trecho (jusante)                                           | real    | 10      | 6        | m       |
| `X_i`         | Coordenada X no ponto inicial do trecho (montante)                                        | real    | 10      | 6        | m       |
| `Y_f`         | Coordenada Y no ponto final do trecho (jusante)                                           | real    | 10      | 6        | m       |
| `Y_i`         | Coordenada Y no ponto inicial do trecho (montante)                                        | real    | 10      | 6        | m       |
| `yn_f`        | Lâmina líquida no coletor - final de plano                                                | string  | 80      | -        | m       |
| `yn_i`        | Lâmina líquida no coletor - início de plano                                               | string  | 80      | -        | m       |
| `yrel_f`      | Lâmina líquida relativa no coletor - final de plano                                        | string  | 80      | -        | %       |
| `yrel_i`      | Lâmina líquida relativa no coletor - início de plano                                       | string  | 80      | -        | %       |

### Atributos da camada vetorial de dispositivos de inspeção (nós)

| Nome           | Descrição                                                                                           | Tipo    | Tamanho | Precisão | Unidade |
|----------------|-----------------------------------------------------------------------------------------------------|---------|---------|----------|---------|
| `aux04`        | Auxiliar genérico                                                                                   | string  | 10      | -        | -       |
| `aux05`        | Auxiliar genérico                                                                                   | string  | 10      | -        | -       |
| `aux06`        | Auxiliar genérico                                                                                   | string  | 10      | -        | -       |
| `CF_nodo`      | Cota de fundo do dispositivo de inspeção                                                           | string  | 80      | -        | m       |
| `Citrd_nodo`   | Cota de intrados do nó                                                                             | string  | 80      | -        | m       |
| `CT_(N)`       | Cota do terreno no nó (inicial e final)                                                           | real    | 10      | 2        | m       |
| `h_nodo_NT`    | Profundidade do dispositivo de inspeção em relação ao nível do terreno                            | string  | 80      | -        | m       |
| `h_nodo_tp`    | Profundidade do dispositivo de inspeção em relação à sua tampa                                    | string  | 80      | -        | m       |
| `Id_NODO_(n)`  | Nome do nó (CI ou PV) atual                                                                       | string  | 80      | -        | -       |
| `Qi_cat`       | Vazão de fim de plano da área de influência originada de dados de vazão (cadastro de usuários)   | real    | 10      | 6        | l/s     |
| `Qf_cat`       | Vazão de fim de plano da área de influência originada de dados de vazão (cadastro de usuários)   | real    | 10      | 6        | l/s     |
| `Qi_con`       | Vazão de início de plano da área de influência originada de dados de conexões                   | real    | 10      | 6        | l/s     |
| `Qf_con`       | Vazão de fim de plano da área de influência originada de dados de conexões                      | real    | 10      | 6        | l/s     |
| `Qi_pop`       | Vazão de início de plano da área de influência originada de dados de população                  | real    | 10      | 6        | l/s     |
| `Qf_pop`       | Vazão de fim de plano da área de influência originada de dados de população                     | real    | 10      | 6        | l/s     |
| `Id_UC`        | Identificação da quadra contribuinte (manzana)                                                  | string  | 10      | -        | -       |
| `LABEL_VIS`    | Auxílio visibilidade rótulos (1 = visível, 0 = oculto)                                           | inteiro | 10      | -        | -       |
| `LABEL_X`      | Auxílio coordenada X rótulo                                                                      | real    | 10      | 6        | m       |
| `LABEL_Y`      | Auxílio coordenada Y rótulo                                                                      | real    | 10      | 6        | m       |
| `Nodo_tipo`    | Tipo e tamanho do dispositivo de inspeção                                                       | string  | 80      | -        | -       |
| `Tap_nodo`     | Profundidade da camada de cobertura do dispositivo de inspeção                                  | string  | 80      | -        | m       |
| `CF_NODO2`     | Cota do nó calculada pela estimativa de profundidade                                            | real    | 10      | 2        | m       |
| `H_NODO_TP2`   | Profundidade do nó calculada pela estimativa de profundidade                                    | real    | 10      | 2        | m       |


### Atributos da camada vetorial de unidades de contribuição

| Nome     | Descrição                                                      | Tipo    | Tamanho | Precisão | Unidade |
|----------|----------------------------------------------------------------|---------|---------|----------|---------|
| `Id_UC`  | Identificação da quadra contribuinte (manzana)                | string  | 10      | -        | -       |
| `Qe_ip`  | Número de casas contribuintes início de plano                | inteiro | 10      | -        | un      |
| `Qe_fp`  | Número de casas contribuintes final de plano                 | inteiro | 10      | -        | un      |
| `QConcI` | Vazão concentrada de início de plano                         | real    | 10      | 4        | l/s     |
| `QConcF` | Vazão concentrada de fim de plano                            | real    | 10      | 4        | l/s     |


# Como Contribuir?

Se você estiver interessado em contribuir para o desenvolvimento do plugin, entre em contato por e-mail: leonazareth@gmail.com
