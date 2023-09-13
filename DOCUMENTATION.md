# Project: HNG Internship Stage 2 Backend Task


# A. Documentation

---

## 1. Get All Persons

#### Description

- This endpoint gets all persons in the database.

### Method: GET

> ```
> https://hng-api-crud.onrender.com/api
> ```

### Example Response (**raw**)

```json
[
  {
    "id": "1",
    "name": "Adooz Ndonake",
  },
  {
    "id": "2",
    "name": "Ruth Justice",
  }
]
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## 2.Create Person

#### Description

- This endpoint create a new person and save to the database
- Example below shows that a person name "Kingsley Ndonake" has been created and added to the database
- Inputs must be passed through the request body.
- Only name of type string is allowed in the body.
- Name must be unique, if a duplicate name is entered, the request will spit error

### Method: POST

> ```
> https://hng-api-crud.onrender.com/api
> ```

### Example Body (**raw**)

```json
{
  "name": "Adooz Ndonake"
}
```

### Example Response (**raw**)

```json
{
  "name": "Adooz Ndonake",
  "_id": "1",
}
```

### Example Duplicate Error Response (**raw**)

```json
{
  "message": "Duplicate entry. Person already exists"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## 3. Get Single Person

### Method: GET

> ```
> https://hng-api-crud.onrender.com/api/{user_id}
> ```

- Supposing user_id is "1";

### Example Response (**raw**)

```json
{
  "id": "1",
  "name": "Adooz Ndonake",
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## 4. Update Person

### Method: PATCH

> ```
> https://hng-api-crud.onrender.com/api/{user_id}
> ```

- Supposing user_id is "2";

### Example Body (**raw**)

```json
{
  "name": "Ruth Justina"
}
```

### Example Response (**raw**)

```json
{
  "message": "Person Updated successfully"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## 5. Delete Person

### Method: DELETE

> ```
> https://hng-api-crud.onrender.com/api/{user_id}
> ```

- Supposing user_id is "2";

### Example Response (**raw**)

```json
{
  "message": "Person deleted successfully"
}