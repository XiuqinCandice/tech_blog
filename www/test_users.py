import asyncio
import orm
from models import User, Blog, Comment
from config import configs
loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(loop=loop, **configs['db'])
   # u = User(name='Test14', email='test14@example.com', passwd='1234567fa90', image='about:blank')
    b = Blog(user_id = '3', user_name = 'test5',user_image = 'about:blank', name='Blog1', summary = 'summary', content = 'Text' )
    #await u.save()
    await b.save()

loop.run_until_complete(test())


