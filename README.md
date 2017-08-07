# Dependencies

```
sudo pip install django
sudo pip install djangorestframework
```

# Configuration

The configuration file "config.txt" must be created in the api/configuration directory. Below is the format:

```
[GlobalInformation]
apiUserName = Sets username used to authenticate with this API
apiPassword = Sets password used to authenticate with this API
```

# Starting up the API

You must initialize the database of the API with the following command

```
python manage.py migrate
```

Then you can run the API with the following command

```
python manage.py runserver 127.0.0.1:8000
```

Replace 127.0.0.1 with the appropriate IP address you wish to bind the API to, or use 0.0.0.0 to bind the API to all.

Replace 8000 with the desired port you wish the API to listen to

# Ensuring your code is easily imported into this API

This API will pass into your function(s) an image as a byte string.  You can use the following code to convert it into a numpy array.

```
# Load image as numpy
nparr = np.fromstring(image.read(), np.uint8)
frame = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
```

Ensure that the processed image is converted back into a byte string.  You can use the following code to do the conversion.

```
frame_str = cv2.imencode('.jpg', frame)[1].tostring()
```

# Adding custom code to the API

By default, this API will simply return the same image you sent it.

Navigate to and open api -> views.py

Following the placement of the comments, import your module and call the appropriate function(s) as needed.

# API Commands

(GET) /image/

Returns an image with the machine learning processing on top of it.

Header Format:

```
{
	"api-uname":"username", 
	"api-pass":"password",
}
```

Example POST:

```
curl -D /path/for/json/results -v -X POST -F 'image=@/path/to/image' [IP]:[port]/image/ -H "api-uname: [api username]" -H "api-pass: [api password]" > /path/for/output
```

EXAMPLE RESPONSE:

```
HTTP Header['Results']:  JSON Results (if needed)
HTTP Data:  [ImageData as a Byte String]
```

Returns: HTTP Code 200
