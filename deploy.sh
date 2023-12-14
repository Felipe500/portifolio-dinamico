DIR_PROJECT_NAME=demo-portifolio-dev
BASE=/root/projects/demos/portifolio-dev/$DIR_PROJECT_NAME
ENV_FOLDER=env

echo "### PROJECT 1 1 ###"
echo "ENTER FOLDER PROJECT"
cd $BASE && . ../$ENV_FOLDER/bin/activate

echo "### Pip install ###"
poetry install

echo "### Django check ###"
python manage.py check --settings=config.settings.production

echo "### Migration ###"
python manage.py migrate --settings=config.settings.production

echo "### Sync with S3 ###"
python manage.py collectstatic --noinput
python manage.py collectstatic --noinput --settings=config.settings.production

echo  "### Restart gunicorn service and socket ###"
sudo systemctl restart my_portifolio.socket
sudo systemctl restart my_portifolio.service
sudo systemctl daemon-reload

echo "### Create symbolic link nginx config ###"
sudo ln -sfn /$BASE/nginx/demo_portifolio.conf /etc/nginx/sites-enabled
if sudo nginx -t 2>&1 | grep -q 'successful'; then
    echo "### Reload Nginx ###"
    sudo /etc/init.d/nginx reload
else
    echo "Nginx Fail"
fi
