# whatdotapp

Visit [App link goes here](http://divio.com).

## Run locally
- Ensure you have Docker installed.
- Clone the project.
- Create a `.env` file in the root of the cloned repo and add the following defaults
    - SECRET_KEY=`your-project-secret-key`
    - DB_NAME=`your-db-name`
    - DB_USER=`your-db-user`
    - DB_PASSWORD=`your-db-password`
    - DB_HOST=`your-db-host`
    - DB_PORT=`your-db-port`
    - REACT_APP_API_URL="http://localhost:8000/api/"

> NOTE: To create a django secret key, run the shell commands below and copy/paste the generated key.
```
    python manage.py shell
    >>> from django.core.management.utils import get_random_secret_key

    >>> print(get_random_secret_key())

    "gw^9ej(l4vq%d_06xig$vw+b(-@#00@8l7jlv77=sq5r_sf3nu"
```
- Run `docker-compose build`. This should build the project in a container
- Run `docker-compose up`. This will run migration the backend servers.
- You can navigation to `http://localhost:8000/` to interact with the API.

## API Endpoints
- POST login: `http://127.0.0.1:8000/api/user/login/`
- POST register: `http://127.0.0.1:8000/api/user/register/`
- POST logout: `http://127.0.0.1:8000/api/user/logout/`
- GET product: `http://127.0.0.1:8000/api/product/`
- POST create product: `http://127.0.0.1:8000/api/product/`
- PUT update product: `http://127.0.0.1:8000/api/product/<id>/`
