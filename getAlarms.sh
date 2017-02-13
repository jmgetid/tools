#!/bin/bash

echo Source#Alarm 
for d in `ls -d pe-*`
do
  if [ $d != 'pe-bmps' ] && [ $d != 'pe-rss' ] && [ $d != 'pe-bmpsrss-core' ]
  then
    cd $d
	for file in `find . -name "*.java"`
	do
		awk 'BEGIN { RS = ";";  FS = "\""}; /LOG_ALARM/ { print FILENAME, $2 }' $file | sed 's/\.java/#/g' | sort | uniq
	done
    cd ..
  fi
done
