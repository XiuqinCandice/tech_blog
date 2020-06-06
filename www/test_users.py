import asyncio
import orm
from models import User, Blog, Comment

loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(user='www-data', password='www-data', db='tech_blog', loop=loop)

    #u = User(name='Test', email='test3@example.com', passwd='14567890', image='about:blank')
    c = Comment(blog_id = '2', user_id = '3', user_name = 'test5', content = 'Text', user_image = 'about:blank')

   # await u.save()
    await c.save()

loop.run_until_complete(test())


