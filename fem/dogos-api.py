import requests

def get_shibes(count):
  api_url = "http://shibe.online/api/shibes"
  param = {"count": count}
  response = requests.get(api_url, params=param)

  status_code = response.status_code

  response_json = response.json()
  return (status_code, response_json)

if __name__ == "__main__":
  code, response = get_shibes(count=1)
  print(f"shibe found {response}")