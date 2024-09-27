import uvicorn
from fastapi import FastAPI, Header, HTTPException, Depends,  Query
from pydantic import BaseModel
from typing import List, Optional

import functions.func_db as func_db

app = FastAPI()

API_KEY = "your_api_key_here"

def verify_api_key(authorization: str = Header(...)):
   if authorization != f"Bearer {API_KEY}": 
      raise HTTPException(status_code=401, detail="Invalid API Key")
   
   if authorization is None:
      raise HTTPException(status_code=400, detail="API Key missing")

class Region(BaseModel):
   region_id: int = None
   region_name: str = None
   created_date: str = None
   modified_date: str = None
   
class Province(BaseModel):
   province_id: int = None
   region_id: int = None
   province_name: str = None
   created_date: str = None
   modified_date: str = None

class RegionResponse(BaseModel):
   region_id: int = None
   region_name: str = None
   created_date: str = None
   modified_date: str = None

class ProvinceResponse(BaseModel):
   province_id: int = None
   region_id: int = None
   province_name: str = None
   created_date: str = None
   modified_date: str = None

class PaginatedResponse(BaseModel):
    total: int
    page: int
    per_page: int
    data: List[RegionResponse]
    
class PaginatedResponseProvince(BaseModel):
    total: int
    page: int
    per_page: int
    data: List[ProvinceResponse]

def get_filtered_regions(name: Optional[str], page: int, per_page: int):
   def db_tbl_list_region():
      db = func_db.Database()
      emps = db.list_region()
      return emps
   resRegion = db_tbl_list_region()
   filtered_regions = []

   # Filter by region name if a filter is provided
   if name:
      # filtered_regions = [region for region in resRegion if name.lower() in region["region_name"].lower()]
      for items in resRegion:
         if items["region_name"].lower() == name.lower():
            filtered_regions.append(items)
   else:
      filtered_regions = resRegion
   
   # Calculate total number of filtered records
   total = len(filtered_regions)
   
   # Apply pagination
   start = (page - 1) * per_page
   end = start + per_page
   paginated_regions = filtered_regions[start:end]
   
   return paginated_regions, total

def get_filtered_provinces(name: Optional[str], region_id: Optional[str], page: int, per_page: int):
   def db_tbl_list_province():
      db = func_db.Database()
      emps = db.list_province()
      return emps
   resProvince = db_tbl_list_province()
   filtered_provinces = []

   # Filter by region name if a filter is provided
   if name and region_id:
      # filtered_regions = [region for region in resRegion if name.lower() in region["region_name"].lower()]
      for items in resProvince:
         if items["province_name"].lower() == name.lower() and str(items["region_id"]) == str(region_id) :
            filtered_provinces.append(items)

   elif name:
      # filtered_regions = [region for region in resRegion if name.lower() in region["region_name"].lower()]
      for items in resProvince:
         if items["province_name"].lower() == name.lower() :
            filtered_provinces.append(items)
            
   elif region_id:
      # filtered_regions = [region for region in resRegion if name.lower() in region["region_name"].lower()]
      for items in resProvince:
         if str(items["region_id"]) == str(region_id) :
            filtered_provinces.append(items)
   else:
      filtered_provinces = resProvince
   
   # Calculate total number of filtered records
   total = len(filtered_provinces)
   
   # Apply pagination
   start = (page - 1) * per_page
   end = start + per_page
   paginated_provinces = filtered_provinces[start:end]
   
   return paginated_provinces, total

'''

Region

'''

@app.get('/api/v1/region/{region_id}', dependencies=[Depends(verify_api_key)])
def view_region(region_id):

   def db_tbl_view_region():
      db = func_db.Database()
      emps = db.view_region(region_id)
      return emps
   resRegion = db_tbl_view_region()
   
   return resRegion

@app.post('/api/v1/region', dependencies=[Depends(verify_api_key)])
def create_region(region: Region):

   if not region.region_name:
      raise HTTPException(status_code=400, detail="Region name is missing")

   def db_tbl_list_region():
      db = func_db.Database()
      emps = db.list_region()
      return emps
   resRegion = db_tbl_list_region()

   def db_tbl_insert_region():
      db = func_db.Database()
      emps = db.insert_region(region.region_name)
      return emps
   
   for items in resRegion:
      if items["region_name"].lower() == region.region_name.lower():
         raise HTTPException(status_code=400, detail="Region name already exists")
      
   db_tbl_insert_region()
   
   return {"message": "Region created successfully"}

