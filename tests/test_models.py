from tests import TestCaseBase
from core import models
import datetime


class Address(models.Model):
    type = models.StringProperty()  # E.g., 'home', 'work'
    street = models.StringProperty()
    city = models.StringProperty()
    is_active = models.BooleanProperty()


class TestModel(models.Model):
    name = models.StringProperty()
    title = models.StringProperty(default='Implicit Title')
    jive = models.StringProperty(repeated=True)
    total = models.StringProperty()
    addresses = models.StructuredProperty(Address, repeated=True)
    data = models.JsonProperty()

    birthday = models.DateTimeProperty()
    is_cool = models.BooleanProperty()
    is_uncool = models.BooleanProperty(default=True)


def funco():
    pass


class ModelPropertyTests(TestCaseBase):

    def test_default(self):
        # Implicitly Setting Title
        m = TestModel(name='Explicit Name')
        self.assertEqual(m.name, 'Explicit Name')
        self.assertEqual(m.title, 'Implicit Title')

        # Explicitly Setting Title
        m.title = 'Explicit Title'
        self.assertEqual(m.title, 'Explicit Title')

    def test_derp(self):
        m = TestModel(title='cheese', name='booger', total='666')
        m.jive = ['a', 's', 'd']

        m.addresses = [
            Address(city='MPLS'),
            Address(city='Barron')
        ]
        m.data = {'frog': funco}

        now = datetime.datetime.now()
        m.birthday = now

        # Test non-property attribute
        m.benga = 'cornpone'

        self.assertEqual(m.name, 'booger')
        self.assertEqual(m.total, '666')
        self.assertEqual(m.title, 'cheese')
        self.assertEqual(m.jive, ['a', 's', 'd'])
        self.assertEqual(m.is_cool, None)
        self.assertEqual(m.is_uncool, True)
        self.assertEqual(m.birthday, now)

        # raise Exception(m._properties)
