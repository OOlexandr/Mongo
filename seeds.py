import json
import datetime
import connect
from models import Tag, Authors, Quotes


with open('authors.json') as f:
    authors = json.loads(f.read())
    at = {}
    for i in authors:
        at[i["fullname"]] = Authors(
            fullname=i["fullname"],
            birthdate=datetime.datetime.strptime(i["born_date"], "%B %d, %Y"),
            birthplace=i["born_location"],
            description=i["description"]).save()
        

with open('quotes.json') as f:
    quotes = json.loads(f.read())

    for i in quotes:
        tags = []
        for t in i["tags"]:
            tags.append(Tag(name=t))
        Quotes(
            tags=tags,
            author=at[i["author"]],
            quote=i["quote"]).save()