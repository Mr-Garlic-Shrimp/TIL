#!/bin/bash

target_dirs=$(ls -d */)

for dir in $target_dirs;
do
	base_dir=$(basename $dir) 
	if [ -e ${base_dir}.tar ]; then
		echo "${base_dir}.tar already exists. skip tar."
	else
		tar -czvf ${base_dir}.tar $dir
	fi
done
