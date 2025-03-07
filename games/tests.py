from django.test import TestCase

from factory import DjangoModelFactory, Faker

from models import GoGame


class CompanyFactory(DjangoModelFactory):
    name = Faker('company')
    description = Faker('text')
    website = Faker('url')
    street_line_1 = Faker('street_address')
    city = Faker('city')
    state = Faker('state_abbr')
    zipcode = Faker('zipcode')

    class Meta:
        model = Company
