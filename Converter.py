import requests
import json

fromc = input("Enter from currency: ")
to = input("Enter to currency: ")
amount = input("Enter amount currency: ")
url = f"https://api.apilayer.com/fixer/convert?to={to}&from={fromc}&amount={amount}"


def validate_names():  # Проверка
    if len(fromc) or len(to) != 3:
        print("Неверный формат, попробуйте снова")
    else:
        return "ok"


payload = {}
headers = {
  "apikey": "3x8h3ELNU3M5JQLSwgG4rBxUovHGVtZ1"
}

response = requests.request("GET", url, headers=headers, data=payload)
result = response.text
json_data = json.loads(result)
print("result:", json_data["result"])
