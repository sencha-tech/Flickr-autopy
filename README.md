# Flickr-autopy
Automation of Flickr API using python requests
Prerequisites
1. Create a regular Flickr account
2. Create a new app on Flickr

Make sure you have the consumer key and secret
3. Open the Flickr API documentation
Overview
As you can notice from the very nice image in the documentation, there are three steps we need to perform, before we can actually use the API. These steps are:
1.Getting a Request Token
2.Getting the User Authorization
3.Exchanging the Request Token for an Access Token

So let’s take them one by one.
Step 1 — Getting a Request Token
This is the first step in the OAuth 1.0 flow. Using your consumer key, you are requesting a Request Token which you will later exchange for an Access Token, as soon as the user has given permission.
The endpoint that you need to use is:
https://www.flickr.com/services/oauth/request_token
So open Postman and put that in the address. Additionally, click on the tab Authorization, select OAuth 1.0, and fill in the fields Consumer Key and Consumer Secret with the key and secret you’ve got when creating the app.

OAuth 1.0 configuration in Postman.
If you submit the request as it is, most likely you will get the error:
oauth_problem=parameter_absent&oauth_parameters_absent=oauth_callback
This means that the oauth_callback parameter has not been provided but it is required.
Unfortunately, Postman does not have a field for the callback URL (the URL where the user is going after giving access to your app). So we have to add this manually form the Params tab. Set the value to http://example.com for now.

Step 2— Getting the User Authorization
This is the step where the user has to confirm that he/she wants to allow your application (in this case Postman) to access their account information.
The endpoint for this action is:
https://www.flickr.com/services/oauth/authorize
This request does not need any additional authorization, only a query parameter called oauth_token, which is the exact token you have received in the second step.
So the URL will look like this:
https://www.flickr.com/services/oauth/authorize?oauth_token=72157714121474431-eadbb7c8b59cbee5
Unfortunately, you cannot do this step directly from Postman (as you can with OAuth 2.0). Open this URL in a browser and log in to any Flickr account. You will get this screen asking you to confirm you are giving access to the application you have configured.

The user is asked to confirm that he/she is given access to the application
If the user clicks on OK, Flickr will redirect the user to the callback URL that was configured in the first request (Step 1 — Getting a Request Token).

The oauth_token remains the same but now we also have a piece of new information, the oauth_verifier which we will use in the 3rd step.
Step 3— Exchanging the Request Token for an Access Token
In the previous step, we have obtained the users' permission and now we can go ahead and exchange the request token for an access token that will allow us to make API requests.
The endpoint for this action is:
https://www.flickr.com/services/oauth/access_token
The Consumer Key and the Consumer Secret will stay the same as before. Now you need to add two additional pieces of information that you have got from the first step: the Access Token and the Token Secret.

The next error you will encounter is:
oauth_problem=verifier_invalid
This is because Flickr expects you to send the oauth_verifier you have received through the callback URL.
Again, unfortunately, Postman does not have a configuration for the oauth_verifier, so we have to manually add a query parameter called oauth_verifier with the respective value from the callback URL from step 2.

Manually adding the oauth_verifier query parameter in Postman.
Now we finally have an access token and the secret that can be used in other requests.

Step 4: Verifying the access token
Use the following endpoint to check if the access token works.
https://www.flickr.com/services/rest?nojsoncallback=1&format=json&method=flickr.test.login
Configure the authorization in Postman using the new access token and secret you have gotten in the third step.

And if everything works as expected, you should get the details of the user.

