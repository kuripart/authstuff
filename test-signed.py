# Use this script to test out Cryptographic signing in Djano

from django.core.signing import Signer
from django.core import signing
import sys

signer = Signer()
value = signer.sign('My string')
print(value)
## 'My string:GdMGD6HNQ_qdgxYP8yBZAdAIV1w'

# value += 'm'
try:
    original = signer.unsign(value)
except signing.BadSignature:
    print("Tampering detected!")
    sys.exit(1)

original = signer.unsign(value)
print(original)
## 'My string'

signed = signer.sign(2.5)
print(signed)
## 2.5:_2O6Kk7DhCXl73J82eKvINMSsQF8sBe3WGunKqt_3tQ

original = signer.unsign(signed)
print(original)
## '2.5'

signed_obj = signer.sign_object({'message': 'Hello!'})
print(signed_obj)
## 'eyJtZXNzYWdlIjoiSGVsbG8hIn0:Xdc-mOFDjs22KsQAqfVfi8PQSPdo3ckWJxPWwQOFhR4'

obj = signer.unsign_object(signed_obj)
print(obj)
## {'message': 'Hello!'}




### Using the salt argument

signer = Signer()
value = signer.sign('My string')
print(value)
## 'My string:GdMGD6HNQ_qdgxYP8yBZAdAIV1w'

value = signer.sign_object({'message': 'Hello!'})
print(value)
## 'eyJtZXNzYWdlIjoiSGVsbG8hIn0:Xdc-mOFDjs22KsQAqfVfi8PQSPdo3ckWJxPWwQOFhR4'

signer = Signer(salt='extra')
value = signer.sign('My string')
print(value)
## 'My string:O-qg19vki_W09r4RyqNUK1S2Oc3QGVZWHerPeMAMfTw'

value = signer.unsign(value)
print(value)
## 'My string'

value = signer.sign_object({'message': 'Hello!'})
print(value)
## eyJtZXNzYWdlIjoiSGVsbG8hIn0:F7eUJO5p9nO5WxjxS8K9ep2oQw0A-kJy65Cua8Urc-M

value = signer.unsign_object(value)
print(value)
## {'message': 'Hello!'}




### Verifying timestamped values

from datetime import timedelta
from django.core.signing import TimestampSigner

signer = TimestampSigner()
value = signer.sign('hello')
print(value)
## ephemeral:
## 'hello:1NMg5H:oPVuCqlJWmChm1rA2lyTUtelC-c'

value_unsinged = signer.unsign(value)
print(value_unsinged)
## 'hello'

value_unsinged = signer.unsign(value, max_age=10)
# set: max_age=0.0005 -> gives: django.core.signing.SignatureExpired: Signature age 0.037035465240478516 > 0.0005 seconds
print(value_unsinged)
## 'hello'

value_unsinged = signer.unsign(value, max_age=20)
print(value_unsinged)
## 'hello'

value_unsinged = signer.unsign(value, max_age=timedelta(seconds=20))
print(value_unsinged)
## 'hello'



### Protecting complex data structures

signer = signing.TimestampSigner()
value = signer.sign_object({'foo': 'bar'})
print(value)
## ephemeral:
## eyJmb28iOiJiYXIifQ:1lsuUr:FC26EBp3q4uwfIieHP8UdAZ3heepsdrUffS4XMiX3jg

un = signer.unsign_object(value)
print(un)
## {'foo': 'bar'}

value = signing.dumps({'foo': 'bar'})
print(value)
## ephemeral:
## eyJmb28iOiJiYXIifQ:1lsuUr:Bvnx3HxGhHH7J5CPR3cPuC-Cm6qtU9o--4UmAsr4EQQ

un = signing.loads(value)
print(un)
## {'foo': 'bar'}


value = signing.dumps(('a','b','c'))
print(signing.loads(value))
## ['a', 'b', 'c']


### Use your own signature in place of SECRET_KEY

signer = Signer('my-other-secret')
value = signer.sign('My string')
print(value)
## My string:o3DrrsT6JRB73t-HDymfDNbTSxfMlom2d8TiUlb1hWY