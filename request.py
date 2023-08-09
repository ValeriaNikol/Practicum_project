import requests as requests
import configuration
import data


def new_order_body(field, name):
    create_body = data.order_body.copy()
    create_body[field] = name
    return create_body


def create_order():
    return requests.post(url=configuration.URL + configuration.CREATE_ORDER_PATH, json=new_order_body("field", "name"), 
                         headers=data.order_headers)


response_create_order = create_order()
print(response_create_order.status_code)
print(response_create_order.json()['track'])

track_code = response_create_order.json()['track']
url_track = {'t': track_code}
        

def get_order_info():
    return requests.get(url=configuration.URL + configuration.GET_ORDER_INFO_PATH, params=url_track)

response_get = get_order_info()
print(response_get.status_code)
print(response_get.json())