# Type to run deeppavlov agent
```
docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build
```

# Type to check agent
```
curl --location --request POST 'localhost:4242' --header 'Content-Type: application/json' --data-raw '{"user_id": "1", "payload": "Кто ты?"}'
```
Put your own message in the payload!
