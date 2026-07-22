from supabase import create_client
import os
from dotenv import load_dotenv
from faker import Faker
import random

# loading the variables
load_dotenv()

# reading the variables
url = os.getenv("supabase_url")
key = os.getenv("supabase_key")

# initializing the client
supabase = create_client(url, key)

mock_data = []
fake = Faker()

# apartments
for _ in range(50):
    
    apartment = {
        'title': f"{fake.word().capitalize()} Apartment",
        'neighborhood': fake.city_suffix(),
        'address': fake.street_address(),
        'price': round(random.uniform(150000, 850000), 2),
        'bedrooms': random.randint(1, 5),
        'bathrooms': random.choice([1.0, 1.5, 2.0, 2.5, 3.0]),
        'sqft': random.randint(500, 3500),
        'year_built': random.randint(1950, 2023),
        'renovation_year': random.choice([None, random.randint(2010, 2024)]),
        'charm_score': random.randint(1, 10),
        'has_fireplace': random.choice([True, False]),
        'listing_status':random.choice(['active', 'pending', 'sold'])
        }

    mock_data.append(apartment)

response = supabase.table('apartments').insert(mock_data).execute()

print('Data inserted successfully!')
