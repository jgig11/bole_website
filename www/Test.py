import orm
from models import User, Blog, Comment

def test():
    yield from orm.create_pool(host="10.104.20.123",user='developer', password='developer1015', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()
