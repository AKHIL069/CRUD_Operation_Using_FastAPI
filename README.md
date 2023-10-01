
# CRUD Operations Using FastAPI

In this project, I have performed CRUD opration on Blogs and also create the User for fetching the particular blogs were creating on the database and also use the proper authentication for each User.



## Project Setup

> Ensure that you have [Python3.10](https://www.python.org/downloads/release/python-31013/) installed. 

```
python -m venv /path/to/new/virtual/environment
.\venv\Scripts\activate
pip install -r requirements.txt
```




## API Reference

### Blog API's

#### Get Access Token

```http
    POST /login
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your username |
| `password` | `string` | **Required**. Your password |

#### Get All Blogs

```http
  GET /blog
```

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your Access Token|

#### Get a Blog by id

```http
  GET /blog/{id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required**. Blog Id |

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your Access Token|

#### Create New Blog

```http
  POST /blog
```

| Header | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Your Access Token |

#### Request data
```json
{
  "title": "string",
  "body": "string"
}
```
#### Update any Blog

```http
  PUT /blog/{id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required**. Blog Id |

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your Access Token|

#### Request data
```json
{
  "title": "string",
  "body": "string"
}
```

#### Delete any Blog

```http
  DELETE /blog/{id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required**. Blog Id |

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your Access Token|


### User API's

#### Get a User by id

```http
  GET /user/{id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required**. Blog Id |

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your Access Token|

#### Create New User

```http
  POST /user/create
```

| Header | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Your Access Token |

#### Request data
```json
{
  "name": "string",
  "email": "string",
  "password": "string"
}
```
#### Delete any User

```http
  DELETE /user/{id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required**. User Id |

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your Access Token|
