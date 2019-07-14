### Django Project + Docker Setup in Linux

    Url : https://dzone.com/articles/create-a-simple-api-using-django-rest-framework-in

### Django Project
    
    # Activating an environment
    csk@csk-ai-revolution:~/PycharmProjects/djangoapi$ source activate djangoapi
    (djangoapi) csk@csk-ai-revolution:~/PycharmProjects/djangoapi$ pip install django
        
      Collecting django
              Downloading https://files.pythonhosted.org/packages/36/50/078a42b4e9bedb94efd3e0278c0eb71650ed9672cdc91bd5542953bec17f/Django-2.1.5-py3-none-any.whl (7.3MB)
                100% |████████████████████████████████| 7.3MB 1.4MB/s 
            Collecting pytz (from django)
              Using cached https://files.pythonhosted.org/packages/f8/0e/2365ddc010afb3d79147f1dd544e5ee24bf4ece58ab99b16fbb465ce6dc0/pytz-2018.7-py2.py3-none-any.whl
            Installing collected packages: pytz, django
            Successfully installed django-2.1.5 pytz-2018.7
            (djangoapi) csk@csk-ai-revolution:~/PycharmProjects/djangoapi/djangoapi$ pip install djangorestframework
            Collecting djangorestframework
              Downloading https://files.pythonhosted.org/packages/99/0b/d37a5a96c5d301e23adcabcc2f3fa659fb34e6308590f95ebb50cdbe98a1/djangorestframework-3.9.0-py2.py3-none-any.whl (924kB)
                100% |████████████████████████████████| 931kB 2.4MB/s 
            Installing collected packages: djangorestframework
            Successfully installed djangorestframework-3.9.0
### Start a django project
    (djangoapi) csk@csk-ai-revolution:~/PycharmProjects/djangoapi$ django-admin startproject djangoapi
    (djangoapi) csk@csk-ai-revolution:~/PycharmProjects/djangoapi$ cd djangoapi

### Create an app

    (djangoapi) csk@csk-ai-revolution:~/PycharmProjects/djangoapi/djangoapi$ python manage.py startapp api

### Migrate 
    
    (djangoapi) csk@csk-ai-revolution:~/PycharmProjects/djangoapi/djangoapi$ python3 manage.py migrate

    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying admin.0003_logentry_add_action_flag_choices... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying sessions.0001_initial... OK

### Run
    (djangoapi) csk@csk-ai-revolution:~/PycharmProjects/djangoapi/djangoapi$ python3 manage.py runserver 8000
    Performing system checks...
    
    System check identified no issues (0 silenced).
    January 05, 2019 - 09:53:41l
    Django version 2.1.5, using settings 'djangoapi.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    
