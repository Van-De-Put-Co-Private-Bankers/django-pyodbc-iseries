# copied from django.tests.models.py
from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation,
)
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Square(models.Model):
    root = models.IntegerField()
    square = models.PositiveIntegerField()

    def __str__(self):
        return "%s ** 2 == %s" % (self.root, self.square)


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class SchoolClass(models.Model):
    year = models.PositiveIntegerField()
    day = models.CharField(max_length=9, blank=True)
    last_updated = models.DateTimeField()


class VeryLongModelNameZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ(models.Model):
    primary_key_is_quite_long_zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = models.AutoField(primary_key=True)
    charfield_is_quite_long_zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = models.CharField(max_length=100)
    m2m_also_quite_long_zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = models.ManyToManyField(Person, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=30)
    content_type = models.ForeignKey(ContentType, models.CASCADE, related_name='backend_tags')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Post(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    tags = GenericRelation('Tag')

    class Meta:
        db_table = 'CaseSensitive_Post'


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class ReporterProxy(Reporter):
    class Meta:
        proxy = True


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, models.CASCADE)
    reporter_proxy = models.ForeignKey(
        ReporterProxy,
        models.SET_NULL,
        null=True,
        related_name='reporter_proxy',
    )

    def __str__(self):
        return self.headline


class Item(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    last_modified = models.DateTimeField()

    def __str__(self):
        return self.name


class Object(models.Model):
    related_objects = models.ManyToManyField("self", db_constraint=False, symmetrical=False)

    def __str__(self):
        return str(self.id)


class ObjectReference(models.Model):
    obj = models.ForeignKey(Object, models.CASCADE, db_constraint=False)

    def __str__(self):
        return str(self.obj_id)


class RawData(models.Model):
    raw_data = models.BinaryField()


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Book(models.Model):
    author = models.ForeignKey(Author, models.CASCADE, to_field='name')


class BooleanTable(models.Model):
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(blank=True, default=False)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    country1 = models.CharField(max_length=2, blank=True)
    country2 = models.CharField(max_length=2, blank=True)
    country3 = models.CharField(max_length=2, blank=True)
    delete_code = models.CharField(max_length=1, default=' ')


class Country(models.Model):
    code = models.CharField(max_length=2)
