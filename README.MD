# Simple API for Adverts

## How to run
- Clone repo 
- Activate env ``` source env/bin/activate ```
- Install all requirements ``` pip install -r requirements.txt ```
- Come to project directory ``` cd advert/ ```
- Run project on 8000 port ``` python manage.py runserver 8000 ```

### Run tests 
``` python manage.py test ```

## Available HTTP Methods

* GET 
  * See all adverts: http://127.0.0.1:8000/ads/
  * See advert by id: http://127.0.0.1:8000/ads/2
- POST
  * Add advert: http://127.0.0.1:8000/ads/ with params like in example: ``` {"subject": "aluminium fälgar och sommar däck",
"body": "Fälgar till BMW 530. Fäglar fina däck lite slitna men fins en del kvar på",
"price": "1500",
"email": "asdasd@assd.asd"} ```
- DELETE 
  * Delete ad by id: http://127.0.0.1:8000/ads/27/ ` curl -X DELETE "http://localhost:8000/ads/<ad-id>/" `

## Sorting results
You can sort results by two fields **created** and **price**

example of get request with sorting: 
- ``` http://127.0.0.1:8000/ads?ordering=price ```


- ``` http://127.0.0.1:8000/ads?ordering=-created ```

# Response structure
```json
[
{
"id": 1,
"subject": "bil till salu",
"body": "det ar min alsklig bil",
"price": "0.00",
"email": "asd@assd.asd"
},
{
"id": 2,
"subject": "basta bord",
"body": "nu saljar jag min bord",
"price": "0.00",
"email": "adddd@as33d.com"
},
...
```