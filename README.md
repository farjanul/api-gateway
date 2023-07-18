# Micro Service Architecture


## Tasks and Goal

Complete here the following tasks:
-	Develop a Python (Django) microservice api for jwt authentication 
-	Develop a Python (Django) microservice api for Business (data field - Name, location data) 
-	Secure Business api with authentication api and return business data within 10 km in postman api calls
-	Dockerize both the api services 
-	Setup CI/CD for auto build and deployment of these services using Github actions and AWS (EC2) hosting service to auto build docker and deploy it when new code changes is committed to github

## Architecture Flow
![microservice-architecture](https://www.futurefundamentals.com/wp-content/uploads/2019/06/microservice-architecture-1024x560.png)

**Identity Provider:** This handles authentication and authorization for users. It is also quickly deployed and horizontally scaled.

There are two services for executing our plan.
- **API Gateway** - That works for `Identity Provider` and `Routing`. [Repo Link](https://github.com/farjanul/api-gateway)
- **Business Service** - Managing business data and `API`. [Repo Link](https://github.com/farjanul/business-service)

## Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python 3.x](https://www.python.org/)
* [Django 4.x](https://www.djangoproject.com/)
* [SQLite Database](https://www.sqlite.org/index.html)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [JWT Auth](https://jwt.io/)
* [Nginx](https://www.nginx.com/)
* [Gunicorn](https://gunicorn.org/)
* [CI/CD for GitHub Actions](https://github.com/features/actions)
* [AWS EC2 Server](https://aws.amazon.com/ec2/)


## API and Service Specification
**Login API:** default username and password is `admin` and `helloworld`

**Endpoint:** `https://api.example.com/users`
**Method:** `POST`
**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer your-access-token`

**Request Body:**

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "age": 30
}
```

**Login API:** default username and password is `admin` and `helloworld`

**Endpoint:** `https://api.example.com/users`
**Method:** `POST`
**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer your-access-token`

**Request Body:**

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "age": 30
}
```

**Login API:** default username and password is `admin` and `helloworld`

**Endpoint:** `https://api.example.com/users`
**Method:** `POST`
**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer your-access-token`

**Request Body:**

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "age": 30
}
```

**Login API:** default username and password is `admin` and `helloworld`

**Endpoint:** `https://api.example.com/users`
**Method:** `POST`
**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer your-access-token`

**Request Body:**

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "age": 30
}
```

**Login API:** default username and password is `admin` and `helloworld`

**Endpoint:** `https://api.example.com/users`
**Method:** `POST`
**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer your-access-token`

**Request Body:**

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "age": 30
}
```
