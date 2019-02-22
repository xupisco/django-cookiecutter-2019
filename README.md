# django cookiecutter 2019
2019 (c) \@xupisco - <xupisco@gmail.com>

 1. Create your virtualenv
 2. Install cookiecutter `$ pip install cookiecutter`
 3. Install this project `$ cookiecutter <ADD_PROJECT_REPO_HERE>`
 4. Answer the questions about your project
 5. Run `$ pip install -r requirements/dev.txt`
 6. Migrate `$ manage.py migrate`, and run `$ manage.py runserver`
 7. ...
 8. Profit!

#### Default packages and apps
What's inside?

- Django Rest Framework (optional)
- Django AllAuth (optional)
- Django Grappelli and Filebrowser (optional)
- Django Filter (optional)
- Markdown
- Pillow (optional)
- And some other used for development (see requirements/dev.txt)

#### Just ignore below this line for now!

Create the file: **conf/settings.ini**
```
[settings]
SITE_NAME=ACME
ADMIN_TITLE=ACME Admin
SITE_URL=https://acme.net

SECRET_KEY=jenny_ive_got_your_number...its_867-5309
DEBUG=True
DATABASE_URL=postgres://user:passwd@127.0.0.1/database_name
EMAIL_BACKEND=django.core.mail.backends.filebased.EmailBackend

OG_DESCRIPTION=ACME Website is open for business
GTM_ID=1234 (without the "GTM-" part)
TW_CONSUMER_KEY=<twitter app key>
TW_CONSUMER_SECRET=<twitter app secrect>
TW_TOKEN=<twitter token>
TW_TOKEN_SECRET=<twitter secret>
FACEBOOK_APP_ID=<facebook app ai>
```

**PostgreSQL setup**
```
$ sudo -i -u postgres
(postgres) $ psql
postgres=# CREATE ROLE <user> WITH PASSWORD '<passwd>' LOGIN CREATEDB;
postgres=# CREATE DATABASE <database_name> WITH OWNER <user>;
```