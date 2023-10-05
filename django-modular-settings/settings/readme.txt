1- when you implemented this method you must modify manage.py file like this :

```

from project_name.setting import base


if base.DEBUG == True:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings.production')

```


2- whenever we set DEBUG to False we must set a domain in ALLOWED_HOSTS .