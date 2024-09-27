# Philippines Region and Province API Test

## Prerequisites
 - Python 3.12.0
 - Virtualenv (Optional - Virtual Environment)
 - Docker (Optional - Containerization)
 - SQLite DB Browser (Optional -  view database)
 - Postman (Optional - API Testing)

## Stacks
 - Python
 - FastAPI
 - SQLite3 (Database)

## Virtual Environment Setup
Create a virtual environment:
> python -m venv path/virtualenvironment

Enter the virtual environment (Windows OS):
> source path/virtualenvironment/script/activate

Enter the virtual environment (Linux OS):
> source path/virtualenvironment/bin/activate

Go to app directory and install required libraries
> cd totheappdirectory
> pip install -r requirements.txt

Run app
> python app_fast_api.py

Access the app on http://localhost:8000

## Docker Setup

Build image
> docker build -t myimagename .

Run the image amd create container
> docker run -d --name mycontainername -p 8000:8000 myimagename

Access the app on http://localhost:8000

## API Details

### Api_Region

Create region url = "http://localhost:8000/api/v1/region"
 - Request Body: {"name": "CAR"}

Update region url = "http://localhost:8000/api/v1/region/{{region_id}}"
 - Request Body: {"name": "CAR - Updated"}

List region url = "http://localhost:8000/api/v1/region?page={{page_num}}&per_page={{rows_per_page}}"
 -Request Query: ?page=1&per_page=10&name=CAR

view_region url = "http://localhost:8000/api/v1/region/{{region_id}}"

### Api_Province

Create province url = "http://localhost:8000/api/v1/province"
 - Request Body: {"name": "Abra", "region_id":1}

Update province url = "http://localhost:8000/api/v1/province/{{province_id}}"
 - Request Body: {"name": "CAR - Updated"}

List province url = "http://localhost:8000/api/v1/province?page="+str(page_num)+"&per_page="+str(per_page)+"&name="+str(province_name)+"&region_id="+str(region_id)
 - Request Query: ?page=1&per_page=10&name=Abra&province=1

View province url = "http://localhost:8000/api/v1/province/{{province_id}}"

## Testing API
### Using Postman

Download Postman app in the website: https://www.postman.com/downloads/
In the test directory inside the app directory, import the _PhilippinesRegionAndProvince.postman_collection.json_ file.

### Using api_test.py

Go to the test directory and run api_test.py
> python api_test.py
