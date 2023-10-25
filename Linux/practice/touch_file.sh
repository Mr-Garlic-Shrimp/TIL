#!/bin/sh

dir_list=$(ls -d */ | cut -c 1-5)

for dir in $dir_list;
do
	for i in $(seq 3);
	do
		touch ./$dir/file_$i.txt;
	done;
done;

