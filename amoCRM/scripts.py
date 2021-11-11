import requests


def patch_contact(response, token):
    response = response.json()
    user_id = response["_embedded"]['contacts'][0]['id']
    patch = {"last_name": "luck"}
    response = requests.patch(f'https://zolberg68.amocrm.ru/api/v4/contacts/{user_id}',
                              headers=token, data=patch)
    response = response.json()
    return response


def create_lead(name, phone, email, token):
    post = [{"name": name,
             "custom_fields_values": [
                 {
                     "field_code": "PHONE",
                     "field_name": "Телефон",
                     "values": [
                         {
                             "value": phone,
                             "enum_code": "WORK"
                         }
                     ]
                 },
                 {
                     "field_code": "EMAIL",
                     "values": [
                         {
                             "value": email,
                             "enum_code": "WORK"
                         }
                     ]
                 }
             ]
             }]
    import json
    response = requests.post(f'https://zolberg68.amocrm.ru/api/v4/contacts',
                             headers=token, data=json.dumps(post))
    response = response.json()
    # created a lead
    user_id = response["_embedded"]['contacts'][0]['id']
    post = [{
        "_embedded": {

            "contacts": [
                {
                    "id": user_id
                }
            ]}

    }]
    response = requests.post(f'https://zolberg68.amocrm.ru/api/v4/leads',
                             headers=token, data=json.dumps(post))
    response = response.json()
    return response
