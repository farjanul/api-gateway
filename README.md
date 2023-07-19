# Microservice Architecture
A microservice is a software architectural style that structures an application as a collection of small, independent, loosely coupled services. Each service focuses on performing a specific business capability and can be developed, deployed, and scaled independently.

## Tasks and Goals

**Step:**
Create Microservice `->` Dockerize `->` CI/CD `->` Deploy to AWS EC2

**Complete the following tasks:**
-	Develop a Python (Django) microservice API for JWT authentication 
-	Develop a Python (Django) microservice API for Business (data field - Name, location data) 
-	Secure Business API with authentication API and return business data within 10 km in postman API calls
-	Dockerize both the API services 
-	Setup CI/CD for auto build and deployment of these services using Github actions and AWS (EC2) hosting service to auto build docker and deploy it when new code changes are committed to GitHub

## Architecture Flow
![microservice-architecture](https://www.futurefundamentals.com/wp-content/uploads/2019/06/microservice-architecture-1024x560.png)

**Identity Provider:** This handles authentication and authorization for users. It is also quickly deployed and horizontally scaled.

**There are two services for executing our plan:**
- [API Gateway Repo](https://github.com/farjanul/api-gateway) - That works for `Identity Provider` and `Routing`. 
- [Business Service Repo](https://github.com/farjanul/business-service) - Implementing `business logic` and `API` for business service.

## Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgments section. Here are a few examples.

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

**Login Endpoint:** `https://apigateway.farjanul.com/user/login/`
**Method:** `POST`
**Headers:**
- `Content-Type: application/json`

**Request Body:**

```json
{
    "username": "admin",
    "password": "helloadmin"
}
```

**Response Body**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MDAwMjg5NiwiaWF0IjoxNjg5NzQzNjk2LCJqdGkiOiIxYWE0NTRhMmE2OTQ0OTY4ODkyOGJmOTU4ZDliZDVkMCIsInV1aWQiOjF9.tAAKzVbkOdS1tq_T0yBBIT1mJ7mleKBTxCaQnZ8cvKA",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyMzM1Njk2LCJpYXQiOjE2ODk3NDM2OTYsImp0aSI6ImYyNjE3YmRmNjZlNjQxNTA4ZmRkZWVkMDRlODVlZmI0IiwidXVpZCI6MX0.XoPqHw-sJlPA9pvf7nft-vnLfY7kx4Vk7wxcNrZev54"
}
```

**All Location API Endpoint:** `https://apigateway.farjanul.com/api/businesses/`
**Method:** `GET`
**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer your-access-token`
- `Service: business`

**Response Body:** Here has three cities data. `Dhaka`, `Bogura` and `Chittagong`

```json
[
    {
        "uuid": "39b923a4-c1e7-4d6a-9512-73e7c7aa5217",
        "name": "Bogura Edward Paura Park",
        "latitude": 24.846345,
        "longitude": 89.37089
    },
    {
        "uuid": "2c7e70ae-9645-485d-a145-3a451e2b5211",
        "name": "Chittagong Zoo",
        "latitude": 22.366067,
        "longitude": 91.796522
    },
    {
        "uuid": "45112442-e77e-4234-9f90-0a6ed1bb7147",
        "name": "Foy's Lake, Chittagong",
        "latitude": 22.371886,
        "longitude": 91.792769
    },
    {
        "uuid": "a2d75ec6-400d-4f0e-a5b6-39565dec92d8",
        "name": "Gloria Jean's Coffees, Gulshan 1",
        "latitude": 23.779086,
        "longitude": 90.416442
    },
    {
        "uuid": "49a80665-60e9-49d3-b225-e43df0c9f25b",
        "name": "Pan Pacific Sonargaon Dhaka",
        "latitude": 23.749863,
        "longitude": 90.393667
    },
    {
        "uuid": "4058051c-d170-42ee-8723-3053faddf22a",
        "name": "Shaheed Chandu Stadium, Bogura",
        "latitude": 24.839056,
        "longitude": 89.365187
    },
    {
        "uuid": "2cdc6181-430d-4c04-b1d1-9dae7a5831e4",
        "name": "Square Hospitals Ltd",
        "latitude": 23.752746,
        "longitude": 90.381707
    }
]
```

**Location within 10km API Endpoint:** `https://apigateway.farjanul.com/api/businesses/within-10km/?lat=23.761809&lon=90.401848`
**Method:** `GET`
**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer your-access-token`
- `Service: business`

**Request Body:**

```json
[
    {
        "uuid": "a2d75ec6-400d-4f0e-a5b6-39565dec92d8",
        "name": "Gloria Jean's Coffees, Gulshan 1",
        "latitude": 23.779086,
        "longitude": 90.416442
    },
    {
        "uuid": "49a80665-60e9-49d3-b225-e43df0c9f25b",
        "name": "Pan Pacific Sonargaon Dhaka",
        "latitude": 23.749863,
        "longitude": 90.393667
    },
    {
        "uuid": "2cdc6181-430d-4c04-b1d1-9dae7a5831e4",
        "name": "Square Hospitals Ltd",
        "latitude": 23.752746,
        "longitude": 90.381707
    }
]
```

**Create Location API Endpoint:** `https://apigateway.farjanul.com/api/businesses/`
**Method:** `POST`
**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer your-access-token`
- `Service: business`

**Request Body:**

```json
{
    "name": "Gloria Jean's Coffees, Gulshan 1",
    "latitude": 23.779086,
    "longitude": 90.416442
}
```

**Response Body:**
```json
{
    "uuid": "a2d75ec6-400d-4f0e-a5b6-39565dec92d8",
    "name": "Gloria Jean's Coffees, Gulshan 1",
    "latitude": 23.779086,
    "longitude": 90.416442
}
```

**Update Location APIEndpoint:** `https://apigateway.farjanul.com/api/businesses/<uuid>/`
**Method:** `PATCH`
**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer your-access-token`
- `Service: business`

**Request Body:**

```json
{
    "name": "Foy's Lake, Chittagong Sample"
}
```

**Response Body:**
```json
{
    "uuid": "45112442-e77e-4234-9f90-0a6ed1bb7147",
    "name": "Foy's Lake, Chittagong Sample",
    "latitude": 22.371886,
    "longitude": 91.792769
}
```

**Delete Location API Endpoint:** `https://apigateway.farjanul.com/api/businesses/<uuid>/`
**Method:** `DELETE`
**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer your-access-token`
- `Service: business`

**Response Body:**

```json
{
    "message": "DELETE request processed successfully."
}
```

## Installation

You can easily set up the project by following the steps below. In that case, `Docker` and `Docker Compose` are required.

1. Clone the repo
   ```sh
   git clone git@github.com:farjanul/api-gateway.git
   ```
   and

   ```sh
   git clone git@github.com:farjanul/business-service.git
   ```
   
2. Create the `.env` file copying from `.env.example` and update these values for both projects.
3. Run the project.
    ```sh
    docker-compose up --build -d
    ```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Developer
Follow me on - [@LinkedIn](https://www.linkedin.com/in/farjanuln/)

😊 Happy Coding 😊
