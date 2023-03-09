import requests
import pytest


@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5),
    (4, 5, 9),
    (10, -3, 7),
])
def test_addition(num1, num2, expected):
    assert num1 + num2 == expected

# retrieving location data for a given country code and zip code (the first two elements in each tuple) and then asserting that the corresponding place name returned by the API is equal to the specified expected place name (the third tuple element).

test_data_zip_codes = [
    ("us", "90210", "Beverly Hills"),
    ("ca", "B2A", "North Sydney South Central"),
    ("it", "50123", "Firenze") 
]


@pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip_codes)
def test_using_test_data_object_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name