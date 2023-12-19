DIR_PROJECT_NAME=demo-portifolio-dev
BASE=/root/projects/demos/portifolio-dev/$DIR_PROJECT_NAME
ENV_FOLDER=env
FOLDER_MEDIA="media"
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

echo "### ====================================== ###"
echo "### very folder '/media/$DIR_PROJECT_NAME' ###"
echo "### ====================================== ###"
if [ ! -d "/home/$DIR_PROJECT_NAME" ]; then
    sudo mkdir "/home/$DIR_PROJECT_NAME"
fi

echo "### ====================================== ###"
echo "### very folder 'media' ###"
echo "### ====================================== ###"
if [ ! -d "/home/$DIR_PROJECT_NAME/$FOLDER_MEDIA" ]; then
    sudo mkdir "/home/$DIR_PROJECT_NAME/$FOLDER_MEDIA"
fi

echo "### ====================================== ###"
echo "### very folder static files ###"
echo "### ====================================== ###"
python manage.py collectstatic --noinput
cp -r -f "$BASE/$FOLDER_STATICFILES" "/home/$DIR_PROJECT_NAME/"


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

echo "### ====================================== ###"
echo "### deployment is complete. check website in production ###"
echo "### ====================================== ###"