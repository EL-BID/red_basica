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

<img src="https://github.com/leonazareth/sanihub_redbasica/blob/master/Images/Logo%20SaniBID%20RB_v.02..png"></P>


<BODY LANG="pt-BR" DIR="LTR">
<H1 CLASS="western">Apresentação</H1>
<P STYLE="margin-bottom: 0.14in"><BR><BR>
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
<FONT COLOR="#000000">
O saniHUB RedBasica  é um software livre que tem como objetivo auxiliar no traçado 
e dimensionamento redes coletoras de esgoto, com ferramentas para projeto de sistemas do tipo condominial. 
Funciona como um complemento para o software de livre acesso QGIS, de Sistema de Informações Geográficas.</P>

Além do módulo livre, é fornecida uma <a href="https://github.com/leonazareth/sanihub_redbasica/blob/master/saniBID_RedBasica_Planilha_Dimensionamento_PT.xlsm">planilha</a> de cálculo hidráulico e dimensionamento, desenvolvida no software Excel.
Isso não impede o usuário de utilizar os dados exportados pelo QGIS para o dimensionamento em outra planilha ou software 
de sua preferência.</P>

O software foi desenvolvido originalmente para o Banco Interamericano de Desarrollo (BID), da Agencia Española de 
Cooperación Internacional para el Desarrollo (AECID) e a Latin America Investment Facility – European Union (LAIF) 
com a finalidade educativa e de promover o livre acesso a ferramentas modernas para o projeto de sistemas de esgoto 
e com funcionalidades adaptadas para o projeto de sistemas de esgoto do tipo condominial. </P>

Atualmente o plugin está na versão beta 0.9, é suportado pelo QGIS 3.0, ou mais recente, e a planilha 
fornecida funciona com Excel versão 2010 em diante, com sistema operacional Windows de 32 ou 64-bits. </P>
<P STYLE="margin-bottom: 0.14in"><BR><BR>

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
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Exportação
	de dados do traçado realizado para cálculo hidráulico em planilha
	especialmente elaborada com essa finalidade (ou outro tipo de
	software externo de cálculo hidráulico);</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Importação
	dos resultados do cálculo hidráulico realizado externamente  de
	volta para o projeto;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Exibição
	do resultado do dimensionamento na planta de projeto;</P>
</UL>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
O vínculo entre os módulos do QGIS e o modo de cálculos (planilha ou software) é feito a 
partir das funções de exportação e importação de arquivo de texto separados por vírgula 
(“.csv”) contendo informações básicas para o dimensionamento, como: nomeação dos
coletores, nomeação dos trechos, extensão de cada trecho,tipologia do traçado, 
cotas do terrenos, anotações auxiliares feitas pelo usuário durante o projeto, etc. </P>

A planilha de cálculo fornecida (RedBasica) está baseada na norma brasileira de “Projeto de
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
"saniBID_RedBasica-master.zip", disponibilizado no <a href="https://github.com/leonazareth/sanihub_redbasica/blob/master/saniBID_RedBasica-master.zip">LINK</a>;</P>
	<LI><P STYLE="margin-bottom: 0.14in; line-height: 150%">Utilizando o QGIS
  Versão 3.0 ou superior abrir o menu <b>Complementos>Instalar Complementos</b> e escolher a opção 
  <b>Install from Zip</b> e informar o local onde se encontra o instalador no seu computador, conforme a figura;</P> <img src="https://github.com/leonazareth/sanihub_redbasica/blob/master/Images/01%20Manual_Instalacao_Complemento_4.jpg" width=60% height=60%>

</P>
<H1 CLASS="western" STYLE="line-height: 150%">Manual do Usuário</H1>
<P STYLE="margin-bottom: 0.14in; line-height: 150%"><BR><BR>
</P>
<P STYLE="text-indent: 0.39in; margin-bottom: 0.14in; line-height: 150%">
No repositório está disponibilizado um <b> Guia Rápido para o Usuário</b>,
um tutorial na forma de exemplo com os passos básicos para um projeto de redes
básicas de esgoto condominial.

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
<img src="https://github.com/leonazareth/sanihub_redbasica/blob/master/Images/Atributos_Trechos.png" width=60% height=60%></P>
Atributos da camada vetorial de dispositivos de inspeção (nós):</P>
<img src="https://github.com/leonazareth/sanihub_redbasica/blob/master/Images/Atributos_Nodes.png" width=60% height=60%></P>
<P STYLE="text-indent: -0.79in; margin-bottom: 0.14in; line-height: 150%">
Atributos da camada vetorial de unidades de contribuição:</P>
<img src="https://github.com/leonazareth/sanihub_redbasica/blob/master/Images/Unidades%20de%20Contribui%C3%A7%C3%A3o.png" width=60% height=60%></P>


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
Analista de Programação: Ticiano Bragatto</P>
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

Para mais detalhes acesse o link de <a href="https://github.com/leonazareth/sanihub_redbasica/blob/master/LICENSE">LICENÇA</a> do plugin.

<H1 CLASS="western" STYLE="line-height: 150%; page-break-before: always">
Dúvidas e Sugestões</H1>
<P STYLE="margin-bottom: 0.14in; line-height: 150%"><BR><BR>
Qualquer dúvida, sugestão ou para reportar algum problema encontrado podem ser enviados para o e-mail: leonazareth@gmail.com

<H1 CLASS="western" STYLE="line-height: 150%; page-break-before: always">
Como Contribuir?</H1>
<P STYLE="margin-bottom: 0.14in; line-height: 150%"><BR><BR>
Se você tiver interesse em contribuir com o desenvolvimento do plugin, entre em contato pelo email: leonazareth@gmail.com