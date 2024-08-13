from faker import Faker
import json


def generate_customer_data(file_path):
    fake = Faker()
    data = []
    information = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'password': fake.password(),
    }
    data.append(information)
    with open(f'{file_path}/customer_data.json', 'w') as f:
        json.dump(data, f)
