import factory
from django.contrib.auth.models import User

from blog.models import Post

class UserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = User
    
    username = "test"
    password = "test"
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Post
    
    title = "x"
    subtitle = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    status = 'published'
    
    # title = factory.Faker('sentence', nb_words=4)
    # subtitle = factory.Faker('sentence', nb_words=6)
    # slug = factory.Faker('slug')
    # author = factory.SubFactory('blog.tests.factory.UserFactory')
    # content = factory.Faker('text')
    # status = 'published'