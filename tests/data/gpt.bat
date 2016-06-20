@echo off

set BEAM4_HOME=C:\Program Files\beam-5.0

"%BEAM4_HOME%\jre\bin\java.exe" ^
    -Xmx4849M ^
    -Dceres.context=beam ^
    "-Dbeam.mainClass=org.esa.beam.framework.gpf.main.GPT" ^
    "-Dbeam.home=%BEAM4_HOME%" ^
    "-Dncsa.hdf.hdflib.HDFLibrary.hdflib=%BEAM4_HOME%\modules\lib-hdf-2.7\lib\jhdf.dll" ^
    "-Dncsa.hdf.hdf5lib.H5.hdf5lib=%BEAM4_HOME%\modules\lib-hdf-2.7\lib\jhdf5.dll" ^
    -jar "%BEAM4_HOME%\bin\ceres-launcher.jar" %*

exit /B %ERRORLEVEL%
