![analytics image (flat)](https://raw.githubusercontent.com/vitr/google-analytics-beacon/master/static/badge-flat.gif)
![analytics](https://www.google-analytics.com/collect?v=1&cid=555&t=pageview&ec=repo&ea=open&dp=/red_basica/readme&dt=&tid=UA-4677001-16)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EL-BID_red_basica&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EL-BID_red_basica)
---
[![en](https://img.shields.io/badge/lang-en-green.svg)](README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](README.pt.md)
[![es](https://img.shields.io/badge/lang-es-green.svg)](README.es.md)

# Presentación

El saniHUB RedBasica es un software libre diseñado para apoyar la planificación y dimensionamiento de redes colectoras de alcantarillado sanitario. Ofrece herramientas especializadas para el diseño de sistemas tipo condominial. El software funciona como un complemento para QGIS, un Sistema de Información Geográfica (SIG) gratuito y potente.

Se recomienda siempre utilizar la versión estable actual (LTR), que puede ser consultada en el sitio: [https://qgis.org/en/site/](https://qgis.org/en/site/).

El software fue desarrollado originalmente para el Banco Interamericano de Desarrollo (BID), la Agencia Española de Cooperación Internacional para el Desarrollo (AECID) y la Latin America Investment Facility – European Union (LAIF) con un propósito educativo y para promover el acceso libre a herramientas modernas para el diseño de redes colectoras de alcantarillado sanitario.

# Funcionalidades

El complemento aprovecha una gran cantidad de herramientas esenciales que ya existen en QGIS, como herramientas de dibujo, georreferenciación, tablas de atributos, entre otras, y agrega funcionalidades para facilitar y automatizar el proceso de diseño de redes colectoras de alcantarillado.

Las herramientas desarrolladas por el complemento incluyen:

- Creación de capas vectoriales preconfiguradas (tramos, nodos,...) para el desarrollo del proyecto;
- Nombrado de colectores (tanto manual como automáticamente);
- Vinculación entre capas vectoriales y sus atributos;
- Estilos y etiquetas personalizados para cada capa;
- Verificación de posibles inconsistencias del proyecto;
- Ventanas de visualización de atributos del tramo seleccionado y otra información del proyecto;
- Herramienta para cálculos y dimensionamiento de redes colectoras de alcantarillado directamente en QGIS, con todos los parámetros de cálculo editables;
- Importación de resultados de cálculos hidráulicos de vuelta al diseño de QGIS;
- Exportación de resultados de la red dimensionada al software EPA SWMM;
- Visualización del resultado del dimensionamiento en el diseño del proyecto;
- Visualización del perfil de la red diseñada;
- Posibilidad de exportar datos del trazado para cálculos hidráulicos a otras hojas de cálculo o software externos y posteriormente importar los resultados.

La conexión entre los módulos de QGIS y la aplicación de cálculo se simplifica utilizando las herramientas del complemento. Si el usuario desea exportar para uso externo (hojas de cálculo o software), esto se puede hacer mediante las funciones de exportación e importación de archivos separados por comas (“.csv”), que contienen información básica para el dimensionamiento, como: nombres de colectores, nombres de tramos, longitudes de tramos, tipología del trazado, cotas del terreno, anotaciones auxiliares realizadas por el usuario durante el proyecto, etc.

Tanto la aplicación de cálculo interna como la hoja de cálculo proporcionada (RedBasica) se basan en la norma brasileña "Proyecto de Redes Colectoras de Alcantarillado Sanitario" (NBR 9649), incluyendo el cálculo de tensión trativa. Sin embargo, los parámetros de cálculo pueden ser ajustados libremente por el usuario para adaptarse a las características locales.

# Instalación del Complemento

Para instalar el complemento saniHUB RedBasica, el usuario debe:

1. Descargar el archivo disponible en el [LINK](https://github.com/sanihub/red_basica/archive/refs/heads/dev.zip);
2. Utilizando QGIS versión 3.0 o superior, abrir el menú **Complementos > Administrar e Instalar Complementos**, seleccionar la opción **Instalar desde Zip** y especificar la ubicación donde se encuentra el instalador en su computadora, como se muestra en la figura:
   ![Instalación del Complemento](https://raw.githubusercontent.com/leonazareth/sanibid_redbasica/refs/heads/master/Images/01%20Manual_Instalacao_Complemento_4.jpg)

# Tutoriales, Cursos y Manuales

Actualmente, el manual completo para la versión 1.0, que incluye la aplicación de cálculo en QGIS, está en desarrollo. Además, existe un curso disponible en el [canal de YouTube](https://www.youtube.com/playlist?list=PL1UvLzB7MU_YAU45sXd9zy0UOV3_hkMPH) con traducciones al Inglés, Portugués y Francés. Este curso también se está actualizando para incluir nuevas funcionalidades.

# Lista de Atributos

El usuario puede elegir entre utilizar una capa vectorial ya existente (con una red ya trazada) o crear una nueva y trazarla utilizando las herramientas de dibujo de QGIS.

Los atributos estándar utilizados por el complemento están listados a continuación con sus respectivas funciones.

### Atributos de la capa vectorial de tramos

| Nombre        | Descripción                                                                                   | Tipo    | Tamaño | Precisión | Unidad |
|---------------|-----------------------------------------------------------------------------------------------|---------|--------|-----------|--------|
| `aux_pav_1`   | Tipo de pavimento de la calle (ej: asfalto = 1; adoquín = 2; bloque de concreto = 3)          | string  | 10     | -         | -      |
| `aux_pav_2`   | Tipo de pavimento de la acera, misma lógica que el pavimento de la calle                     | string  | 10     | -         | -      |
| `aux_pos`     | Anotación de la posición preferencial del tramo (0 = calle, 1 = acera)                        | string  | 10     | -         | -      |
| `aux_Prof_f`  | Asistencia de profundidad requerida en el punto de aguas abajo del tramo actual               | string  | 80     | -         | -      |
| `aux_Prof_i`  | Asistencia de profundidad requerida en el punto de aguas arriba del tramo actual              | string  | 80     | -         | -      |
| `aux01`       | Auxiliar genérico                                                                             | string  | 10     | -         | -      |
| `aux02`       | Auxiliar genérico                                                                             | string  | 10     | -         | -      |
| `aux03`       | Auxiliar genérico                                                                             | string  | 10     | -         | -      |
| `Caida_p2`    | Dispositivo de caída en el punto de aguas abajo del tramo                                    | string  | 80     | -         | -      |
| `Caida_p2_h`  | Altura del dispositivo de caída en el punto de aguas abajo del tramo                         | string  | 80     | -         | m      |
| `DN`          | Diámetro nominal del colector                                                               | string  | 80     | -         | mm     |
| `h_col_p1`    | Profundidad del colector en el punto de aguas arriba (inicial) del tramo                     | string  | 80     | -         | m      |
| `h_col_p2`    | Profundidad del colector en el punto de aguas abajo (final) del tramo                       | string  | 80     | -         | m      |
| `h_tap_p1`    | Profundidad de la capa de cobertura del colector en el punto de aguas arriba (inicial)      | string  | 80     | -         | m      |
| `h_tap_p2`    | Profundidad de la capa de cobertura del colector en el punto de aguas abajo (final)         | string  | 80     | -         | m      |
| `Id_Col`      | Nombre del colector                                                                         | string  | 10     | -         | -      |
| `Id_TRM_(n)`  | Nombre del tramo del colector (nombre y número del tramo actual)                           | string  | 10     | -         | -      |
| `L`           | Extensión del tramo                                                                         | real    | 10     | 2         | m      |
| `LABEL_VIS`   | Ayuda de visibilidad de etiquetas (1 = visible, 0 = oculto)                                | entero  | -      | -         | -      |
| `LABEL_X`     | Ayuda de coordenada X de la etiqueta                                                       | real    | 10     | 6         | m      |
| `LABEL_Y`     | Ayuda de coordenada Y de la etiqueta                                                       | real    | 10     | 6         | m      |
| `Mat_col`     | Material de la tubería                                                                     | string  | 80     | -         | -      |
| `n`           | Coeficiente de Manning del tramo                                                          | string  | 80     | -         | -      |
| `Q_f`         | Caudal final adoptado del tramo                                                           | string  | 80     | -         | l/s    |
| `Q_i`         | Caudal inicial adoptado del tramo                                                         | string  | 80     | -         | l/s    |
| `Qmax_f`      | Caudal máximo al final del tramo                                                          | string  | 80     | -         | l/s    |
| `Qmax_i`      | Caudal máximo al inicio del tramo                                                         | string  | 80     | -         | l/s    |
| `Qmed_f`      | Caudal medio al final del tramo                                                          | string  | 80     | -         | l/s    |
| `Qmed_i`      | Caudal medio al inicio del tramo                                                         | string  | 80     | -         | l/s    |
| `Qr_f`        | Caudal recurrente proyectado al final del tramo                                          | string  | 80     | -         | l/s    |
| `Qr_i`        | Caudal recurrente proyectado al inicio del tramo                                         | string  | 80     | -         | l/s    |
| `S`           | Pendiente de la tubería                                                                  | string  | 80     | -         | m/m    |
| `Trativa_f`   | Tensión de tracción al final del tramo                                                  | string  | 80     | -         | Pa     |
| `Trativa_i`   | Tensión de tracción al inicio del tramo                                                 | string  | 80     | -         | Pa     |
| `V_f`         | Velocidad de flujo al final del tramo                                                   | string  | 80     | -         | m/s    |
| `V_i`         | Velocidad de flujo al inicio del tramo                                                  | string  | 80     | -         | m/s    |
| `Vc_f`        | Velocidad crítica de flujo al final del tramo                                           | string  | 80     | -         | m/s    |
| `Vc_i`        | Velocidad crítica de flujo al inicio del tramo                                          | string  | 80     | -         | m/s    |
| `X_f`         | Coordenada X en el punto final del tramo (aguas abajo)                                  | real    | 10     | 6         | m      |
| `X_i`         | Coordenada X en el punto inicial del tramo (aguas arriba)                               | real    | 10     | 6         | m      |
| `Y_f`         | Coordenada Y en el punto final del tramo (aguas abajo)                                  | real    | 10     | 6         | m      |
| `Y_i`         | Coordenada Y en el punto inicial del tramo (aguas arriba)                              | real    | 10     | 6         | m      |
| `yn_f`        | Nivel de líquido en el colector - final del tramo                                       | string  | 80     | -         | m      |
| `yn_i`        | Nivel de líquido en el colector - inicio del tramo                                      | string  | 80     | -         | m      |
| `yrel_f`      | Nivel de líquido relativo en el colector - final del tramo                              | string  | 80     | -         | %      |
| `yrel_i`      | Nivel de líquido relativo en el colector - inicio del tramo                             | string  | 80     | -         | %      |


### Atributos de la capa vectorial de dispositivos de inspección (nodos)

| Nombre         | Descripción                                                                                         | Tipo    | Tamaño | Precisión | Unidad |
|----------------|-----------------------------------------------------------------------------------------------------|---------|--------|-----------|--------|
| `aux04`        | Auxiliar genérico                                                                                   | string  | 10     | -         | -      |
| `aux05`        | Auxiliar genérico                                                                                   | string  | 10     | -         | -      |
| `aux06`        | Auxiliar genérico                                                                                   | string  | 10     | -         | -      |
| `CF_nodo`      | Cota de fondo del dispositivo de inspección                                                        | string  | 80     | -         | m      |
| `Citrd_nodo`   | Cota de intradós del nodo                                                                          | string  | 80     | -         | m      |
| `CT_(N)`       | Cota del terreno en el nodo (inicial y final)                                                     | real    | 10     | 2         | m      |
| `h_nodo_NT`    | Profundidad del dispositivo de inspección respecto al nivel del terreno                           | string  | 80     | -         | m      |
| `h_nodo_tp`    | Profundidad del dispositivo de inspección respecto a su tapa                                      | string  | 80     | -         | m      |
| `Id_NODO_(n)`  | Nombre del nodo actual (CI o PV)                                                                  | string  | 80     | -         | -      |
| `Qi_cat`       | Caudal de fin de plan del área de influencia originada de datos de caudal (registro de usuarios) | real    | 10     | 6         | l/s    |
| `Qf_cat`       | Caudal de fin de plan del área de influencia originada de datos de caudal (registro de usuarios) | real    | 10     | 6         | l/s    |
| `Qi_con`       | Caudal de inicio de plan del área de influencia originada de conexiones                         | real    | 10     | 6         | l/s    |
| `Qf_con`       | Caudal de fin de plan del área de influencia originada de conexiones                            | real    | 10     | 6         | l/s    |
| `Qi_pop`       | Caudal de inicio de plan del área de influencia originada de datos de población                | real    | 10     | 6         | l/s    |
| `Qf_pop`       | Caudal de fin de plan del área de influencia originada de datos de población                   | real    | 10     | 6         | l/s    |
| `Id_UC`        | Identificación de la manzana contribuyente                                                     | string  | 10     | -         | -      |
| `LABEL_VIS`    | Ayuda de visibilidad de etiquetas (1 = visible, 0 = oculto)                                    | entero  | 10     | -         | -      |
| `LABEL_X`      | Ayuda de coordenada X de la etiqueta                                                           | real    | 10     | 6         | m      |
| `LABEL_Y`      | Ayuda de coordenada Y de la etiqueta                                                           | real    | 10     | 6         | m      |
| `Nodo_tipo`    | Tipo y tamaño del dispositivo de inspección                                                   | string  | 80     | -         | -      |
| `Tap_nodo`     | Profundidad de la capa de cobertura del dispositivo de inspección                            | string  | 80     | -         | m      |
| `CF_NODO2`     | Cota del nodo calculada por estimación de profundidad                                         | real    | 10     | 2         | m      |
| `H_NODO_TP2`   | Profundidad del nodo calculada por estimación de profundidad                                  | real    | 10     | 2         | m      |


### Atributos de la capa vectorial de unidades de contribución

| Nombre     | Descripción                                               | Tipo    | Tamaño | Precisión | Unidad |
|------------|-----------------------------------------------------------|---------|--------|-----------|--------|
| `Id_UC`    | Identificación de la manzana contribuyente                | string  | 10     | -         | -      |
| `Qe_ip`    | Número de viviendas contribuyentes al inicio del plan     | entero  | 10     | -         | un     |
| `Qe_fp`    | Número de viviendas contribuyentes al final del plan      | entero  | 10     | -         | un     |
| `QConcI`   | Caudal concentrado al inicio del plan                     | real    | 10     | 4         | l/s    |
| `QConcF`   | Caudal concentrado al final del plan                      | real    | 10     | 4         | l/s    |


# ¿Cómo Contribuir?

Si está interesado en contribuir al desarrollo del complemento, por favor contacte por correo electrónico: leonazareth@gmail.com
