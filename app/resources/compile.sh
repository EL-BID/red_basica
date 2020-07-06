#!/bin/bash

pyuic5 main_window.ui -o ../views/MainWindowUi.py
pyuic5 project_dialog.ui -o ../views/ProjectDialogUi.py
pyuic5 new_project_dialog.ui -o ../views/NewProjectDialogUi.py
pyuic5 parameter_dialog.ui -o ../views/ParameterDialogUi.py
pyrcc5 images/contributions.qrc -o ../views/contributions_rc.py
sed -i 's/import\ contributions_rc/from\ .\ import\ contributions_rc/g' ../views/ParameterDialogUi.py 
echo " "
echo "done!"
# echo "Remember to change the import contributions_rc in ParameterDialogUi to from . import contributions_rc (diff between python 2.7 and 3.4)"