@app.post('/api/v1/region/{region_id}', dependencies=[Depends(verify_api_key)])
def update_region(region: Region, region_id: int = None):
   
   if region_id is None or region_id == "":
      raise HTTPException(status_code=400, detail="Region ID is missing")
   
   if not region.region_name:
      raise HTTPException(status_code=400, detail="Region name is missing")

   region.region_id = region_id

   print(region.region_id)

   def db_tbl_list_region():
      db = func_db.Database()
      emps = db.list_region()
      return emps
   resRegion = db_tbl_list_region()

   def db_tbl_update_region():
      db = func_db.Database()
      emps = db.update_region(region.region_id, region.region_name)
      return emps
   
   for items in resRegion:
      if items["region_name"].lower() == region.region_name.lower():
         raise HTTPException(status_code=400, detail="Region name already exists")
      
   db_tbl_update_region()
   
   return {"message": "Region updated successfully"}

@app.get('/api/v1/region', response_model=PaginatedResponse, dependencies=[Depends(verify_api_key)])
def list_region(
   page: int = Query(1, ge=1), 
   per_page: int = Query(10, ge=1),
   name: Optional[str] = None):

   regions, total = get_filtered_regions(name, page, per_page)

   if not regions and page > 1:
      raise HTTPException(status_code=404, detail="No more records found")
   
   return {
      "total": total,
      "page": page,
      "per_page": per_page,
      "data": regions
   }

'''

Province

'''

@app.get('/api/v1/province/{province_id}', dependencies=[Depends(verify_api_key)])
def view_province(province_id):

   def db_tbl_view_province():
      db = func_db.Database()
      emps = db.view_province(province_id)
      return emps
   resProvince = db_tbl_view_province()
   
   return resProvince

@app.post('/api/v1/province', dependencies=[Depends(verify_api_key)])
def create_province(province: Province):

   if not province.province_name:
      raise HTTPException(status_code=400, detail="Province name is missing")
   
   if not province.region_id:
      raise HTTPException(status_code=400, detail="Region ID is missing")

   def db_tbl_list_province():
      db = func_db.Database()
      emps = db.list_province()
      return emps
   resProvince = db_tbl_list_province()

   def db_tbl_insert_province():
      db = func_db.Database()
      emps = db.insert_province(province.province_name, province.region_id)
      return emps
   
   for items in resProvince:
      if items["province_name"].lower() == province.province_name.lower() and items["region_id"] == province.region_id:
         raise HTTPException(status_code=400, detail="Province name already exists")
      
   db_tbl_insert_province()
   
   return {"message": "Province created successfully"}

@app.post('/api/v1/province/{province_id}', dependencies=[Depends(verify_api_key)])
def update_province(province: Province, province_id: int):
   
   province.province_id = province_id

   def db_tbl_list_province():
      db = func_db.Database()
      emps = db.list_province()
      return emps
   resProvince = db_tbl_list_province()

   def db_tbl_update_province():
      db = func_db.Database()
      emps = db.update_province(province_id, province.province_name)
      return emps
   
   for items in resProvince:
      if items["province_name"].lower() == province.province_name.lower() :
         raise HTTPException(status_code=400, detail="Province name already exists")
      
   db_tbl_update_province()
   
   return {"message": "Province updated successfully"}

@app.get('/api/v1/province', response_model=PaginatedResponseProvince, dependencies=[Depends(verify_api_key)])
def list_province(
   page: int = Query(1, ge=1), 
   per_page: int = Query(10, ge=1),
   name: Optional[str] = None,
   region_id: Optional[str] = None):

   provinces, total = get_filtered_provinces(name, region_id, page, per_page)

   if not provinces and page > 1:
      raise HTTPException(status_code=404, detail="No more records found")
   
   return {
      "total": total,
      "page": page,
      "per_page": per_page,
      "data": provinces
   }


if __name__ == "__main__":
   uvicorn.run("app_fast_api:app", host="0.0.0.0", port=8000, reload=True)
