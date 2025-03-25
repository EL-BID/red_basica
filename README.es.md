![analytics image (flat)](https://raw.githubusercontent.com/vitr/google-analytics-beacon/master/static/badge-flat.gif)
![analytics](https://www.google-analytics.com/collect?v=1&cid=555&t=pageview&ec=repo&ea=open&dp=/red_basica/readme&dt=&tid=UA-4677001-16)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EL-BID_red_basica&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EL-BID_red_basica)
---
[![en](https://img.shields.io/badge/lang-en-green.svg)](README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](README.pt.md)
[![es](https://img.shields.io/badge/lang-es-green.svg)](README.es.md)
# Presentación

El plugin saniHUB RedBasica es un software libre que tiene como objetivo ayudar en el trazado y dimensionamiento de redes colectoras de alcantarillado, con herramientas para el diseño de sistemas tipo condominial. Funciona como un complemento (Plug-in) para el software libre QGIS, de Sistema de Información Geográfica.

En septiembre de 2021 se lanzó la versión 1.0 del plugin, que es compatible con las versiones de QGIS 3 en adelante, pero se recomienda siempre utilizar con la versión estable (LTR) actual, que puede consultarse en el sitio: [https://qgis.org/en/site/](https://qgis.org/en/site/). La versión 1.0 marca el fin de la necesidad de usar la hoja de cálculo de dimensionamiento basada en Excel proporcionada anteriormente, todos los cálculos realizados en ella fueron incorporados en una aplicación dentro del propio QGIS, lo que hace al software 100% libre y de código abierto además de ofrecer mayor practicidad durante las etapas del proyecto. Es importante mencionar que las funcionalidades de exportar la red trazada a un archivo .csv siguen disponibles en saniHUB RedBasica, lo que permite que los usuarios que prefieran seguir usando la [hoja de cálculo](https://github.com/sanihub/red_basica/blob/dev/saniBID_RedBasica_Planilha_Dimensionamento_PT_v191020.xlsm) proporcionada o incluso una hoja propia.

El software fue desarrollado originalmente para el Banco Interamericano de Desarrollo (BID), la Agencia Española de Cooperación Internacional para el Desarrollo (AECID) y la Latin America Investment Facility – European Union (LAIF) con fines educativos y para promover el libre acceso a herramientas modernas para el diseño de sistemas de alcantarillado, con funcionalidades adaptadas al diseño de sistemas de alcantarillado tipo condominial.

# Funcionalidades

El complemento combina funciones básicas ya presentes en QGIS (herramientas de dibujo, georreferenciación, entre otras) con otras funcionalidades creadas para facilitar y automatizar el diseño de una red colectora de alcantarillado.

Las herramientas añadidas a QGIS por el complemento son:

- Creación de capas vectoriales (shapes) preconfiguradas para la elaboración del proyecto;
- Nombrado de los colectores;
- Vinculación entre las capas vectoriales y sus atributos;
- Estilos y etiquetas personalizadas para cada capa;
- Verificación de posibles inconsistencias en el proyecto;
- Ventanas de visualización de los atributos del tramo seleccionado y otras informaciones del proyecto;
- Herramienta de cálculos y dimensionamiento de las redes colectoras de alcantarillado directamente dentro de QGIS, con todos los parámetros de cálculo editables;
- Importación de los resultados del cálculo hidráulico realizado de vuelta al trazado en QGIS;
- Exportación de los resultados de la red dimensionada al software EPA SWMM;
- Visualización del resultado del dimensionamiento en el plano de proyecto;
- Posibilidad de exportación de datos del trazado para cálculos hidráulicos en otras hojas de cálculo o software externos y posterior importación de los resultados;

El vínculo entre los módulos de QGIS y la aplicación de cálculos se realiza de manera simplificada utilizando las herramientas del plugin. Si el usuario desea exportar para uso externo (hoja de cálculo o software), esto se hace mediante las funciones de exportación e importación de archivos de texto separados por comas (“.csv”) que contienen información básica para el dimensionamiento, como: nombrado de los colectores, nombrado de los tramos, extensión de cada tramo, tipología del trazado, cotas del terreno, anotaciones auxiliares realizadas por el usuario durante el proyecto, etc.

Tanto la aplicación de cálculos interna como la hoja de cálculo de cálculo proporcionada (RedBasica) están basadas en la norma brasileña de “Proyecto de redes colectoras de alcantarillado sanitario” (NBR 9649), incluyendo el cálculo de tensión trativa. Sin embargo, los parámetros de cálculo pueden ser ajustados libremente por el usuario según las características locales.

# Instalación del Complemento

Para la instalación del complemento saniHUB RedBasica, el usuario debe:

1. Descargar el archivo proporcionado en [LINK](https://github.com/sanihub/red_basica/archive/refs/heads/dev.zip);
2. Usando QGIS versión 3.0 o superior, abrir el menú **Complementos > Instalar Complementos** y elegir la opción **Install from Zip**, luego indicar la ubicación donde se encuentra el instalador en su computadora, como se muestra en la figura:
   ![Instalación del Complemento](https://raw.githubusercontent.com/leonazareth/sanibid_redbasica/refs/heads/master/Images/01%20Manual_Instalacao_Complemento_4.jpg)

# Tutoriales, cursos y manuales

Actualmente, el manual completo para la versión 1.0 que contiene la aplicación de cálculos en QGIS está en desarrollo, además de existir un curso disponible a través del [canal de YouTube](https://www.youtube.com/playlist?list=PL1UvLzB7MU_YAU45sXd9zy0UOV3_hkMPH) con traducción al inglés, español y francés, que también se está actualizando para incluir las nuevas funcionalidades.

# Lista de Atributos

El usuario puede elegir entre utilizar una capa vectorial ya existente (con un trazado de red ya hecho) o insertar una nueva y realizar su trazado utilizando las herramientas de dibujo de QGIS.

Los atributos estándar utilizados por el plugin están listados con sus respectivas funciones a continuación.

### Atributos de la capa vectorial de tramos

| Nombre         | Descripción                                                              | Tipo    | Tamaño | Precisión | Unidad |
|----------------|--------------------------------------------------------------------------|---------|--------|-----------|--------|
| `aux_pav_1`    | Tipo de pavimento de la calle (ej: asfalto = 1; adoquinado = 2; bloque de concreto = 3) | string  | 10     | -         | -      |
| `aux_pav_2`    | Tipo de pavimento de la acera, misma lógica que el pavimento de la calle | string  | 10     | -         | -      |
| `aux_pos`      | Anotación de la posición preferencial del tramo (0 = calle, 1 = acera)  | string  | 10     | -         | -      |
| `aux_Prof_f`   | Ayuda de la profundidad exigida en el punto aguas abajo del tramo actual (por interferencia u otro factor) | string  | 80     | -         | -      |
| `aux_Prof_i`   | Ayuda de la profundidad exigida en el punto aguas arriba del tramo actual (por interferencia u otro factor) | string  | 80     | -         | -      |
| `aux01`        | Auxiliar genérico                                                         | string  | 10     | -         | -      |
| `aux02`        | Auxiliar genérico                                                         | string  | 10     | -         | -      |
| `aux03`        | Auxiliar genérico                                                         | string  | 10     | -         | -      |
| `Caida_p2`     | Dispositivo de caída en el punto aguas abajo del tramo                   | string  | 80     | -         | -      |
| `Caida_p2_h`   | Altura del dispositivo de caída en el punto aguas abajo del tramo        | string  | 80     | -         | m      |
| `DN`           | Diámetro nominal del colector                                             | string  | 80     | -         | mm     |
| `h_col_p1`     | Profundidad del colector en el punto aguas arriba (inicial) del tramo    | string  | 80     | -         | m      |
| `h_col_p2`     | Profundidad del colector en el punto aguas abajo (final) del tramo       | string  | 80     | -         | m      |
| `h_tap_p1`     | Profundidad de la capa de cobertura del colector en el punto aguas arriba (inicial) del tramo | string  | 80     | -         | m      |
| `h_tap_p2`     | Profundidad de la capa de cobertura del colector en el punto aguas abajo (final) del tramo | string  | 80     | -         | m      |
| `Id_Col`       | Nombre del colector                                                       | string  | 10     | -         | -      |
| `Id _TRM(n)`   | Nombre del tramo del colector (nombre y número del tramo actual)         | string  | 10     | -         | -      |
| `L`            | Extensión del tramo                                                        | real    | 10     | 2         | m      |
| `LABEL_VIS`    | Ayuda para visibilidad de etiquetas (1 = visible, 0 = oculto)             | integer  | -      | -         | -      |
| `LABEL_X`      | Ayuda coordenada X de la etiqueta                                          | real    | 10     | 6         | m      |
| `LABEL_Y`      | Ayuda coordenada Y de la etiqueta                                          | real    | 10     | 6         | m      |
| `Mat_col`      | Material de la tubería                                                    | string  | 80     | -         | -      |
| `n`            | Coeficiente de Manning del tramo                                          | string  | 80     | -         | -      |
| `Q_f`          | Caudal de final de tramo adoptado                                          | string  | 80     | -         | l/s    |
| `Q_i`          | Caudal de inicio de tramo adoptado                                         | string  | 80     | -         | l/s    |
| `Qt_f`         | Caudal de contribución del tramo en el final del tramo                    | string  | 80     | -         | l/s    |
| `Qt_i`         | Caudal de contribución del tramo en el inicio del tramo                   | string  | 80     | -         | l/s    |
| `S`            | Pendiente de la tubería                                                   | string  | 80     | -         | m/m    |
| `Trativa_f`    | Tensión trativa en el final del tramo                                     | string  | 80     | -         | Pa     |
| `Trativa_i`    | Tensión trativa en el inicio del tramo                                    | string  | 80     | -         | Pa     |
| `V_f`          | Velocidad de flujo en el final del tramo                                  | string  | 80     | -         | m/s    |
| `V_i`          | Velocidad de flujo en el inicio del tramo                                 | string  | 80     | -         | m/s    |
| `Vc`           | Velocidad crítica de flujo en el final del tramo                          | string  | 80     | -         | m/s    |
| `X_f`          | Coordenada X en el punto final del tramo (aguas abajo)                    | real    | 10     | 6         | m      |
| `X_i`          | Coordenada X en el punto inicial del tramo (aguas arriba)                 | real    | 10     | 6         | m      |
| `Y_f`          | Coordenada Y en el punto final del tramo (aguas abajo)                    | real    | 10     | 6         | m      |
| `Y_i`          | Coordenada Y en el punto inicial del tramo (aguas arriba)                 | real    | 10     | 6         | m      |
| `yn_f`         | Cota líquida en el colector - final de tramo                              | string  | 80     | -         | m      |
| `yn_i`         | Cota líquida en el colector - inicio de tramo                             | string  | 80     | -         | m      |
| `yrel_f`       | Cota líquida relativa en el colector - final de tramo                     | string  | 80     | -         | %      |
| `yrel_i`       | Cota líquida relativa en el colector - inicio de tramo                    | string  | 80     | -         | %      |


### Atributos de la capa vectorial de dispositivos de inspección (nodos):

| Nombre del Atributo | Descripción                                               | Tipo   | Tamaño | Precisión | Unidad |
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


### Atributos de la capa vectorial de unidades de contribución:

| Nombre  | Descripción                                          | Tipo   | Tamaño | Precisión | Unidad |
|---------|----------------------------------------------------|--------|---------|-----------|---------|
| `Id_UC` | Identificación de la cuadra contribuyente (manzana) | string | 10      | -         | -       |
| `Qe_ip` | Número de casas contribuyentes inicio de plano      | integer | 10      | -         | un      |
| `Qe_fp` | Número de casas contribuyentes final de plano       | integer | 10      | -         | un      |

# Colaboradores

- **Analista de Concepto**: Leonardo Porto Nazareth
- **Coordinación de Desarrollo**: Marta Fernandez
- **Desarrolladores**: Martin Dell' Oro y Federico Sanchez
- **Cálculos y Modelado Hidráulico**: Leonardo Porto Nazareth y Pery Nazareth

# Licencia

El saniHUB RedBasica es un software Copyleft. Posee código fuente libre para actualizaciones y mejoras, asegurando, sin embargo, que los productos derivados de la versión aquí disponible estén licenciados bajo términos idénticos, estando prohibida cualquier comercialización de los mismos. Términos de Licencia: GNU GPLv3

Para más detalles accede al enlace de [LICENCIA](https://github.com/leonazareth/sanibid_redbasica/blob/master/LICENSE) del plugin.

# Dudas y Sugerencias

Cualquier duda, sugerencia o para reportar algún problema encontrado pueden ser enviados al correo electrónico: leonazareth@gmail.com

# ¿Cómo Contribuir?

Si tienes interés en contribuir al desarrollo del plugin, contacta por correo electrónico a: leonazareth@gmail.com