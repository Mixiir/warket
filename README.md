# Warket

Wine market is a web application for wine lovers, where you can trade and auction wines.

### How to run
1. Clone the repository into your local machine
2. Run the following command:
```pip install -r requirements.txt```
3. Create a file named .env with the following content:
```
SECRET_KEY=''
DB_IP=''
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
FTP_USER=''
FTP_PASSWORD=''
FTP_ADDRESS=''
```
4. Run the following command to start the server:
```python manage.py runserver```