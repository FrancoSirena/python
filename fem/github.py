import requests

def create_query(languages, stars=50000):
  query_languages = ""
  for language in languages:
    query_languages += f"language:{language} "

  return f"{query_languages} stars:>{stars}"

def get_repositories(languages, sort="stars", order="desc"):
  query = create_query(languages)
  param = {"q": query, "sort": sort, "order": order}
  response = requests.get('https://api.github.com/search/repositories', params=param)
  status_code = response.status_code
  if status_code == 403:
    raise RuntimeError("Rate limit reached. Please wait a minute and try again.")
  elif status_code != 200:
    raise RuntimeError(f"An error has occurred, {status_code}")
  else:
    response_json = response.json()
    return response_json["items"]

if __name__ == "__main__":
  items = get_repositories(["ruby", "python", "javascript"])
  for item in items:
    print(f"Language: {item['language']}, starts: {item['stargazers_count']}, name: {item['name']}")