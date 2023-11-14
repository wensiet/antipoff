## External service request emulator

### Stack

- Python 3.9
- FastAPI
- MongoDB
- Uvicorn
- Docker
- React

### How to install

- Clone repository to your machine.

```bash
  git clone https://github.com/wensiet/antipoff.git
```

- Run docker container. Note that you need docker installed on your machine.

```bash
  docker-compose up --build
```

- Now you can access the app on http://localhost:8000

### Endpoints

1. Route: [/api/ping](http://localhost:8000/api/ping)

- Method ```GET```
- Request example: ```curl -X 'GET' 'http://127.0.0.1:8000/api/ping' -H 'accept: application/json'```
- Response example:
    ```json
    {
       "msg": "OK"
    }
    ```

2. Route [/api/query](http://localhost:8000/api/query)

- Method ```GET```
- Request
  example: ```curl -X 'GET' 'http://127.0.0.1:8000/api/query?cadastrial=22%3A10%3A2455%3A123345&latitude=22.5635&longitude=55.6864' -H 'accept: application/json'```
- Response example:
    ```json
    {
      "msg": false
    }
    ```

3. Route [/api/history](http://localhost:8000/api/history)

- Method ```GET```
- Request example: ```curl -X 'GET' 'http://127.0.0.1:8000/api/history' -H 'accept: application/json'```
- Response example:
     ```json
  {
      "history": [
       {
         "cadastrial": "12:34:5678:012345",
         "latitude": 12.11,
         "longitude": 23.23,
         "result": true
       },
       {
         "cadastrial": "22:10:2455:123345",
         "latitude": 22.5635,
         "longitude": 55.6864,
         "result": false
       }
      ]
    }
    ```
4. [/admin-panel](http://localhost:8000/admin-panel)
- Method ```GET```
- Description: React Admin Panel
5. [/docs](http://localhost:8000/docs)
- Method ```GET```
- Description: Auto-Generated SwaggerUI docs