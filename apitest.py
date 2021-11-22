import requests

def test_country():          #test to see if country for given URL is united states
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["country"] == 'United States'

#print(test_country())


def test_country_abbreviation():            #test to see if the country abbreviation is US 
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body['country abbreviation'] == 'US'

#print(test_country_abbreviation())