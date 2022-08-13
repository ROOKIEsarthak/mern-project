@ECHO OFF
SET MYPATH=%~dp0
IF EXIST %MYPATH%bulk_copy_errors.log del /F %MYPATH%bulk_copy_errors.log
mysql_config_editor.exe remove --login-path=wb_migration_source 2>> "%MYPATH%bulk_copy_errors.log"
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
mysql_config_editor.exe set --login-path=wb_migration_source -h127.0.0.1 -P3306 -uroot -p 2>> "%MYPATH%bulk_copy_errors.log"
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
SET command=mysql.exe -h127.0.0.1 -P3306 -uroot -p -s -N information_schema -e "SELECT Variable_Value FROM GLOBAL_VARIABLES WHERE Variable_Name = 'datadir'" 2>> "%MYPATH%bulk_copy_errors.log"
FOR /F "tokens=* USEBACKQ" %%F IN (`%command%`) DO (
    SET DADADIR=%%F
)
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
pushd %DADADIR%
echo [0 %%] Creating directory dump_pump
mkdir dump_pump
pushd dump_pump
copy NUL import_pump.sql
echo SET SESSION UNIQUE_CHECKS=0; >> import_pump.sql
echo SET SESSION FOREIGN_KEY_CHECKS=0; >> import_pump.sql
echo use pump1; >> import_pump.sql
echo [10 %%] Start dumping tables
mysqldump.exe --login-path=wb_migration_source -t --tab=. pump admin --fields-terminated-by=, 2>> "%MYPATH%bulk_copy_errors.log"
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
rename admin.txt admin.csv
del admin.sql
echo LOAD DATA INFILE 'pump1_#####_import/admin.csv' INTO TABLE admin FIELDS TERMINATED BY ',' ENCLOSED BY ''; >> import_pump.sql
echo [20 %%] Dumped table admin
mysqldump.exe --login-path=wb_migration_source -t --tab=. pump collection --fields-terminated-by=, 2>> "%MYPATH%bulk_copy_errors.log"
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
rename collection.txt collection.csv
del collection.sql
echo LOAD DATA INFILE 'pump1_#####_import/collection.csv' INTO TABLE collection FIELDS TERMINATED BY ',' ENCLOSED BY ''; >> import_pump.sql
echo [30 %%] Dumped table collection
mysqldump.exe --login-path=wb_migration_source -t --tab=. pump developer --fields-terminated-by=, 2>> "%MYPATH%bulk_copy_errors.log"
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
rename developer.txt developer.csv
del developer.sql
echo LOAD DATA INFILE 'pump1_#####_import/developer.csv' INTO TABLE developer FIELDS TERMINATED BY ',' ENCLOSED BY ''; >> import_pump.sql
echo [40 %%] Dumped table developer
mysqldump.exe --login-path=wb_migration_source -t --tab=. pump diesel --fields-terminated-by=, 2>> "%MYPATH%bulk_copy_errors.log"
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
rename diesel.txt diesel.csv
del diesel.sql
echo LOAD DATA INFILE 'pump1_#####_import/diesel.csv' INTO TABLE diesel FIELDS TERMINATED BY ',' ENCLOSED BY ''; >> import_pump.sql
echo [50 %%] Dumped table diesel
mysqldump.exe --login-path=wb_migration_source -t --tab=. pump user --fields-terminated-by=, 2>> "%MYPATH%bulk_copy_errors.log"
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
rename user.txt user.csv
del user.sql
echo LOAD DATA INFILE 'pump1_#####_import/user.csv' INTO TABLE user FIELDS TERMINATED BY ',' ENCLOSED BY ''; >> import_pump.sql
echo [60 %%] Dumped table user
mysqldump.exe --login-path=wb_migration_source -t --tab=. pump gas --fields-terminated-by=, 2>> "%MYPATH%bulk_copy_errors.log"
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
rename gas.txt gas.csv
del gas.sql
echo LOAD DATA INFILE 'pump1_#####_import/gas.csv' INTO TABLE gas FIELDS TERMINATED BY ',' ENCLOSED BY ''; >> import_pump.sql
echo [70 %%] Dumped table gas
mysqldump.exe --login-path=wb_migration_source -t --tab=. pump petrol --fields-terminated-by=, 2>> "%MYPATH%bulk_copy_errors.log"
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
rename petrol.txt petrol.csv
del petrol.sql
echo LOAD DATA INFILE 'pump1_#####_import/petrol.csv' INTO TABLE petrol FIELDS TERMINATED BY ',' ENCLOSED BY ''; >> import_pump.sql
echo [80 %%] Dumped table petrol
copy NUL import_pump.cmd
(echo @ECHO OFF) >> import_pump.cmd
(echo echo Started load data. Please wait.) >> import_pump.cmd
(echo SET MYPATH=%%~dp0) >> import_pump.cmd
(echo IF EXIST %%MYPATH%%import_errors.log del /F %%MYPATH%%import_errors.log) >> import_pump.cmd
(echo SET command=mysql.exe -h127.0.0.1 -P3306 -uroot -p -s -N information_schema -e "SELECT Variable_Value FROM GLOBAL_VARIABLES WHERE Variable_Name = 'datadir'" 2^>^> %%MYPATH%%import_errors.log) >> import_pump.cmd
(echo FOR /F "tokens=* USEBACKQ" %%%%F IN ^(^`%%command%%^`^) DO ^() >> import_pump.cmd
(echo     SET DADADIR=%%%%F) >> import_pump.cmd
(echo ^)) >> import_pump.cmd
(echo if %%ERRORLEVEL%% GEQ 1 ^() >> import_pump.cmd
(echo     echo Script has failed. See the log file for details.) >> import_pump.cmd
(echo     exit /b 1) >> import_pump.cmd
(echo ^)) >> import_pump.cmd
(echo pushd %%DADADIR%%) >> import_pump.cmd
(echo mkdir pump1_#####_import) >> import_pump.cmd
(echo xcopy %%MYPATH%%*.csv pump1_#####_import\* 2^>^> %%MYPATH%%import_errors.log) >> import_pump.cmd
(echo if %%ERRORLEVEL%% GEQ 1 ^() >> import_pump.cmd
(echo     echo Script has failed. See the log file for details.) >> import_pump.cmd
(echo     exit /b 1) >> import_pump.cmd
(echo ^)) >> import_pump.cmd
(echo xcopy %%MYPATH%%*.sql pump1_#####_import\* 2^>^> %%MYPATH%%import_errors.log) >> import_pump.cmd
(echo if %%ERRORLEVEL%% GEQ 1 ^() >> import_pump.cmd
(echo     echo Script has failed. See the log file for details.) >> import_pump.cmd
(echo     exit /b 1) >> import_pump.cmd
(echo ^)) >> import_pump.cmd
(echo mysql.exe -h127.0.0.1 -P3306 -uroot -p ^< pump1_#####_import\import_pump.sql 2^>^> %%MYPATH%%import_errors.log) >> import_pump.cmd
(echo if %%ERRORLEVEL%% GEQ 1 ^() >> import_pump.cmd
(echo     echo Script has failed. See the log file for details.) >> import_pump.cmd
(echo     exit /b 1) >> import_pump.cmd
(echo ^)) >> import_pump.cmd
(echo rmdir pump1_#####_import /s /q) >> import_pump.cmd
(echo echo Finished load data) >> import_pump.cmd
(echo popd) >> import_pump.cmd
(echo pause) >> import_pump.cmd
echo [90 %%] Generated import script import_pump.cmd
popd
set TEMPDIR=%DADADIR%dump_pump
echo Set fso = CreateObject("Scripting.FileSystemObject") > _zipIt.vbs
echo InputFolder = fso.GetAbsolutePathName(WScript.Arguments.Item(0)) >> _zipIt.vbs
echo ZipFile = fso.GetAbsolutePathName(WScript.Arguments.Item(1)) >> _zipIt.vbs
echo CreateObject("Scripting.FileSystemObject").CreateTextFile(ZipFile, True).Write "PK" ^& Chr(5) ^& Chr(6) ^& String(18, vbNullChar) >> _zipIt.vbs
echo Set objShell = CreateObject("Shell.Application") >> _zipIt.vbs
echo Set source = objShell.NameSpace(InputFolder).Items >> _zipIt.vbs
echo objShell.NameSpace(ZipFile).CopyHere(source) >> _zipIt.vbs
echo Do Until objShell.NameSpace( ZipFile ).Items.Count ^= objShell.NameSpace( InputFolder ).Items.Count >> _zipIt.vbs
echo wScript.Sleep 200 >> _zipIt.vbs
echo Loop >> _zipIt.vbs
CScript  _zipIt.vbs  "%TEMPDIR%"  "%DADADIR%dump_pump.zip" 2>> "%MYPATH%bulk_copy_errors.log"
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
echo [100 %%] Zipped all files to dump_pump.zip file
xcopy dump_pump.zip %MYPATH% 2>> "%MYPATH%bulk_copy_errors.log"
if %ERRORLEVEL% GEQ 1 (
    echo Script has failed. See the log file for details.
    exit /b 1
)
del dump_pump.zip
del _zipIt.vbs
del /F /Q dump_pump\*.*
rmdir dump_pump
popd
echo Now you can copy %MYPATH%dump_pump.zip file to the target server and run the import script.
pause
