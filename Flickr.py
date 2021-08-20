Import requests
Response = requests.get("https://www.flickr.comservices/rest/?method=flickr.photos.getPopular&api_key=fd70e4e90cc36ed3ecc1fe8319ace1f3&user_id=193746000@NO6&format=json&nojsoncallback=1")
Print (response.json())
Print(response.status_code)
