#!/bin/sh

source=$1

#-------------------------------------------------------------------------------

#	whatson

rm ./whatson/*.py

for f in admin.py apps.py models.py routers.py tests.py views.py
do

scp \
$source:/home/david/Django/derbyartsandtheatre/whatson/$f \
./whatson/.

done
