import requests
import json

new_author = {
    "name": "Elon Musk",
    "nationality": "American",
    "phone": "555-215-555",
    "email": "elon@musk.com"
}

# new_post = {
#     "date": "2023-04-02",
#     "title": "such title",
#     "text": "very text",
#     "authors": "8,9"
# }

r = requests.post('http://localhost:5000/api/authors/new', json=new_author)
# r = requests.post('http://localhost:5000/api/posts/new', json=new_post)
print(json.loads(r.text))
