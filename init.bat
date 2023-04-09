::when launching in an editor like VS code with start command, editor must also be restarted 
::along with resulting CMD window for change to take effect

@echo off
if defined PYTHONPATH (GOTO add_directory) else (GOTO create_pythonpath)


:create_pythonpath
setx PYTHONPATH "%cd%"
echo "PYTHONPATH variable created and current path added, session must be restarted for change to take effect"
EXIT /B 0

:add_directory
echo "%PYTHONPATH%" | findstr "%cd%" & if ERRORLEVEL 1 (
    ::if cd not in PYTHONPATH
    setx PYTHONPATH "%PYTHONPATH%";"%cd%"
    echo "variable added, session must be restarted for change to take effect"
) else (
    ::if cd in PYTHONPATH
    echo "current path already exists in PYTHONPATH environment variable"
)
EXIT /B 0


        


