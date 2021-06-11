## Auth and Sessions in Django

> Part of this app is built based on the tutorial in [How To Tango With Django](https://www.tangowithdjango.com/book17/index.html)

### How Django takes care of authenication

```python
>>> from django.contrib.auth import authenticate
>>> authenticate(username='partha', password='partha')
<User: partha> # Valid
>>> authenticate(username='partha', password='test')
>>> # None => Invalid
```

### Registration

Look into the [view](./login/views.py) for a very basic regisration process 

```python
def register(request)
```

### Login and Logout

```python
username = request.POST.get('username')
password = request.POST.get('password')
user = authenticate(username=username, password=password)
login(request, user)
```

```python
logout(request)
```


Use decorator `@login_required` to restrict access to views ONLY for logged in users

```python
from django.contrib.auth.decorators import login_required

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    # Logged in user can log out
    logout(request)
```

### Cookies

Test cookies to see if your browser supports them:

```python
# Sets a test cookie to determine whether the user’s browser supports cookies
request.session.set_test_cookie()
# Returns either True or False, depending on whether the user’s browser accepted the test cookie
request.session.test_cookie_worked()
# Deletes the test cookie. Use this to clean up
request.session.delete_test_cookie()
```

### Client Side Cookies

```python
from django.shortcuts import render

request.COOKIES.get('<COOKIE>') # All cookie values are returned as strings
response = render(request, '<TEMPLATE-PATH>', {})
response.set_cookie('<COOKIE>', '<COOKIE-VALUE>')
```


### Server Side Cookies

 "A more secure way to save session information is to store any such data on the server side"


```python
request.session.get('<COOKIE>')
request.session['<COOKIE>'] = '<COOKIE-VALUE>'
```

NOTE:

In `settings.py`

> `SESSION_EXPIRE_AT_BROWSER_CLOSE` = `False` # to not expire on browser closure

Which allows you to specify the age of which a cookie can live to

> `SESSION_COOKIE_AGE` = `<TIME-IN-SECONDS>` # expire in `TIME-IN-SECONDS`

