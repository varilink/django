#!/bin/sh

source=$1
path=/home/david/Django/derbyartsandtheatre

#-------------------------------------------------------------------------------

#	whatson

rm ./whatson/*.py

for f in admin.py apps.py models.py routers.py tests.py views.py
do

scp \
$source:$path/whatson/$f \
./whatson/.

done

scp \
$source:$path/whatson/migrations/0001_initial.py \
./whatson/migrations/.
