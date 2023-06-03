
import requests
from datetime import datetime,timedelta
result = requests.post("http://3.133.142.121:8989/user/signup", data={"email": "nithinypadickal@gmail.com",
                                                                      "password": "12345678"})
print(result.json())
