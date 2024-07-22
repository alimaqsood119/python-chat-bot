import requests

def get_gemini_data(query):
    url = 'https://api.gemini.com/v1/ai/query'
    headers = {
        'Authorization': 'AIzaSyBA8RsDsqs0juKRnXQvXOqnoGMz7Ygtp6c',
        'Content-Type': 'application/json'
    }
    payload = {
        'query': query
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def main():
    query = input("Enter your query: ")
    result = get_gemini_data(query)
    if result:
        print("Gemini AI Response:")
        print(result)

if __name__ == "__main__":
    main()
