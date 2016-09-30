# WOIS_Installer <img src="https://github.com/TIGER-NET/screenshots/blob/master/General/WOIS.png" height="40">
This installer is part of the Water Observation Information System (WOIS) developed under the TIGER-NET project funded by the European Space Agency as part of the long-term TIGER initiative aiming at promoting the use of Earth Observation (EO) for improved Integrated Water Resources Management (IWRM) in Africa. 

It calls the installers of the various WOIS components (OSGeo4W software, BEAM, S-1 Toolbox etc.) in the appropriate order and takes care of post-installation tasks such as file copying (e.g. of QGIS plugins) or changing settings.

This is not the complete WOIS software package. The actual software can be downloaded (after registration) from http://www.tiger.esa.int/page_eoservices_wois_form.php.


Copyright (C) 2015 TIGER-NET (www.tiger-net.org) 


## Building

Building the installer requires pyqt version 4. Install it in Anaconda with `conda install pyqt=4`.
