meta/rose-meta.conf


[jinja2:suite.rc=USE_PREBUILD]
compulsory=true
description=Use prebuilds for compilation ?
help=This controls whether the build step uses pre(compiled)-builds distributed
    =by the UM team at version. Using prebuilds can reduce the compilation
    =time as well as memory/disk space requirements significantly. At the same
    =time some code changes, and desire to use Dr hook will mean prebuilds have
    =to be turned Off
sort-key=1a
type=boolean


app/fcm_make/rose-app.conf:5:DR_HOOK=false
app/um/rose-app.conf:12:DR_HOOK=false
app/um/rose-app.conf:13:!!DR_HOOK_CATCH_SIGNALS=0
app/um/rose-app.conf:14:!!DR_HOOK_IGNORE_SIGNALS=0
app/um/rose-app.conf:15:!!DR_HOOK_OPT=wallprof,self
app/um/rose-app.conf:16:!!DR_HOOK_PROFILE=$CYLC_TASK_WORK_DIR/drhook.prof.%d
app/um/rose-app.conf:17:!!DR_HOOK_PROFILE_LIMIT=-10.0
app/um/rose-app.conf:18:!!DR_HOOK_PROFILE_PROC=-1

../u-bz168/app/fcm_make/rose-app.conf:5:DR_HOOK=true
../u-bz168/app/um/rose-app.conf:12:DR_HOOK=true
../u-bz168/app/um/rose-app.conf:13:DR_HOOK_CATCH_SIGNALS=0
../u-bz168/app/um/rose-app.conf:14:DR_HOOK_IGNORE_SIGNALS=0
../u-bz168/app/um/rose-app.conf:15:DR_HOOK_OPT=wallprof,self
../u-bz168/app/um/rose-app.conf:16:DR_HOOK_PROFILE=$CYLC_TASK_WORK_DIR/drhook.prof.%d
../u-bz168/app/um/rose-app.conf:17:DR_HOOK_PROFILE_LIMIT=-0.0
../u-bz168/app/um/rose-app.conf:18:DR_HOOK_PROFILE_PROC=-1


rose-suite.conf

[file:ana/mule_cumf.py]
source=fcm:um.xm_tr/rose-stem/ana/mule_cumf.py@vn11.7

[jinja2:suite.rc]
BUILD=true
CLOCK='PT30M'
CLOCK_RIGOROUS='PT20M'
!!DUMPFREQ=2
HOUSEKEEP=true
RUN_OFFLINE=true
RUN_RIGOROUS=true
RUN_STRATTROP=true
RUN_TESTS=true
SITE='Meto_cray'
!!TASKEND='0,0,2,0,0,0'
USE_PREBUILD=true

[command]
default=rm -rf ${RUNDIR}
app/housekeep/rose-app.conf lines 1-2/2 (END) 

