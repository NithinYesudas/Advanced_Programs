
import requests



options = {
    "Authorization": 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im5pdGhpbiIsImV4cCI6MTY4MTU2NzYyMSwidG9rZW5fdHlwZSI6ImFjY2VzcyJ9.KBASywnRNc0Dl_M8gvEQSlaw0Su_XsIsplxI0pHTrSI'
}
response = requests.get(
    "http://127.0.0.1:8000/user/me/", headers=options)
print(response.content)
