import requests

'''
# 
# example url for API
#

# Api_Region

create_region
url = "http://localhost:8000/api/v1/region"
Request Body: {"name": "CAR"}

update_region
url = "http://localhost:8000/api/v1/region/{{region_id}}"
Request Body: {"name": "CAR - Updated"}

list_region
url = "http://localhost:8000/api/v1/region?page={{page_num}}&per_page={{rows_per_page}}"
Request Query: ?page=1&per_page=10&name=CAR

view_region
url = "http://localhost:8000/api/v1/region/{{region_id}}"

# Api_Province

create_province
url = "http://localhost:8000/api/v1/province"
Request Body: {"name": "Abra", "region_id":1}

update_province
url = "http://localhost:8000/api/v1/province/{{province_id}}"
Request Body: {"name": "CAR - Updated"}

list_province
url = "http://localhost:8000/api/v1/province?page="+str(page_num)+"&per_page="+str(per_page)+"&name="+str(province_name)+"&region_id="+str(region_id)
Request Query: ?page=1&per_page=10&name=Abra&province=1

view_province
url = "http://localhost:8000/api/v1/province/{{province_id}}"

'''

t = 30 #timeout

api_key = "your_api_key_here"

headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json;"
}

class Api_Region:

    def _handle_response(self, response):
        if response.status_code == 200:
            print("Success!")
        elif response.status_code == 404:
            print("Not Found!")
        elif response.status_code == 500:
            print("Internal Server Error!")
        elif response.status_code == 422:
            print("Internal Server Error! 422")
    
    def _handle_exception(self, exception):
        print(exception)
    
    def _make_request(self, url, data, timeout=t):
        try:
            response = requests.post(url, json=data, timeout=timeout, headers=headers)
            self._handle_response(response)
            print(response.text)
        except (requests.exceptions) as e:
            self._handle_exception(e)
            
    def _make_request_get(self, url, timeout=t):
        try:
            response = requests.get(url, timeout=timeout, headers=headers)
            self._handle_response(response)
            print(response.text)
        except (requests.exceptions) as e:
            self._handle_exception(e)

    def view_region(self, url, timeout=10):
        self._make_request_get(url, timeout)

    def create_region(self, url, region_name, timeout=10):
        data = {"region_name": region_name}
        self._make_request(url, data, timeout)
    
    def update_region(self, url, region_name, timeout=10):
        data = {"region_name": region_name}
        self._make_request(url, data, timeout)
        
    def list_region(self, url, timeout=10):
        self._make_request_get(url, timeout)
    

class Api_Province:

    def _handle_response(self, response):
        if response.status_code == 200:
            print("Success!")
        elif response.status_code == 404:
            print("Not Found!")
        elif response.status_code == 500:
            print("Internal Server Error!")
        elif response.status_code == 422:
            print("Internal Server Error! 422")
    
    def _handle_exception(self, exception):
        print(exception)
    
    def _make_request(self, url, data, timeout=t):
        try:
            response = requests.post(url, json=data, timeout=timeout, headers=headers)
            self._handle_response(response)
            print(response.text)
        except (requests.exceptions) as e:
            self._handle_exception(e)
            
    def _make_request_get(self, url, timeout=t):
        try:
            response = requests.get(url, timeout=timeout, headers=headers)
            self._handle_response(response)
            print(response.text)
        except (requests.exceptions) as e:
            self._handle_exception(e)

    def view_province(self, url, timeout=10):
        self._make_request_get(url, timeout)

    def create_province(self, url, province_name, region_id, timeout=10):
        data = {"region_id":region_id, "province_name": province_name}
        self._make_request(url, data, timeout)
    
    def update_province(self, url, province_name, timeout=10):
        data = {"province_name": province_name}
        self._make_request(url, data, timeout)
        
    def list_province(self, url, timeout=10):
        self._make_request_get(url, timeout)

'''

functions for testing Api_Region

'''

def view_data_region ():
    region_id  = 2
    url = "http://localhost:8000/api/v1/region/"+str(region_id)
    viewDataRegion = Api_Region()
    viewDataRegion.view_region(url=url)

def create_data_region ():
    url = "http://localhost:8000/api/v1/region"
    region_name  = "CARwerwelkjr"
    createDataRegion = Api_Region()
    createDataRegion.create_region(url=url, region_name=region_name)

def update_data_region ():
    region_id  = 3
    url = "http://localhost:8000/api/v1/region/"+str(region_id)
    region_name  = "CAR - updated 2"
    updateDataRegion = Api_Region()
    updateDataRegion.update_region(url=url, region_name=region_name)
    
def list_data_region ():
    page_num = 1
    per_page = 10
    region_name  = "CARwerwer"
    # url = "http://localhost:8000/api/v1/region?page="+str(page_num)+"&per_page="+str(per_page) # to test for no name
    url = "http://localhost:8000/api/v1/region?page="+str(page_num)+"&per_page="+str(per_page)+"&name="+str(region_name)
    listDataRegion = Api_Region()
    listDataRegion.list_region(url=url)



'''

functions for testing Api_Province

'''

def view_data_province ():
    province_id  = 1
    url = "http://localhost:8000/api/v1/province/"+str(province_id)
    viewDataProvince = Api_Province()
    viewDataProvince.view_province(url=url)

def create_data_province ():
    url = "http://localhost:8000/api/v1/province"
    province_name  = "La Trinidad"
    region_id = 3
    createDataProvince = Api_Province()
    createDataProvince.create_province(url=url, province_name=province_name, region_id=region_id)

def update_data_province ():
    province_id  = 3
    url = "http://localhost:8000/api/v1/province/"+str(province_id)
    province_name  = "La trinidad - updated"
    updateDataProvince = Api_Province()
    updateDataProvince.update_province(url=url, province_name=province_name)
    
def list_data_province():
    page_num = 1
    per_page = 10
    province_name  = "La trinidad"
    region_id  = 3
    # url = "http://localhost:8000/api/v1/province?page="+str(page_num)+"&per_page="+str(per_page) # to test for no name
    # url = "http://localhost:8000/api/v1/province?page="+str(page_num)+"&per_page="+str(per_page)+"&name="+str(province_name) # to test with name only
    url = "http://localhost:8000/api/v1/province?page="+str(page_num)+"&per_page="+str(per_page)+"&name="+str(province_name)+"&region_id="+str(region_id)
    # url = "http://localhost:8000/api/v1/province?page="+str(page_num)+"&per_page="+str(per_page)+"&region_id="+str(region_id)
    updateDataProvince = Api_Province()
    updateDataProvince.list_province(url=url)


'''

run this functions for testing Api_Region

'''

view_data_region() # done
create_data_region() # done
update_data_region() # done
list_data_region() # done


'''

run this functions for testing Api_Province

'''

view_data_province() # done
create_data_province() # done
update_data_province() # done
list_data_province() # done
