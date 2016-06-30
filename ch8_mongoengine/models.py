import datetime
import mongoengine as me


class Review(me.EmbeddedDocument):
    stars = me.fields.IntField(default=0)
    date = me.fields.DateTimeField(default=datetime.datetime.now)


class Book(me.Document):
    title = me.fields.StringField(required=True)
    chapter_count = me.fields.IntField(default=0)
    price = me.fields.FloatField(required=True)
    published = me.fields.DateTimeField(default=datetime.datetime.now)
    reviews = me.fields.ListField(
        me.fields.EmbeddedDocumentField(Review)
    )

