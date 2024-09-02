import requests
import json

# URL of the GraphQL endpoint
graphql_url = "https://api.eonnext-kraken.energy/v1/graphql/"
account_number = '1234567890'
token = ''

def make_graphql_request(operation, query, variables, auth_required=True):
    # Create the payload
    payload = {"operationName": operation, "variables": variables, "query": query}

    # Headers
    headers = {
        'content-type': 'application/json'
    }

    if auth_required & (token != ''):
        headers['authorization'] = token

    # Send the POST request
    response = requests.post(graphql_url, headers=headers, data=json.dumps(payload))
  

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()

        # Check for errors in the response
        if "errors" in response_data:
            print("Error:", response_data["errors"])
            return {}      
        else:
            return response_data
    else:
        print("Failed to connect to the GraphQL endpoint. Status code:", response.status_code)
        print("Response:", response.text)

def login_with_username_and_password(username, password):
    global token
    response = make_graphql_request(
        "loginEmailAuthentication",
        "mutation loginEmailAuthentication($input: ObtainJSONWebTokenInput\u0021) {  obtainKrakenToken(input: $input) {    payload    refreshExpiresIn    refreshToken    token}}",
        {
            "input": {
                "email": username,
                "password": password
            }
        },
        False
    )

    # Check if the login was successful
    if "data" in response and "obtainKrakenToken" in response["data"]:
        token = response["data"]["obtainKrakenToken"]["token"]

def fetch_account_balance(account_number):
    response = make_graphql_request(
        "GetOptimizelyAttributeUserData",
        "query GetOptimizelyAttributeUserData($accountNumber: String!) {account(accountNumber: $accountNumber) {balance}}",
        {
            "accountNumber": account_number
        }
    )

    # Check if the request was successful
    if "data" in response and "account" in response["data"]:
        balance = response["data"]["account"]["balance"]
        print("Account balance:", balance/100.0)
    else:
        print("Failed to fetch account balance")

def main():
    # Login with username and password
    login_with_username_and_password("", "")
    fetch_account_balance(account_number)

main()
