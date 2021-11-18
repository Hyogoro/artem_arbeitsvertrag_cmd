import avlib as la
import os
from datetime import datetime

mitarbeiterdaten = la.vertragsdaten

la.get_vertrags_input_from_cmd(mitarbeiterdaten)
la.write_dict_to_configfile(inputdict=mitarbeiterdaten, outputfile="texdata/lat.tex")
#os.system("pdflatex texdata/main.tex")
la.generate_avpdf(configfile="texdata/lat.tex", templatefile="texdata/main.tex", outputdir=".", \
    jobname=mitarbeiterdaten['nachname']+"_"+mitarbeiterdaten['stellenbezeichnung']+ str(datetime.today().strftime('%Y-%m-%d')))
