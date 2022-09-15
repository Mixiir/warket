# Warket

Wine market is a web application for wine lovers, where you can trade and auction wines.

It has been written in python using the Django framework, database used is mysql, but can work with local sqlite3 too.
It is a project for the SD Academy Python course.

Preview images:
![Welcome image](https://github.com/Mixiir/warket/blob/master/warket_viewer/static/images/default_view.png?raw=true)

## Installation

1. Clone the repository into your local machine
2. Create your virtual environment with the command:
   ```py -m venv venv```
3. Activate the created virtual environment by the command:
   ```venv\scripts\activate```
4. Run the following command to install all required packages:
   ```pip install -r requirements.txt```
5. Create a file named '.env' at the root warket directory with the following content:

```
SECRET_KEY=''   #Django secret key
DB_IP=''   #DB addres like - 'random.mysql.center.eu' 
DB_NAME=''   #DB name
DB_USER=''   #DB username
DB_PASSWORD=''  #DB password
FTP_USER=''   #FTP username
FTP_PASSWORD=''   #FTP password
FTP_ADDRESS=''   #FTP server address like - 'center.eu'
FTP_STORAGE_LOCATION=''   #FTP storages full address like - 'ftp://random:password@center.eu:21/htdocs'
IMAGE_SERVER=''   #URL to ftp server like - 'https://center.eu/'
```

6. Run the following command to create and initialize the database:

```
python manage.py makemigrations auctions
python manage.py makemigrations cart
python manage.py makemigrations users
python manage.py makemigrations warket_viewer
python manage.py makemigrations
python manage.py migrate
```

7. Run the following command to create a superuser:
   ```python manage.py createsuperuser```
8. Run the following command to start the server:
   ```python manage.py runserver```
9. Open the browser and go to the following address:
   ```http://127.0.0.1:8000/```
10. Firstly you will need to create some mandatory information for the application to work properly. Go to the following
    address:
    ```http://127.0.0.1:8000/create_manufacturer/``` and create a manufacturer. Then go to the following address:
    ```http://127.0.0.1:8000/auctions/categories/``` and add atleast one category to be able to use the auctions as the
    category is a mandatory field.

## Things to know

Do not forget to create a superuser to be able to access the admin panel.
Users can be created from the admin panel or from the registration page.
By default no user can sell wines, so you will need to give him/her the permission to sell wines from the admin panel.

To access the admin panel go to the following address:
```http://127.0.0.1:8000/admin/```

### How to run tests

1. Run the following command to run all tests:
   ```python manage.py test```

# Authors

1. Kuuba Onnis - [KuubaOnnis]
2. Mikk Narusberg -[Mixiir]

