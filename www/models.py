import time
# uuid是python中生成唯一的ID的库
import uuid
from orm import Model,StringField,BooleanField,FloatField,TextField

# 生成一个基于时间的唯一的id，作为数据库的主键
def next_id():
    #time.time()  return now time ts
    #uuid4() -- random num Have a chance to repeat
    return "%015d%s000" % (int(time.time()*1000),uuid.uuid4().hex)

#用户表
class User(Model):
    __table__ = "user"
    id = StringField(primary_key=True, default=next_id(),ddl="varchar(50)")
    email = StringField(ddl="varchar(50)")
    passwd = StringField(ddl="varchar(50)")
    admin = BooleanField() #isAdmin
    name = StringField(ddl="varchar(50)") #姓名
    image = StringField(ddl="varchar(500)") #头像
    created_at = FloatField(default=time.time) #创建时间默认为当前时间

#博客表
class Blog(Model):
    __table__ = "blogs"
    id = StringField(primary_key=True, default=next_id(), ddl="varchar(50)")
    user_id = StringField(ddl="varchar(50)") # 作者id
    user_name = StringField(ddl="varchar(50)")  # 作者名
    user_image = StringField(ddl="varchar(500)")  # 作者上传的图片
    name = StringField(ddl="varchar(50)")  # 文章名
    summary = StringField(ddl="varchar(200)")  # 文章概要
    content = TextField()  # 文章正文
    created_at = FloatField(default=time.time)

#评论表
class Comment(Model):
    __table__ = "comments"
    id = StringField(primary_key=True, default=next_id())
    blog_id = StringField(ddl="varchar(50)")  # 博客id
    user_id = StringField(ddl="varchar(50)")  # 评论者id
    user_name = StringField(ddl="varchar(50)")  # 评论者名字
    user_image = StringField(ddl="varchar(500")  # 评论者上传的图片
    content = TextField()
    created_at = FloatField(default=time.time)