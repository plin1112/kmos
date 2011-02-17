#!/usr/bin/env python
import sys
sys.path.append('..')
import main
import shutil

export_dir = 'default_src'
xml_file = 'dreiD.xml'

shutil.rmtree(export_dir,ignore_errors=True)
kmc = main.KMC_Editor()
kmc.project_tree.import_xml_file(xml_file)

kmc.on_btn_export_src__clicked('',export_dir)

exit()
