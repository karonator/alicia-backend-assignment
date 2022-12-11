# Alicia backend assignment

Thank you for interesting assignment!
The easiest way to try this API is to use postman.
Please, don't forget to fill basic auth credentials while doing cart_item and order endpoints requests.

## Technologies used
- Python
- Django
- django-rest-framework

## Installation
To start the server just use the command:

``` docker-compose --env-file .env up ```

Server is configured to use PostgreSQL database, so I added the corresponding configuration in ```docker-compose.yml``` file.

After server and DB startup, please use this commands to migrate DB and create user:

``` docker exec -it alicia-backend-assignment-server-1 python manage.py migrate ```
``` docker exec -it alicia-backend-assignment-server-1 python manage.py createsuperuser ```

(Container name may differ from alicia-backend-assignment-server-1)
After this, login to admin panel at ``` http://127.0.0.1/admin/ ```

## Endpoints

#### product
Allowing to list all products (short presentation), and to see a detailed representation of product
Allowed methods: GET, auth required: no

**Request: all products**
``` GET: 127.0.0.1/api/v1/product/ ```

**Response**
```json
[
    {
        "id": 1,
        "title": "product 1",
        "sku": "sku 1",
        "short": "ke ke ke",
        "price": 9.9
    },
    {
        "id": 2,
        "title": "product 2",
        "sku": "some sku 2",
        "short": "alalala",
        "price": 3.0
    }
]
```

**Request: one product**
``` GET: 127.0.0.1/api/v1/product/1 ```

**Response**
```json
{
    "id": 1,
    "properties": [
        {
            "id": 1,
            "title": "azaza",
            "value": "xxx"
        }
    ],
    "title": "product 1",
    "sku": "sku 1",
    "short": "ke ke ke",
    "full": "fe fe fe",
    "price": 9.9
}
```

#### cart_item
Allowing to create, get, and delete cart_item's
Allowed methods: GET, POST, DELETE, auth required: basic auth

If the product already exists in cart, instead of creating a new cart item, the amount of products in the cart will be increased.

**Request: create cart_item (adding product to cart)**
``` POST: 127.0.0.1/api/v1/cart_item ```
Params: product: 1, amount: 5

**Response**
```json
{
    "id": 7,
    "amount": 5,
    "product": 1
}
```

**Request: list cart items**
``` GET: 127.0.0.1/api/v1/cart_item ```

**Response**
```json
[
    {
        "id": 7,
        "product": {
            "id": 1,
            "title": "product 1",
            "sku": "sku 1",
            "short": "ke ke ke",
            "price": 9.9
        },
        "amount": 5
    }
]
```

**Request: delete cart items**
``` DELETE: 127.0.0.1/api/v1/cart_item/7 ```

**Response**
Empty massage woth status code 200

#### order
Allowing to create, get, list orders
Allowed methods: GET, POST, auth required: basic auth

If cart is empty, the request will fail with an error.
If not, the cart will clear.

**Request: create order**
``` POST: 127.0.0.1/api/v1/order ```
Params: delivery_time: 2022-12-10T22:25:17+0000

**Response**
```json
{
    "id": 8,
    "items": [
        {
            "id": 6,
            "product": {
                "id": 1,
                "title": "product 1",
                "sku": "sku 1",
                "short": "ke ke ke",
                "price": 9.9
            },
            "amount": 5
        }
    ],
    "delivery_time": "2022-12-10T22:25:17Z"
}
```

**Request: get one order**
``` GET: 127.0.0.1/api/v1/order/1 ```


**Response**
```json
{
    "id": 8,
    "items": [
        {
            "id": 6,
            "product": {
                "id": 1,
                "title": "product 1",
                "sku": "sku 1",
                "short": "ke ke ke",
                "price": 9.9
            },
            "amount": 5
        }
    ],
    "delivery_time": "2022-12-10T22:25:17Z"
}
```

**Request: list orders**
``` GET: 127.0.0.1/api/v1/order ```


**Response**
```json
[
    {
        "id": 1,
        "items": [
            {
                "id": 1,
                "product": {
                    "id": 1,
                    "title": "product 1",
                    "sku": "sku 1",
                    "short": "ke ke ke",
                    "price": 9.9
                },
                "amount": 3
            },
            {
                "id": 2,
                "product": {
                    "id": 2,
                    "title": "product 2",
                    "sku": "some desc 2",
                    "short": "alalala",
                    "price": 3.0
                },
                "amount": 1
            }
        ],
        "delivery_time": "2022-12-10T22:09:07Z"
    }
]
```
