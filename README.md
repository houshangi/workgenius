a django web-app that takes opening hours of a resturant 
in JSON format and returns the human-readable string in response.

## Local Setup

```
sudo pip3 install virtualenv
virtualenv --python python3.10 venv
source venv/bin/activate
```

## Install Dependencies
after activating venv run following command :
```
pip install -r requirements.txt
```
## Config Project 
create a .env file in the same directory as setting.py and add following lines to it 
```
SECRET_KEY=<Your SECRET KEY>
DEBUG=True=TRUE #False for production

```
## Run Development WebApp
```
python manage.py runserver 
```
## Run Unit Tests
```
python manage.py test mail_events.tests
```

## Local Demo
run the following curl command :
```
curl --location 'http://localhost:8000/api/send-event/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "mandrill_events": [
        {
            "event": "open",
            "msg": {
                "ts": 1365109999,
                "subject": "Roses Are Red, Violets Are On Sale",
                "email": "flowerfriend@example.com",
                "sender": "hello@eiffelflowers.biz",
                "tags": [
                    "violets"
                ],
                "opens": [
                    {
                        "ts": 1365111111
                    }
                ],
                "clicks": [
                    {
                        "ts": 1365111111,
                        "url": "https://www.eiffelflowers.biz/news/ultraviolet-sale"
                    }
                ],
                "state": "sent",
                "metadata": {
                    "user_id": 111
                },
                "_id": "7761629",
                "_version": "123"
            }
        }
    ]
}'

## Considaration 
i couldnt get access to Mandrill Web app because of conflicts in my country , so i desinged a simple webhook with no specific Security on the endpoint.
please just look at my api desing as a toy Api Design because of this conflict.