import requests

url = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup" # сам запрос
token = "dict.1.1.20241218T091456Z.e992add9f25c3eee.4c207229ec58b56cf87ebf79c8bbbf0c02968fe3" # тут хранится мой api ключ
def translate_word(word: str):
    trans_word = ''
    params = {
        "key": token,
        "lang": "ru-en",
        "text": word
    }
    response = requests.get(url, params=params) # сейчас нет key, то есть ключа для api(сделать его в headers)

    if response.ok:
        data = response.json()
    else:
        print("Ошибка")
    trans_word = data['def'][0]["tr"][0]["text"]

    return trans_word