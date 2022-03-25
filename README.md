# AsyncRequests
All for implementing async requests app

Each endpoint /get_data/1 and /get_data/2 provide data from json source (data_source folder).

Endpoint /get_data sends async requests with timeout of 2 second.
After getting responses sort data by "id" field.

Note:
If one of sources will fall in exception it means "no data".

# Install
Download and install provided requirements.

# Start
Launch two different instances of FastAPI app on different ports:

uvicorn main:app --host 0.0.0.0 --port 80

uvicorn main:app --host 0.0.0.0 --port 88

# Check Timeouts
Set constant variable in main.py CHECK_TIMEOUT to True value.

# Requests
Send GET request to

http://0.0.0.0:80/get_data

CURL:
curl --request GET \
  --url http://0.0.0.0:80/get_data

to get sorted list of two json sources provided in data_source folder
