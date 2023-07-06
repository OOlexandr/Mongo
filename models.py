from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ReferenceField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Tag(EmbeddedDocument):
    name = StringField()


class Authors(Document):
    fullname = StringField()
    birthdate = DateTimeField()
    birthplace = StringField()
    description = StringField()

class Quotes(Document):
    tags = ListField(EmbeddedDocumentField(Tag))
    author = ReferenceField(Authors)
    quote = StringField()
    