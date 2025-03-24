![analytics image (flat)](https://raw.githubusercontent.com/vitr/google-analytics-beacon/master/static/badge-flat.gif)
![analytics](https://www.google-analytics.com/collect?v=1&cid=555&t=pageview&ec=repo&ea=open&dp=/red_basica/readme&dt=&tid=UA-4677001-16)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EL-BID_red_basica&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EL-BID_red_basica)

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
	<META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=utf-8">
	<META NAME="GENERATOR" CONTENT="LibreOffice 4.1.6.2 (Linux)">
	<META NAME="AUTHOR" CONTENT="LeoNazareth">
	<META NAME="CREATED" CONTENT="20160913;140200000000000">
	<META NAME="CHANGEDBY" CONTENT="LeoNazareth">
	<META NAME="CHANGED" CONTENT="20160916;123300000000000">
	<META NAME="AppVersion" CONTENT="14.0000">
	<META NAME="DocSecurity" CONTENT="0">
	<META NAME="HyperlinksChanged" CONTENT="false">
	<META NAME="LinksUpToDate" CONTENT="false">
	<META NAME="ScaleCrop" CONTENT="false">
	<META NAME="ShareDoc" CONTENT="false">
</HEAD>

<img src="https://sanihub.org/themes/custom/sanibid/logo.png"></P>


<BODY LANG="pt-BR" DIR="LTR">
<H1 CLASS="western">Apresentação</H1>
<P STYLE="margin-bottom: 0.14in"><BR><BR>
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
<FONT COLOR="#000000">
O saniHUB RedBasica  é um software livre que tem como objetivo auxiliar no traçado 
e dimensionamento redes coletoras de esgoto, com ferramentas para projeto de sistemas do tipo condominial. 
Funciona como um complemento (Plug-in) para o software livre QGIS, de Sistema de Informações Geográficas.</P>
	
Em Setembro de 2021 foi lançada a versão 1.0 do plugin, que é suportado pelas versões do QGIS 3 em diante, mas recomenda-se utilizar sempre com a versão estável (LTR) atual, que pode ser consultada no site: https://qgis.org/en/site/. A versão 1.0 marca o fim da necessidade da utilização da planilha de dimensionamento baseada em Excel fornecida anteriormente, todos os cálculos nela realizados foram trazidos para uma aplicação dentro do próprio QGIS, o que torna o software 100% livre e de código aberto além de uma maior praticidade durante as etapas do projeto. Importante dizer que as funcionalidades de exportar a rede traçada para um arquivo .csv continuam no saniHUB RedBasica, o que permite que os usuários que prefiram, continuem utilizando a <a href="https://github.com/sanihub/red_basica/blob/dev/saniBID_RedBasica_Planilha_Dimensionamento_PT_v191020.xlsm">planilha</a> de dimensionamento fornecida ou até mesmo uma planilha prória. </P>
	
O software foi desenvolvido originalmente para o Banco Interamericano de Desarrollo (BID), da Agencia Española de 
Cooperación Internacional para el Desarrollo (AECID) e a Latin America Investment Facility – European Union (LAIF) 
com a finalidade educativa e de promover o livre acesso a ferramentas modernas para o projeto de sistemas de esgoto 
e com funcionalidades adaptadas para o projeto de sistemas de esgoto do tipo condominial. </P>

<H1 CLASS="western" STYLE="line-height: 150%; page-break-before: always">
Funcionalidades</H1>
<P STYLE="margin-bottom: 0.14in; line-height: 150%"><BR><BR>
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
O complemento mescla funções básicas já presentes no QGIS
(ferramentas de desenho, georreferenciamento, dentre outras) com
outras funcionalidades criadas com a finalidade de facilitar e
automatizar o projeto de uma rede coletora de esgoto.</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
As ferramentas adicionadas ao QGIS pelo complemento são:</P>
<UL>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Criação de
	camadas vetoriais (shapes) pré-configuradas para elaboração do
	projeto;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Nomeação
	dos coletores;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Vinculação
	entre as camadas vetoriais e seus atributos;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Estilos e
	rótulos personalizados para cada camada;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Checagem de
	eventuais inconsistências do projeto;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Janelas de
	exibição dos atributos do trecho selecionado e outras informações
	do projeto;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Ferramenta de
	cálculos e dimensionamento das redes coletoras de esgoto diretamente
	dentro do QGIS, com todos os parâmetros de cálculos editáveis;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Importação
	dos resultados do cálculo hidráulico realizado de volta para o 
	traçado no QGIS;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Exportação
	dos resultados da rede dimensionada para o software EPA SWMM;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Exibição
	do resultado do dimensionamento na planta de projeto;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%"> Possibilidade de
	exportação de dados do traçado para cálculo hidráulico em outras
	planilhas ou softwares externos e posterior importação do resultado;</P>
</UL>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
O vínculo entre os módulos do QGIS e a aplicação de cálculos é feita de maneira simplificada
utilizando as ferramentas do plugin, caso o usuário queira exportar para o uso externo
(planilha ou software), isso é feito a partir das funções de exportação e importação de arquivo 
de texto separados por vírgula (“.csv”) contendo informações básicas para o dimensionamento, 
como: nomeação dos coletores, nomeação dos trechos, extensão de cada trecho,tipologia do traçado, 
cotas do terrenos, anotações auxiliares feitas pelo usuário durante o projeto, etc. </P>

Tanto a aplicação de cálculos interna quanto a planilha de cálculo fornecida (RedBasica) está baseada na norma brasileira de “Projeto de
redes coletoras de esgoto sanitário” (NBR 9649), incluindo o cálculo de tensão trativa. 
Os parâmetros de cálculo, contudo, podem ser ajustados livremente pelo usuário às 
características locais.</P>

<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
<BR><BR>
</P>
<H1 CLASS="western" STYLE="line-height: 150%">Instalação do Complemento</H1>
<P STYLE="margin-bottom: 0.14in; line-height: 150%"><BR><BR>
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
Para a instalação do complemento saniHUB RedBasica o usuário deve:</P> 

<UL>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Descarregar o arquivo 
 disponibilizado no <a href="https://github.com/sanihub/red_basica/archive/refs/heads/dev.zip">LINK</a>;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Utilizando o QGIS
  Versão 3.0 ou superior abrir o menu <b>Complementos>Instalar Complementos</b> e escolher a opção 
  <b>Install from Zip</b> e informar o local onde se encontra o instalador no seu computador, conforme a figura;</P> <img src="https://raw.githubusercontent.com/leonazareth/sanibid_redbasica/refs/heads/master/Images/01%20Manual_Instalacao_Complemento_4.jpg" width=60% height=60%>

</P>
<H1 CLASS="western" STYLE="line-height: 150%">Tutoriais, cursos e manuais</H1>
<P STYLE="margin-bottom: 0.14in; line-height: 150%"><BR><BR>
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
Atualmente o manual completo para a versão 1.0 contendo a aplicação de cálculos no QGIS está em desenvolvimento,
além disso existe um curso disponibilizado através do <a href="https://www.youtube.com/playlist?list=PL1UvLzB7MU_YAU45sXd9zy0UOV3_hkMPH">canal do Youtube</a>
com tradução para Inglês, Espanhol e Francês, que também está sendo atualizado para incluir as novas funcionalidades.

<H1 CLASS="western" STYLE="line-height: 150%">Lista de Atributos</H1>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
<BR><BR>
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
O usuário pode escolher entre utilizar uma camada vetorial já
existente (com um traçado de rede já feito) ou inserir uma nova e
realizar seu traçado utilizando as ferramentas de desenho do QGIS. 
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
Os atributos padrão utilizados pelo plugin
estão listados com suas respectivas funções a seguir.</P>
<P STYLE="text-indent: -0.79in; margin-bottom: 0.14in; line-height: 150%">
Atributos da camada vetorial de trechos:</P>
<table>
  <thead>
    <tr>
      <th>Nome</th>
      <th>Descrição</th>
      <th>Tipo</th>
      <th>Tamanho</th>
      <th>Precisão</th>
      <th>Unidade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>aux_pav_1</td>
      <td>Tipo de pavimento da rua (ex: asfalto = 1; paralelepípedo = 2; bloco de concreto = 3)</td>
      <td>string</td>
      <td>10</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>aux_pav_2</td>
      <td>Tipo de pavimento da calçada, mesma lógica do pavimento rua</td>
      <td>string</td>
      <td>10</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>aux_pos</td>
      <td>Anotação de posição preferencial do trecho (0 = rua, 1 = calçada)</td>
      <td>string</td>
      <td>10</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>aux_Prof_f</td>
      <td>Auxílio de profundidade exigida no ponto de jusante do trecho atual (por interferência ou outro fator)</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>aux_Prof_i</td>
      <td>Auxílio de profundidade exigida no ponto de montante do trecho atual (por interferência ou outro fator)</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>aux01</td>
      <td>auxiliar genérico</td>
      <td>string</td>
      <td>10</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>aux02</td>
      <td>auxiliar genérico</td>
      <td>string</td>
      <td>10</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>aux03</td>
      <td>auxiliar genérico</td>
      <td>string</td>
      <td>10</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Caida_p2</td>
      <td>Dispositivo de queda no ponto de jusante do trecho</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Caida_p2_h</td>
      <td>Altura do dispositivo de queda no ponto de jusante do trecho</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m</td>
    </tr>
    <tr>
      <td>DN</td>
      <td>Diâmetro nominal do coletor</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>mm</td>
    </tr>
    <tr>
      <td>h_col_p1</td>
      <td>Profundidade do coletor no ponto de montante (inicial) do trecho</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m</td>
    </tr>
    <tr>
      <td>h_col_p2</td>
      <td>Profundidade do coletor no ponto de jusante (final) do trecho</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m</td>
    </tr>
    <tr>
      <td>h_tap_p1</td>
      <td>Profundidade da camada de cobertura do coletor no ponto de montante (inicial) do trecho</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m</td>
    </tr>
    <tr>
      <td>h_tap_p2</td>
      <td>Profundidade da camada de cobertura do coletor no ponto de jusante (final) do trecho</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m</td>
    </tr>
    <tr>
      <td>Id_Col</td>
      <td>Nome do coletor</td>
      <td>string</td>
      <td>10</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Id <em>TRM</em>(n) </td>
      <td>Nome do trecho do coletor (nome e número do trecho atual)</td>
      <td>string</td>
      <td>10</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>L</td>
      <td>Extensão do trecho</td>
      <td>real</td>
      <td>10</td>
      <td>2</td>
      <td>m</td>
    </tr>
    <tr>
      <td>LABEL_VIS</td>
      <td>Auxílio visibilidade rótulos (1 = visível, 0 = oculto)</td>
      <td>inteiro</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>LABEL_X</td>
      <td>Auxílio coordenada X rótulo</td>
      <td>real</td>
      <td>10</td>
      <td>6</td>
      <td>m</td>
    </tr>
    <tr>
      <td>LABEL_Y</td>
      <td>Auxílio coordenada Y rótulo</td>
      <td>real</td>
      <td>10</td>
      <td>6</td>
      <td>m</td>
    </tr>
    <tr>
      <td>Mat_col</td>
      <td>Material da tubulação</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>n</td>
      <td>Coeficiente de Manning do trecho</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Q_f</td>
      <td>Vazão de final de plano adotada do trecho</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>l/s</td>
    </tr>
    <tr>
      <td>Q_i</td>
      <td>Vazão de início de plano adotada do trecho</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>l/s</td>
    </tr>
    <tr>
      <td>Qt_f</td>
      <td>Vazão de contribuição do trecho no final do plano</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>l/s</td>
    </tr>
    <tr>
      <td>Qt_i</td>
      <td>Vazão de contribuição do trecho no início do plano</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>l/s</td>
    </tr>
    <tr>
      <td>S</td>
      <td>Declividade da tubulação</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m/m</td>
    </tr>
    <tr>
      <td>Trativa_f</td>
      <td>Tensão trativa no final de plano do trecho</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>Pa</td>
    </tr>
    <tr>
      <td>Trativa_i</td>
      <td>Tensão trativa no início de plano do trecho</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>Pa</td>
    </tr>
    <tr>
      <td>V_f</td>
      <td>Velocidade de escoamento no final do plano</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m/s</td>
    </tr>
    <tr>
      <td>V_i</td>
      <td>Velocidade de escoamento no início do plano</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m/s</td>
    </tr>
    <tr>
      <td>Vc</td>
      <td>Velocidade crítica de escoamento no final do plano</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m/s</td>
    </tr>
    <tr>
      <td>X_f</td>
      <td>Coordenada X no ponto final do trecho (jusante)</td>
      <td>real</td>
      <td>10</td>
      <td>6</td>
      <td>m</td>
    </tr>
    <tr>
      <td>X_i</td>
      <td>Coordenada X no ponto inicial do trecho (montante)</td>
      <td>real</td>
      <td>10</td>
      <td>6</td>
      <td>m</td>
    </tr>
    <tr>
      <td>Y_f</td>
      <td>Coordenada Y no ponto final do trecho (jusante)</td>
      <td>real</td>
      <td>10</td>
      <td>6</td>
      <td>m</td>
    </tr>
    <tr>
      <td>Y_i</td>
      <td>Coordenada Y no ponto inicial do trecho (montante)</td>
      <td>real</td>
      <td>10</td>
      <td>6</td>
      <td>m</td>
    </tr>
    <tr>
      <td>yn_f</td>
      <td>Lâmina líquida no coletor - final de plano</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m</td>
    </tr>
    <tr>
      <td>yn_i</td>
      <td>Lâmina líquida no coletor - início de plano</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m</td>
    </tr>
    <tr>
      <td>yrel_f</td>
      <td>Lâmina líquida relativa no coletor - final de plano</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>%</td>
    </tr>
    <tr>
      <td>yrel_i</td>
      <td>Lâmina líquida relativa no coletor - início de plano</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>%</td>
    </tr>
  </tbody>
</table>
Atributos da camada vetorial de dispositivos de inspeção (nós):</P>
<table>
  <thead>
    <tr>
      <th>Nome do Atributo</th>
      <th>Descrição</th>
      <th>Tipo</th>
      <th>Tamaño</th>
      <th>Precisión</th>
      <th>Unidad</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code>aux_Altura</code>
      </td>
      <td>Altura del nodo.</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m</td>
    </tr>
    <tr>
      <td>
        <code>aux_Cota</code>
      </td>
      <td>Cota del nodo.</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m</td>
    </tr>
    <tr>
      <td>
        <code>aux_Diametro</code>
      </td>
      <td>Diámetro del nodo.</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>mm</td>
    </tr>
    <tr>
      <td>
        <code>aux_Material</code>
      </td>
      <td>Material del nodo.</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>
        <code>aux_Profundidad</code>
      </td>
      <td>Profundidad del nodo.</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>m</td>
    </tr>
    <tr>
      <td>
        <code>aux_Tipo</code>
      </td>
      <td>Tipo de nodo (por ejemplo, pozo de visita, cámara de inspección).</td>
      <td>string</td>
      <td>80</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>
        <code>Id_Nodo</code>
      </td>
      <td>Identificador único del nodo.</td>
      <td>string</td>
      <td>10</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>
        <code>X</code>
      </td>
      <td>Coordenada X del nodo.</td>
      <td>real</td>
      <td>10</td>
      <td>6</td>
      <td>m</td>
    </tr>
    <tr>
      <td>
        <code>Y</code>
      </td>
      <td>Coordenada Y del nodo.</td>
      <td>real</td>
      <td>10</td>
      <td>6</td>
      <td>m</td>
    </tr>
    <tr>
      <td>
        <code>Z</code>
      </td>
      <td>Coordenada Z del nodo (elevación).</td>
      <td>real</td>
      <td>10</td>
      <td>6</td>
      <td>m</td>
    </tr>
  </tbody>
</table>
<P STYLE="text-indent: -0.79in; margin-bottom: 0.14in; line-height: 150%">
<table>
  <thead>
    <tr>
      <th>Nombre</th>
      <th>Descrição</th>
      <th>Tipo</th>
      <th>Tamanho</th>
      <th>Precisção</th>
      <th>Unidade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Id_UC</td>
      <td>Identificacao da quadra contribuinte (manzana)</td>
      <td>string</td>
      <td>10</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Qe_ip</td>
      <td>Número de casas contribuintes inicio de plano</td>
      <td>inteiro</td>
      <td>10</td>
      <td>-</td>
      <td>un</td>
    </tr>
    <tr>
      <td>Qe_fp</td>
      <td>Número de casas contribuintes final de plano</td>
      <td>inteiro</td>
      <td>-</td>
      <td>un</td>
    </tr>
  </tbody>
</table>
</P>


<H1 CLASS="western" STYLE="line-height: 150%; page-break-before: always">
Colaboradores</H1>
<P STYLE="margin-bottom: 0.14in; line-height: 150%"><BR><BR>
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
Analista de Conceito: Leonardo Porto Nazareth</P>
</P>
<P STYLE="margin-bottom: 0.14in"><BR><BR>
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
Coordenação de desenvolvimento: Marta Fedz</P>
</P>
<P STYLE="margin-bottom: 0.14in"><BR><BR>
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
Desenvolvedores: Martin Dell' Oro e Federico Sanchez</P>
</P>
<P STYLE="margin-bottom: 0.14in"><BR><BR>
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
Cálculos e modelagem hidráulica: Leonardo Porto Nazareth e Pery Nazareth</P>


<H1 CLASS="western" STYLE="line-height: 150%; page-break-before: always">
Licença</H1>
<P STYLE="margin-bottom: 0.14in; line-height: 150%"><BR><BR>

O saniHUB RedBasica é um software Copyleft. Possui código-fonte
livre para atualizações e melhorias, assegurando, porém, que os produtos
derivados da versão aqui disponível estejam licenciados sob
termos idênticos, sendo vetada qualquer tipo de comercialização dos
mesmos. Termos de Licença: GNU GPLv3

Para mais detalhes acesse o link de <a href="https://github.com/leonazareth/sanibid_redbasica/blob/master/LICENSE">LICENÇA</a> do plugin.

<H1 CLASS="western" STYLE="line-height: 150%; page-break-before: always">
Dúvidas e Sugestões</H1>
<P STYLE="margin-bottom: 0.14in; line-height: 150%"><BR><BR>
Qualquer dúvida, sugestão ou para reportar algum problema encontrado podem ser enviados para o e-mail: leonazareth@gmail.com

<H1 CLASS="western" STYLE="line-height: 150%; page-break-before: always">
Como Contribuir?</H1>
<P STYLE="margin-bottom: 0.14in; line-height: 150%"><BR><BR>
Se você tiver interesse em contribuir com o desenvolvimento do plugin, entre em contato pelo email: leonazareth@gmail.com
