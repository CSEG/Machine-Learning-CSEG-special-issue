#!/bin/bash

cd dat/zips

unzip fault_dyke_fold_model.zip
mv model/ ../fault_dyke_fold_model
unzip fold_dyke_fault_model.zip
mv model/ ../fold_dyke_fault_model
unzip gbasin_simplified_model.zip
mv model/ ../gbasin_simplified_model

rm -rf __MACOSX/

cd ..

mkdir output_seismic
mkdir pairs
cd pairs
mkdir A B
cd A
mkdir train test val
cd ../B
mkdir train test val

cd ../../../img_frmt

python modeler.py
python pair_generator.py

cd ../pix2pix

python2 scripts/combine_A_and_B.py --fold_A ../dat/pairs/A/ --fold_B ../dat/pairs/B --fold_AB ../dat/pairs/

cd ../dat/pairs/train

FLOOR=1
RANGE=17600

for i in {1..880}
	do
	number=0
	while [ "$number" -le $FLOOR ]
	do
	  number=$RANDOM
	  let "number %= $RANGE"
	done
	mv $number.jpg ../val/
	echo
done

for i in {1..440}
	do
	number=0
	while [ "$number" -le $FLOOR ]
	do
	  number=$RANDOM
	  let "number %= $RANGE"
	done
	mv $number.jpg ../test/
	echo
done
