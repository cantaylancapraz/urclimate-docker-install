import random
from locust import HttpUser, task

# Base Url: http://aa170d9ebd0754a32bbf6828444a5f12-201778709.eu-west-2.elb.amazonaws.com:8080
class MyUser(HttpUser):
    @task(1)
    def all(self):
        cord = generate_random_data(40.99, 25.78)
        lat = cord.get("lat")
        lon = cord.get("lon")
        url = "/static/monthly/location/all?latitude={}&longitude={}".format(lat, lon)
        headers = {
            "X-API-KEY": "45945433-cbbb-4b0b-be9f-183861f30579"
        }
        print(url)
        self.client.get(url, headers = headers)


    @task(4)
    def single(self):
        cord = generate_random_data(40.99, 25.78)
        lat = cord.get("lat")
        lon = cord.get("lon")
        url = "/static/monthly/location?datasetTypeId=1&latitude={}&longitude={}".format(lat, lon)
        headers = {
            "X-API-KEY": "45945433-cbbb-4b0b-be9f-183861f30579"
        }
        print(url)
        self.client.get(url, headers = headers)


def generate_random_data(lat, lon):
    dec_lat = random.random()/100
    dec_lon = random.random()/100
    return {
        "lat": lat+dec_lat,
        "lon": lon+dec_lon
    }
