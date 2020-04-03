import factory
import factory.django
from ActivityPeriod.models import User

#The Faker class to generate fake data
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    name = factory.Faker('name')
    userId = factory.Faker('random_number')
    userTimeZone = factory.Faker('timezone')