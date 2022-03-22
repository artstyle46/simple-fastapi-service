# simple-fastapi-service
A fastapi service that has single api which takes any type of input and returns input as output.

# To run the service

- `pip install -r requirements.txt` (once)
- `uvicorn main:app --reload` (to start the service)

# Example Curl request:

```curl --location --request POST 'localhost:8000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "data": {
        "test": [1,23],
        "test2": {
        "1": 2
    }
    }
}'
```
returns
```
{
    "data": {
        "test": [
            1,
            23
        ],
        "test2": {
            "1": 2
        }
    }
}
```
