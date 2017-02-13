#!/bin/bash

for f in `find . -name "*Api" | cut -d '/' -f 3`
do
  excludeList=`echo $excludeList,$f`
done

for f in `find . -name "*-model" | cut -d '/' -f 3`
do
  excludeList=`echo $excludeList,$f`
done

excludeList=`echo logs,git,puppetcode,$excludeList`

echo excludeList:excludeList:  $excludeList

repositories='pe-dbe-common pe-dbe-payment pe-dbe-subscriptions pe-fe pe-dbe-expenditurelimit pe-dbe-settlement pe-dbe-notificationServer'
#repositories=$1

echo repositories: $repositories

echo Lines without test...
/d/Aplicaciones/cloc/cloc-1.58.exe --exclude-dir=test,dbunit,$excludeList $repositories
echo Lines with test...
/d/Aplicaciones/cloc/cloc-1.58.exe --exclude-dir=$excludeList $repositories

