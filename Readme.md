### Ticket administration module (Backend)
This is the back end for a ticket administration module written in Django.

#### Prerequisites:
* python3
* python3-dev
* python3-pip

#### To do:
- [X] Register models in django admin.
- [X] API endpoint.
- [ ] Add ticket solution evidence to models.
- [ ] Use JWT for Front End operations.

#### How to run this backend code:
First of all, I suggest you create a virtual environment (I use pipenv a lot):<br>
1. Go to this project folder on your terminal, then execute.<br>
`pip install pipenv && pipenv shell`
2. Once virtual env. is set up, install avengers_assemble.txt pip packages<br>
`pip install -r ./avengers_assemble.txt`
3. When all packages are set up, create database and migrate models data.<br>
`python manage.py makemigrations && python manage.py migrate`
4. Create a superuser by executing the following command and enter the requested data.<br>
`python manage.py createsuperuser`
5. Finally run the development server and verify everything works fine.<br>
`python manage.py runserver`

#### Currently being developed on Ubuntu 20.04 by Hector Avalos
If you have any suggestion or you want to ask anything, please send me an email:
[hg.avalosc97@gmail.com](mailto:hg.avalosc97@gmail.com)