FORMS = 	../red_basica_dialog_base.ui \
    		../recobrimento_dialog.ui \
			../create_pointLayer_importRaster_dialog.ui \
			../name_segment_dialog_base.ui \
			../ui_segment_dock.ui \
			../export_dialog.ui \
			../recobrimento_dialog.ui \
			../app/resources/edit_values_dialog.ui \
			../app/resources/main_window.ui \
			../app/resources/new_project_dialog.ui \
			../app/resources/parameter_dialog.ui \
			../app/resources/project_dialog.ui
		

SOURCES = 	../red_basica.py \
			../helper_functions.py \
			../pendencias.py \
    		../profundidade.py \
			../app/controllers/CalculationController.py \
			../app/controllers/DataController.py \
            ../app/views/MainView.py

TRANSLATIONS = RedBasica_en.ts RedBasica_es.ts RedBasica_pt.ts

CODECFORTR= LATIN1
#QMAKE=C:\\Qt5\\5.12.2\\mingw73_32\\bin\\qmake.exe
CODECFORSRC = UTF-8

DISTFILES += \
    ../pendencias.py \
    ../profundidade.py \
	../helper_functions.py \
	../red_basica.py \ 
    ../__init__.py \
    ../create_pointLayer_importRaster_dialog.py \
    ../export_dialog.py \
    ../helper_functions.py \
    ../migrate.py \
    ../name_segment_dialog.py \
    ../pendencias.py \
    ../plugin_upload.py \
    ../profundidade.py \
    ../rasterinterpolator.py \
    ../recobrimento_dialog.py \
    ../red_basica.py \
    ../red_basica_dialog.py \
    ../resources.py \
    ../ui_segment_dock.py \
    ../app/views/EditValuesView.py \
    ../app/views/MainView.py \
    ../app/views/NewProjectView.py \
    ../app/views/ParameterView.py \
    ../app/views/ProjectDialogView.py