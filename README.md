![analytics image (flat)](https://raw.githubusercontent.com/vitr/google-analytics-beacon/master/static/badge-flat.gif)
![analytics](https://www.google-analytics.com/collect?v=1&cid=555&t=pageview&ec=repo&ea=open&dp=/red_basica/readme&dt=&tid=UA-4677001-16)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EL-BID_red_basica&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EL-BID_red_basica)
---
[![en](https://img.shields.io/badge/lang-en-green.svg)](README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](README.pt.md)
[![es](https://img.shields.io/badge/lang-es-green.svg)](README.es.md)

# Presentation

saniHUB RedBasica is a open-source software aimed at assisting in the design and sizing of sewer collection networks, with tools for designing condominium-type systems. It works as a plugin for the free software QGIS, a Geographic Information System.

In September 2021, version 1.0 of the plugin was released, which is supported by QGIS 3.x and later versions. It is recommended to always use the current stable (LTR) version, which can be checked on the website: [https://qgis.org/en/site/](https://qgis.org/en/site/). Version 1.0 marks the end of the need for using the Excel-based sizing spreadsheet that was previously provided; all calculations previously made in that spreadsheet have been integrated into an application within QGIS itself, making the software 100% free and open-source, in addition to offering greater convenience during the project stages. It is important to mention that the functionality to export the traced network to a .csv file is still available in saniHUB RedBasica, allowing users who prefer to continue using the provided [spreadsheet](https://github.com/sanihub/red_basica/blob/dev/saniBID_RedBasica_Planilha_Dimensionamento_PT_v191020.xlsm) or even their own spreadsheet.

The software was originally developed for the Inter-American Development Bank (IDB), the Spanish Agency for International Development Cooperation (AECID), and the Latin America Investment Facility – European Union (LAIF) with an educational purpose and to promote free access to modern tools for sewer system design, with functionalities adapted for designing condominium-type sewer systems.

# Features

The plugin combines basic functions already present in QGIS (drawing tools, georeferencing, and others) with additional functionalities created to facilitate and automate the design of a sewer collection network.

The tools added to QGIS by the plugin include:

- Creation of pre-configured vector layers (shapes) for project development;
- Naming of collectors;
- Linking between vector layers and their attributes;
- Custom styles and labels for each layer;
- Checking for potential project inconsistencies;
- Windows displaying attributes of the selected section and other project information;
- Tool for calculations and sizing of sewer collection networks directly within QGIS, with all calculation parameters editable;
- Importing results from hydraulic calculations back into the QGIS layout;
- Exporting results of the sized network to EPA SWMM software;
- Displaying the sizing result on the project layout;
- Possibility of exporting trace data for hydraulic calculations to other spreadsheets or external software, and later importing the results.

The link between QGIS modules and the calculation application is simplified using the plugin tools. If the user wants to export for external use (spreadsheet or software), this can be done through the export and import functions of comma-separated text files (“.csv”), containing basic information for sizing, such as: collector names, section names, section lengths, trace typology, terrain elevations, auxiliary notes made by the user during the project, etc.

Both the internal calculation application and the provided calculation spreadsheet (RedBasica) are based on the Brazilian standard for "Design of sanitary sewer collection networks" (NBR 9649), including the calculation of tensile stress. However, the calculation parameters can be freely adjusted by the user to suit local characteristics.

# Installation of the Plugin

To install the saniHUB RedBasica plugin, the user must:

1. Download the file available at the [LINK](https://github.com/sanihub/red_basica/archive/refs/heads/dev.zip);
2. Using QGIS Version 3.0 or higher, open the **Plugins > Manage and Install Plugins** menu, select the **Install from Zip** option, and specify the location where the installer is located on your computer, as shown in the figure:
   ![Plugin Installation](https://raw.githubusercontent.com/leonazareth/sanibid_redbasica/refs/heads/master/Images/01%20Manual_Instalacao_Complemento_4.jpg)

# Tutorials, Courses, and Manuals

Currently, the complete manual for version 1.0, which includes the calculation application in QGIS, is under development. Additionally, there is a course available through the [YouTube channel](https://www.youtube.com/playlist?list=PL1UvLzB7MU_YAU45sXd9zy0UOV3_hkMPH) with translations in English, Spanish, and French. This course is also being updated to include new features.

# Attribute List

The user can choose between using an existing vector layer (with an already traced network) or create a new one and trace it using QGIS drawing tools.

The standard attributes used by the plugin are listed below with their respective functions.


### Atributos da camada vetorial de trechos

### Attributes of the vector layer of segments

| Name           | Description                                                                 | Type    | Size   | Precision | Unit    |
|----------------|-----------------------------------------------------------------------------|---------|--------|-----------|---------|
| `aux_pav_1`      | Street pavement type (e.g., asphalt = 1; cobblestone = 2; concrete block = 3) | string  | 10     | -         | -       |
| `aux_pav_2`      | Sidewalk pavement type, same logic as street pavement                        | string  | 10     | -         | -       |
| `aux_pos`        | Preferred position annotation of the segment (0 = street, 1 = sidewalk)      | string  | 10     | -         | -       |
| `aux_Prof_f`     | Depth assistance required at the downstream point of the current segment (due to interference or other factors) | string  | 80     | -         | -       |
| `aux_Prof_i`     | Depth assistance required at the upstream point of the current segment (due to interference or other factors) | string  | 80     | -         | -       |
| `aux01`          | Generic auxiliary                                                           | string  | 10     | -         | -       |
| `aux02`          | Generic auxiliary                                                           | string  | 10     | -         | -       |
| `aux03`          | Generic auxiliary                                                           | string  | 10     | -         | -       |
| `Caida_p2`       | Drop device at the downstream point of the segment                           | string  | 80     | -         | -       |
| `Caida_p2_h`     | Height of the drop device at the downstream point of the segment            | string  | 80     | -         | m       |
| `DN`             | Nominal diameter of the collector                                            | string  | 80     | -         | mm      |
| `h_col_p1`       | Collector depth at the upstream (initial) point of the segment               | string  | 80     | -         | m       |
| `h_col_p2`       | Collector depth at the downstream (final) point of the segment               | string  | 80     | -         | m       |
| `h_tap_p1`       | Covering layer depth of the collector at the upstream (initial) point of the segment | string  | 80     | -         | m       |
| `h_tap_p2`       | Covering layer depth of the collector at the downstream (final) point of the segment | string  | 80     | -         | m       |
| `Id_Col`         | Name of the collector                                                        | string  | 10     | -         | -       |
| `Id _TRM(n)`     | Name of the segment of the collector (name and number of the current segment) | string  | 10     | -         | -       |
| `L`              | Length of the segment                                                        | real    | 10     | 2         | m       |
| `LABEL_VIS`      | Label visibility helper (1 = visible, 0 = hidden)                           | integer | -      | -         | -       |
| `LABEL_X`        | Label X coordinate helper                                                   | real    | 10     | 6         | m       |
| `LABEL_Y`        | Label Y coordinate helper                                                   | real    | 10     | 6         | m       |
| `Mat_col`        | Pipe material                                                                | string  | 80     | -         | -       |
| `n`              | Manning coefficient of the segment                                            | string  | 80     | -         | -       |
| `Q_f`            | Final flow rate adopted for the segment                                      | string  | 80     | -         | l/s     |
| `Q_i`            | Initial flow rate adopted for the segment                                    | string  | 80     | -         | l/s     |
| `Qt_f`           | Contribution flow rate of the segment at the end of the plan                 | string  | 80     | -         | l/s     |
| `Qt_i`           | Contribution flow rate of the segment at the beginning of the plan           | string  | 80     | -         | l/s     |
| `S`              | Slope of the pipe                                                            | string  | 80     | -         | m/m     |
| `Trativa_f`      | Traction tension at the end of the plan of the segment                       | string  | 80     | -         | Pa      |
| `Trativa_i`      | Traction tension at the beginning of the plan of the segment                  | string  | 80     | -         | Pa      |
| `V_f`            | Flow velocity at the end of the plan                                          | string  | 80     | -         | m/s     |
| `V_i`            | Flow velocity at the beginning of the plan                                    | string  | 80     | -         | m/s     |
| `Vc`             | Critical flow velocity at the end of the plan                                | string  | 80     | -         | m/s     |
| `X_f`            | X coordinate at the end point of the segment (downstream)                    | real    | 10     | 6         | m       |
| `X_i`            | X coordinate at the starting point of the segment (upstream)                 | real    | 10     | 6         | m       |
| `Y_f`            | Y coordinate at the end point of the segment (downstream)                    | real    | 10     | 6         | m       |
| `Y_i`            | Y coordinate at the starting point of the segment (upstream)                 | real    | 10     | 6         | m       |
| `yn_f`           | Liquid level in the collector - end of the plan                              | string  | 80     | -         | m       |
| `yn_i`           | Liquid level in the collector - beginning of the plan                        | string  | 80     | -         | m       |
| `yrel_f`        | Relative liquid level in the collector - end of the plan                     | string  | 80     | -         | %       |
| `yrel_i`         | Relative liquid level in the collector - beginning of the plan              | string  | 80     | -         | %       |

### Attributes of the vector layer of inspection devices (nodes):

| Attribute Name      | Description                                               | Type   | Size   | Precision | Unit   |
|---------------------|-----------------------------------------------------------|--------|--------|-----------|--------|
| `aux_Altura`        | Height of the node.                                        | string | 80     | -         | m      |
| `aux_Cota`          | Elevation of the node.                                     | string | 80     | -         | m      |
| `aux_Diametro`      | Diameter of the node.                                      | string | 80     | -         | mm     |
| `aux_Material`      | Material of the node.                                      | string | 80     | -         | -      |
| `aux_Profundidad`   | Depth of the node.                                         | string | 80     | -         | m      |
| `aux_Tipo`          | Type of node (e.g., inspection pit, inspection chamber).   | string | 80     | -         | -      |
| `Id_Nodo`           | Unique identifier of the node.                             | string | 10     | -         | -      |
| `X`                 | X coordinate of the node.                                  | real   | 10     | 6         | m      |
| `Y`                 | Y coordinate of the node.                                  | real   | 10     | 6         | m      |
| `Z`                 | Z coordinate of the node (elevation).                      | real   | 10     | 6         | m      |

### Attributes of the vector layer of contribution units:

| Name    | Description                                        | Type   | Size    | Precision | Unit   |
|---------|----------------------------------------------------|--------|---------|-----------|--------|
| `Id_UC` | Identification of the contributing block (block)   | string | 10      | -         | -      |
| `Qe_ip` | Number of contributing houses at the start of the plan | integer | 10    | -         | un     |
| `Qe_fp` | Number of contributing houses at the end of the plan | integer | 10    | -         | un     |


# Contributors

- **Concept Analyst**: Leonardo Porto Nazareth
- **Development Coordination**: Marta Fernandez
- **Developers**: Martin Dell' Oro and Federico Sanchez
- **Hydraulic Modeling and Calculations**: Leonardo Porto Nazareth and Pery Nazareth

# License

The saniHUB RedBasica is a Copyleft software. It has free source code for updates and improvements, ensuring that any derivative products from the version available here are licensed under the same terms, and commercialization of such products is prohibited. License Terms: GNU GPLv3

For more details, visit the [LICENSE](https://github.com/leonazareth/sanibid_redbasica/blob/master/LICENSE) link of the plugin.

# Questions and Suggestions

Any questions, suggestions, or to report any issues can be sent to the email: leonazareth@gmail.com

# How to Contribute?

If you are interested in contributing to the development of the plugin, please contact us via email: leonazareth@gmail.com