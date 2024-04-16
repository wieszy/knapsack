#! /bin/sh

python -m venv .;
. bin/activate;
pip install -r requirements.txt --quiet;

tmux kill-session -t otree;

mkdir -p ./backups;
mv ./db.sqlite3 "./backups/db.$(date +%Y%m%d%H%M%S).sqlite3";

tmux new -d \
  -s otree \
  -e 'OTREE_ADMIN_PASSWORD=hello!world' \
  -e "OTREE_PRODUCTION=1" \
  -e "OTREE_AUTH_LEVEL=DEMO" \
  "otree prodserver";

echo "Waiting for server to start...";

sleep 5;
chmod 664 ./db.sqlite3;

echo "Deployed!";