import json
# li = [
#   {
#      "CityId": 18,
#        "CityName": "西安",
#       "ProvinceId": 27,
#        "CityOrder": 1
#    },
#    {
#        "CityId": 53,
#        "CityName": "广州",
#        "ProvinceId": 27,
#        "CityOrder": 1
#    }]
# f=open("city.json","w")
# json.dump(li,f)
# f.close()
f=open("city.json","r")
li3=json.load(f)
print(li3)