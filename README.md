# The Saving Grapes

## Requirements

- Django
  - `pip install django`
- Mapbox access token [refer here for detailed information](https://www.fullstackpython.com/blog/maps-django-web-applications-projects-mapbox.html)
  - Go to [Mapbox](mapbox.com).
  - Login or sign up to mapbox.
  - Click on the 'JS Web' link under 'install the Maps SDK'.
  - Then click on 'Use the Mapbox CDN'
  - Click next an copy the access token mentioned under 'mapboxgl.accessToken'
  - Save this value in a new file `./maps/mapbox_token.json`, like below.

    ```json
    {
        "mapbox_access_token" : "<your token>"
    }
    ```

## How to start the app

Once the token is set, you can run the app from the root folder by:

```sh
python manage.py runserver
```
