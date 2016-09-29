if "%1" == "" (
    set osgeodir="C:\OSGeo4W64"
) else (
    set osgeodir=%1
)
if "%2" == "" (
    set pipinstalls=%~dp0
) else (
    set pipinstalls=%2
)
pushd %osgeodir%

@echo off
rem Root OSGEO4W home dir to the same directory this script exists in
call "bin\o4w_env.bat"

@echo on
set pippackages="%pipinstalls%\pip_packages"
cmd.exe /c "pip install --no-index --find-links %pippackages% setuptools"
cmd.exe /c "pip install --no-index --find-links %pippackages% requests pyopenssl ndg-httpsclient pyasn1"

popd