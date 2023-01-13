# spam-detection-ai
Spam detection AI POC in python using kaggle dataset

# Objective
The objective of this POC is to create a RESTful API that reads data from the dataset, passes it to ML algorithm and gives an output.

# How To Run
- Git clone the repository
- Run `pip install`
- Run `flask run --port 8000`

### Example of Spam: Result = 1
```
curl --location --request POST 'http://127.0.0.1:8000/detect-spam' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sentence": "Click here to win 1 million dollars $$$$"
}'
```

### Response
```
{
    "is_spam": true
}
```

### Example of Spam: Result = 0
```
curl --location --request POST 'http://127.0.0.1:8000/detect-spam' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sentence": "Hello this is Siddhesh"
}'
```

### Response
```
{
    "is_spam": false
}
```