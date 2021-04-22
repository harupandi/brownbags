import logging
import requests
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    userData = {}
    userId = req.params.get('id')
    if userId:
        logging.info('Fetching users data from API')
        r = requests.get('https://brpineda-bapi.azurewebsites.net/getUsers.php')

        data = json.loads(r.text)
        print(data)

        for user in data:
            if (user["id"] == int(userId)):
                userData = {
                    "id": user["id"],
                    "name": user["name"],
                    "username": user["username"]
                }

        if userData:
            return func.HttpResponse(json.dumps(userData))
        else:
            return func.HttpResponse(
                f"User with ID {userId} not found. Please enter a valid user ID.",
                status_code=200
        )
    else:
        return func.HttpResponse("Parameter ID must not be empty.")