# Abies

An all-in-one web creator.

> Under development

## 1 About `secrets.py`

Before you start the Django app, you would have to create `secrets.py` file under `Abies -> settings -> secrets.py`. This file consists of the following

```python
SECRET_KEY = # Enter your 50 character secret key
```
Use [1.1](11-generating-keys-in-django-style) to generate the key.

### 1.1 Generating keys in Django style

Using Django's crypto package, you can generate random `50` character long key.

```python
from __future__ import print_function
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = get_random_string(50, chars)

print(SECRET_KEY)

```
