![analytics image (flat)](https://raw.githubusercontent.com/vitr/google-analytics-beacon/master/static/badge-flat.gif)
![analytics](https://www.google-analytics.com/collect?v=1&cid=555&t=pageview&ec=repo&ea=open&dp=/red_basica/readme&dt=&tid=UA-4677001-16)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EL-BID_red_basica&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EL-BID_red_basica)
---
[![en](https://img.shields.io/badge/lang-en-green.svg)](README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](README.pt.md)
[![es](https://img.shields.io/badge/lang-es-green.svg)](README.es.md)

# Apresentação

O saniHUB RedBasica é um software livre que tem como objetivo auxiliar no traçado e dimensionamento redes coletoras de esgoto, com ferramentas para projeto de sistemas do tipo condominial. Funciona como um complemento (Plug-in) para o software livre QGIS, de Sistema de Informações Geográficas.

Em Setembro de 2021 foi lançada a versão 1.0 do plugin, que é suportado pelas versões do QGIS 3 em diante, mas recomenda-se utilizar sempre com a versão estável (LTR) atual, que pode ser consultada no site: [https://qgis.org/en/site/](https://qgis.org/en/site/). A versão 1.0 marca o fim da necessidade da utilização da planilha de dimensionamento baseada em Excel fornecida anteriormente, todos os cálculos nela realizados foram trazidos para uma aplicação dentro do próprio QGIS, o que torna o software 100% livre e de código aberto além de uma maior praticidade durante as etapas do projeto. Importante dizer que as funcionalidades de exportar a rede traçada para um arquivo .csv continuam no saniHUB RedBasica, o que permite que os usuários que prefiram, continuem utilizando a [planilha](https://github.com/sanihub/red_basica/blob/dev/saniBID_RedBasica_Planilha_Dimensionamento_PT_v191020.xlsm) de dimensionamento fornecida ou até mesmo uma planilha própria.

O software foi desenvolvido originalmente para o Banco Interamericano de Desarrollo (BID), da Agencia Española de Cooperación Internacional para el Desarrollo (AECID) e a Latin America Investment Facility – European Union (LAIF) com a finalidade educativa e de promover o livre acesso a ferramentas modernas para o projeto de sistemas de esgoto e com funcionalidades adaptadas para o projeto de sistemas de esgoto do tipo condominial.

# Funcionalidades

O complemento mescla funções básicas já presentes no QGIS (ferramentas de desenho, georreferenciamento, dentre outras) com outras funcionalidades criadas com a finalidade de facilitar e automatizar o projeto de uma rede coletora de esgoto.

As ferramentas adicionadas ao QGIS pelo complemento são:

- Criação de camadas vetoriais (shapes) pré-configuradas para elaboração do projeto;
- Nomeação dos coletores;
- Vinculação entre as camadas vetoriais e seus atributos;
- Estilos e rótulos personalizados para cada camada;
- Checagem de eventuais inconsistências do projeto;
- Janelas de exibição dos atributos do trecho selecionado e outras informações do projeto;
- Ferramenta de cálculos e dimensionamento das redes coletoras de esgoto diretamente dentro do QGIS, com todos os parâmetros de cálculos editáveis;
- Importação dos resultados do cálculo hidráulico realizado de volta para o traçado no QGIS;
- Exportação dos resultados da rede dimensionada para o software EPA SWMM;
- Exibição do resultado do dimensionamento na planta de projeto;
- Possibilidade de exportação de dados do traçado para cálculo hidráulico em outras planilhas ou softwares externos e posterior importação do resultado;

O vínculo entre os módulos do QGIS e a aplicação de cálculos é feita de maneira simplificada utilizando as ferramentas do plugin, caso o usuário queira exportar para o uso externo (planilha ou software), isso é feito a partir das funções de exportação e importação de arquivo de texto separados por vírgula (“.csv”) contendo informações básicas para o dimensionamento, como: nomeação dos coletores, nomeação dos trechos, extensão de cada trecho, tipologia do traçado, cotas do terrenos, anotações auxiliares feitas pelo usuário durante o projeto, etc.

Tanto a aplicação de cálculos interna quanto a planilha de cálculo fornecida (RedBasica) está baseada na norma brasileira de “Projeto de redes coletoras de esgoto sanitário” (NBR 9649), incluindo o cálculo de tensão trativa. Os parâmetros de cálculo, contudo, podem ser ajustados livremente pelo usuário às características locais.

# Instalação do Complemento

Para a instalação do complemento saniHUB RedBasica o usuário deve:

1. Descarregar o arquivo disponibilizado no [LINK](https://github.com/sanihub/red_basica/archive/refs/heads/dev.zip);
2. Utilizando o QGIS Versão 3.0 ou superior abrir o menu **Complementos > Instalar Complementos** e escolher a opção **Install from Zip** e informar o local onde se encontra o instalador no seu computador, conforme a figura:
   ![Instalação do Complemento](https://raw.githubusercontent.com/leonazareth/sanibid_redbasica/refs/heads/master/Images/01%20Manual_Instalacao_Complemento_4.jpg)

# Tutoriais, cursos e manuais

Atualmente o manual completo para a versão 1.0 contendo a aplicação de cálculos no QGIS está em desenvolvimento, além disso existe um curso disponibilizado através do [canal do Youtube](https://www.youtube.com/playlist?list=PL1UvLzB7MU_YAU45sXd9zy0UOV3_hkMPH) com tradução para Inglês, Espanhol e Francês, que também está sendo atualizado para incluir as novas funcionalidades.

# Lista de Atributos

O usuário pode escolher entre utilizar uma camada vetorial já existente (com um traçado de rede já feito) ou inserir uma nova e realizar seu traçado utilizando as ferramentas de desenho do QGIS.

Os atributos padrão utilizados pelo plugin estão listados com suas respectivas funções a seguir.

### Atributos da camada vetorial de trechos

| Nome           | Descrição                                                                 | Tipo    | Tamanho | Precisão | Unidade |
|----------------|---------------------------------------------------------------------------|---------|---------|----------|---------|
| `aux_pav_1`      | Tipo de pavimento da rua (ex: asfalto = 1; paralelepípedo = 2; bloco de concreto = 3) | string  | 10      | -        | -       |
| `aux_pav_2`      | Tipo de pavimento da calçada, mesma lógica do pavimento rua              | string  | 10      | -        | -       |
| `aux_pos`        | Anotação de posição preferencial do trecho (0 = rua, 1 = calçada)        | string  | 10      | -        | -       |
| `aux_Prof_f`     | Auxílio de profundidade exigida no ponto de jusante do trecho atual (por interferência ou outro fator) | string  | 80      | -        | -       |
| `aux_Prof_i`     | Auxílio de profundidade exigida no ponto de montante do trecho atual (por interferência ou outro fator) | string  | 80      | -        | -       |
| `aux01`          | auxiliar genérico                                                          | string  | 10      | -        | -       |
| `aux02`          | auxiliar genérico                                                          | string  | 10      | -        | -       |
| `aux03`          | auxiliar genérico                                                          | string  | 10      | -        | -       |
| `Caida_p2`       | Dispositivo de queda no ponto de jusante do trecho                        | string  | 80      | -        | -       |
| `Caida_p2_h`     | Altura do dispositivo de queda no ponto de jusante do trecho              | string  | 80      | -        | m       |
| `DN`             | Diâmetro nominal do coletor                                              | string  | 80      | -        | mm      |
| `h_col_p1`       | Profundidade do coletor no ponto de montante (inicial) do trecho          | string  | 80      | -        | m       |
| `h_col_p2`       | Profundidade do coletor no ponto de jusante (final) do trecho             | string  | 80      | -        | m       |
| `h_tap_p1`       | Profundidade da camada de cobertura do coletor no ponto de montante (inicial) do trecho | string  | 80      | -        | m       |
| `h_tap_p2`       | Profundidade da camada de cobertura do coletor no ponto de jusante (final) do trecho | string  | 80      | -        | m       |
| `Id_Col`         | Nome do coletor                                                           | string  | 10      | -        | -       |
| `Id _TRM(n)`     | Nome do trecho do coletor (nome e número do trecho atual)                 | string  | 10      | -        | -       |
| `L`              | Extensão do trecho                                                        | real    | 10      | 2        | m       |
| `LABEL_VIS`      | Auxílio visibilidade rótulos (1 = visível, 0 = oculto)                   | integer | -       | -        | -       |
| `LABEL_X`        | Auxílio coordenada X rótulo                                               | real    | 10      | 6        | m       |
| `LABEL_Y`        | Auxílio coordenada Y rótulo                                               | real    | 10      | 6        | m       |
| `Mat_col`        | Material da tubulação                                                     | string  | 80      | -        | -       |
| `n`              | Coeficiente de Manning do trecho                                          | string  | 80      | -        | -       |
| `Q_f`            | Vazão de final de plano adotada do trecho                                 | string  | 80      | -        | l/s     |
| `Q_i`            | Vazão de início de plano adotada do trecho                                | string  | 80      | -        | l/s     |
| `Qt_f`           | Vazão de contribuição do trecho no final do plano                         | string  | 80      | -        | l/s     |
| `Qt_i`           | Vazão de contribuição do trecho no início do plano                        | string  | 80      | -        | l/s     |
| `S`              | Declividade da tubulação                                                  | string  | 80      | -        | m/m     |
| `Trativa_f`      | Tensão trativa no final de plano do trecho                                | string  | 80      | -        | Pa      |
| `Trativa_i`      | Tensão trativa no início de plano do trecho                               | string  | 80      | -        | Pa      |
| `V_f`            | Velocidade de escoamento no final do plano                                | string  | 80      | -        | m/s     |
| `V_i`            | Velocidade de escoamento no início do plano                               | string  | 80      | -        | m/s     |
| `Vc`             | Velocidade crítica de escoamento no final do plano                        | string  | 80      | -        | m/s     |
| `X_f`            | Coordenada X no ponto final do trecho (jusante)                           | real    | 10      | 6        | m       |
| `X_i`            | Coordenada X no ponto inicial do trecho (montante)                       | real    | 10      | 6        | m       |
| `Y_f`            | Coordenada Y no ponto final do trecho (jusante)                           | real    | 10      | 6        | m       |
| `Y_i`           | Coordenada Y no ponto inicial do trecho (montante)                       | real    | 10      | 6        | m       |
| `yn_f`           | Lâmina líquida no coletor - final de plano                                | string  | 80      | -        | m       |
| `yn_i`           | Lâmina líquida no coletor - início de plano                               | string  | 80      | -        | m       |
| `yrel_f`         | Lâmina líquida relativa no coletor - final de plano                       | string  | 80      | -        | %       |
| `yrel_i`         | Lâmina líquida relativa no coletor - início de plano                      | string  | 80      | -        | %       |

### Atributos da camada vetorial de dispositivos de inspeção (nós):

| Nome do Atributo    | Descrição                                               | Tipo   | Tamaño | Precisión | Unidad |
|---------------------|---------------------------------------------------------|--------|--------|-----------|--------|
| `aux_Altura`        | Altura del nodo.                                        | string | 80     | -         | m      |
| `aux_Cota`          | Cota del nodo.                                          | string | 80     | -         | m      |
| `aux_Diametro`      | Diámetro del nodo.                                      | string | 80     | -         | mm     |
| `aux_Material`      | Material del nodo.                                      | string | 80     | -         | -      |
| `aux_Profundidad`   | Profundidad del nodo.                                   | string | 80     | -         | m      |
| `aux_Tipo`          | Tipo de nodo (por ejemplo, pozo de visita, cámara de inspección). | string | 80     | -         | -      |
| `Id_Nodo`           | Identificador único del nodo.                           | string | 10     | -         | -      |
| `X`                 | Coordenada X del nodo.                                  | real   | 10     | 6         | m      |
| `Y`                 | Coordenada Y del nodo.                                  | real   | 10     | 6         | m      |
| `Z`                 | Coordenada Z del nodo (elevación).                      | real   | 10     | 6         | m      |

### Atributos da camada vetorial de unidades de contribuição:

| Nombre  | Descrição                                          | Tipo   | Tamanho | Precisção | Unidade |
|---------|----------------------------------------------------|--------|---------|-----------|---------|
| `Id_UC` | Identificação da quadra contribuinte (manzana)    | string | 10      | -         | -       |
| `Qe_ip` | Número de casas contribuintes inicio de plano      | integer| 10      | -         | un      |
| `Qe_fp` | Número de casas contribuintes final de plano       | integer| 10      | -         | un      |



# Colaboradores

- **Analista de Conceito**: Leonardo Porto Nazareth
- **Coordenação de Desenvolvimento**: Marta Fernandez
- **Desenvolvedores**: Martin Dell' Oro e Federico Sanchez
- **Cálculos e Modelagem Hidráulica**: Leonardo Porto Nazareth e Pery Nazareth

# Licença

O saniHUB RedBasica é um software Copyleft. Possui código-fonte livre para atualizações e melhorias, assegurando, porém, que os produtos derivados da versão aqui disponível estejam licenciados sob termos idênticos, sendo vetada qualquer tipo de comercialização dos mesmos. Termos de Licença: GNU GPLv3

Para mais detalhes acesse o link de [LICENÇA](https://github.com/leonazareth/sanibid_redbasica/blob/master/LICENSE) do plugin.

# Dúvidas e Sugestões

Qualquer dúvida, sugestão ou para reportar algum problema encontrado podem ser enviados para o e-mail: leonazareth@gmail.com

# Como Contribuir?

Se você tiver interesse em contribuir com o desenvolvimento do plugin, entre em contato pelo email: leonazareth@gmail.com