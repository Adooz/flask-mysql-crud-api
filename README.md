
# Getting Started

  This is a simple **CRUD** application
  ## Prerequisite
    1. python3
    2. curl
  ## Setup
> Note: Ensure you are within the flask-mysql-crud-api folder
   
```bs
    //Install the dependencies
    $ pip3 install -r requirements.txt

    // start the server
    $ python3 application.py
```

# API REFERENCES

`POST /api`

#### Creates a new person

#### Sample Request
```bash
$ curl -H "Content-Type: application/json" -d "{\"name\": \"philip\"}" http://localhost:5000/api
```
#### Response 
```json
{
    "message":"Person created successfully",
    "newPerson":{
        "name":"philip",
        "id":"1",
        }
}
```


`GET /api/:user_id`

 #### Returns detail of Person

 #### Sample Request
 ```bash
$ curl -X GET http://localhost:5000/api/1
 ```

#### Response

```json
 {
  "person": [**
    {**
        "_id":"1",
        "name":"Philip",
    }
  ]
 }
```

`PATCH /api/:user_id`

#### Modify person detail

#### Sample Request

```bash
$ curl -X PATCH -H "Content-Type: application/json" -d '{\"name\": \"tomson\"}' http://localhost:5000/api/1
```

#### Response

```json
 {
    "message":"Successfully Updated",
    "updatedPerson": {
        "_id":"1",
        "name":"tomson",
    }
}
```

`DELETE /api/:user_id`

##### Delete a person

#### Sample Request

```bash
$ curl -X DELETE http://localhost:5000/api/1
```

#### Response
```json
{
    "message":"Person successfully deleted",
    "deletedPerson":{
        "_id":"1",
        "name":"tomson",
    }
}

```
### Author
  Kingsley Ndonake

### Acknowledgement
  HNGX
