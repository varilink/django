#!/bin/sh

target=$1

#-------------------------------------------------------------------------------

#	whatson

ssh $target /bin/dash <<'EOF'
for f in admin.py apps.py models.py routers.py tests.py views.py
do
rm /home/david/Django/derbyartsandtheatre/whatson/$f
done
rm /home/david/Django/derbyartsandtheatre/whatson/migrations/0001_initial.py
EOF

scp -r \
./whatson/* \
$target:/home/david/Django/derbyartsandtheatre/whatson/.

