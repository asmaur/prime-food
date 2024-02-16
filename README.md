# Web API with Python, Django and Django Rest

This is a CRUD API with Django Rest, it is a part of a course I have on my
YouTube channel <https://youtube.com/@wanubit>.
More about me or Wanubit company on <https://wanubit.com>

## Requirements

The list of tools required to build and run the project:

* Python > 3 version
* Django Rest

## Steps to Set up

**1. Clone the application**

```bash
git@github.com:asmaur/spring-boot-api-tutorial.git .
```

## Building

In order to run project use:

**2. Create the virtual environment**
Create a new virtual enviornment with this command.

```bash
python venv -m .venv
```

**3. Install requirements**
All requirements from requirements.txt file can be installed sing the following command

```bash
pip install -r requirements.txt
```

**4. Run on the default django server**
Start the project on the default django server.

```bash
python manage.py runserver
```

The app will start running at <http://localhost:8000>

Alternatively if you need another port for your app.

```bash
python manage.py runserver 8888
```

The application will start running a <http://localhost:8888>

## Configuration

Configuration can be updated in `setting.py` or using environment variables.

In `prime` app:

* `manage.py` - Start point of the app,
* `prime/models.py` - models classes for Address, Category, Store, Items
* `prime/v1/views.py` - views for all models
* `prime/v1/serialiazers.py` - models serializers
* `prime/v1/urls.py` - all views and methods endpoints

## Explore Rest APIs

The app defines following CRUD APIs.

### Categories Endpoints

* `GET /api/v1/categories` get all categories.

* `POST /api/v1/categories` create new category.

* `GET /api/v1/categories/{id}/` get category by id.

* `PUT /api/v1/categories/{id}/` update category.

* `DELETE /api/categories/{id}/` delete category.

### Address Endpoints

* `GET /api/v1/address` get all address.

* `POST /api/v1/address` create new address.

* `GET /api/v1/address/{id}/` get address by id.

* `PUT /api/v1/address/{id}/` update address.

* `DELETE /api/v1/address/{id}/` delete address.

### Store Endpoints

* `GET /api/v1/stores` get all stores.

* `POST /api/v1/stores` create new store.

* `GET /api/v1/stores/{id}/` get store by id.

* `PUT /api/v1/stores/{id}/` update store.

* `DELETE /api/v1/stores/{id}/` delete store.

### Item Endpoints

* `GET /api/v1/items` get all items.

* `POST /api/v1/items` create new item.

* `GET /api/v1/items/{id}/` get item by id.

* `PUT /api/v1/items/{id}/` update item.

* `DELETE /api/v1/items/{id}/` delete item.

You can find the tutorial for this application on my YouTube channel <https://youtube.com/@wanubit> -
