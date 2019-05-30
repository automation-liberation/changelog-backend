from mongoengine import StringField, connect, Document

connect("changelog")


class ChangelogEntry(Document):
    service = StringField(required=True, max_length=200)
    version = StringField(required=True, max_length=25)
    header = StringField(required=True, max_length=50)
    body = StringField(required=True, max_length=255)
