DIR_PROJECT_NAME=demo-portifolio-dev
BASE=/root/projects/demos/portifolio-dev/$DIR_PROJECT_NAME
ENV_FOLDER=env
FOLDER_MEDIA="/media"
FOLDER_STATICFILES="staticfiles"

echo "### PROJECT 1 1 ###"
echo "ENTER FOLDER PROJECT"
cd $BASE && . ../$ENV_FOLDER/bin/activate

echo "### Pip install ###"
poetry install

echo "### Django check ###"
python manage.py check --settings=config.settings.production

echo "### Migration ###"
python manage.py migrate --settings=config.settings.production

echo "### very folder 'media' ###"
if [ -f "$FOLDER_MEDIA" ]; then
   echo "existing media folder.(ignore...)"
else
    echo "Folder 'media' does not exist." && \
    sudo mkdir "$FOLDER_MEDIA" && \
    echo "folder created successfully ;)"
fi
sudo chown -R www-data:www-data $BASE/$FOLDER_MEDIA
chmod -R 755 $BASE/$FOLDER_MEDIA
chmod -R 644 $BASE/$FOLDER_MEDIA/

echo "### very folder static files ###"
python manage.py collectstatic --noinput
sudo chown -R www-data:www-data $BASE/$FOLDER_STATICFILES
chmod -R 755 $BASE/$FOLDER_STATICFILES
chmod -R 644 $BASE/$FOLDER_STATICFILES/

echo  "### Restart gunicorn service and socket ###"
sudo systemctl restart demo_portifolio.socket
sudo systemctl restart demo_portifolio.service
sudo systemctl daemon-reload

echo "### Create symbolic link nginx config ###"
sudo ln -sfn /$BASE/nginx/demo_portifolio.conf /etc/nginx/sites-enabled
if sudo nginx -t 2>&1 | grep -q 'successful'; then
    echo "### Reload Nginx ###"
    sudo /etc/init.d/nginx reload
else
    echo "Nginx Fail"
fi
