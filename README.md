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

# API Commands

(GET) /emotion/
Returns a json with emotional probabilities

Header Format:
	{
		"api-uname":"username", 
		"api-pass":"password",
	}
Example GET:
	curl -X GET http://127.0.0.1:8000/emotion/ -d "@/path/to/image" -H "Content-Type: application/json" -H "api-uname: username" -H "api-pass: password"

EXAMPLE RESPONSE:
	{
	}

Return: HTTP Code 200
