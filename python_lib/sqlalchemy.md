## Version Check(版本检查)

```
import sqlalchemy
sqlalchemy.__version__
'1.0.13'
```

---

## connecting(连接数据库)

```
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:test:', echo=True)
```

`echo` 参数是用来设置SQLAlchemy日志的,通过Python标准库logging模块实现.

-------

## Declare a Mapping

声明基类(declarative base class).

```
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

有了"base"之后,我们可通过他定义任何数量的映射类.

```
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String) 
    password = Column(String)
 
    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
```

---

## Create a Schema

通过Declarative系统构建了类之后,我们也定义了被称之为表的元数据信息.被SQLAlchemy用来为某特定的表呈现这些信息的对象被称之为Table对象,Declarative系统为我们实现了这些.我们可以通过检测 __table__ 参数来查看这个对象:如下: 

```
# 代码接上面
>> User.__table__ 
Table('users', MetaData(bind=None),
    Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
    Column('name', String(), table=<users>),
    Column('fullname', String(), table=<users>),
    Column('password', String(), table=<users>), schema=None)
```

`Table` 对象是一系列的元数据的组合.当使用Declarative的时候,这个对象可以使用我们declarative的基类的 `.metadata` 属性

创建数据库

```
>>> Base.metadata.create_all(engine)
SELECT ...
PRAGMA table_info("users")
()
CREATE TABLE users (
    id INTEGER NOT NULL, name VARCHAR,
    fullname VARCHAR,
    password VARCHAR,
    PRIMARY KEY (id)
)
()
COMMIT
```

---

## Create an Instance of the Mapped Class


声明完映射之后,我们来创建一个User对象,如下:

```
>>> ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
>>> ed_user.name
'ed'
>>> ed_user.password
'edspassword'
>>> str(ed_user.id)
'None'
```

---

## Creating a Session


定义Session

```
>>> from sqlalchemy.orm import sessionmaker
>>> Session = sessionmaker(bind=engine)
```

创建session

```
>>> session = Session()
```

---

## 添加／更新对象(Adding and Updating Objects)


为了持续操作(persist)我们的 `User` 对象,我们把他添加(`add()`)到会话中:

```
>>> ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
>>> session.add(ed_user)
```

我们可以使用`add_all()`函数一次性添加多个`User`对象:

```
>>> session.add_all([
...     User(name='wendy', fullname='Wendy Williams', password='foobar'),
...     User(name='mary', fullname='Mary Contrary', password='xxg527'),
...     User(name='fred', fullname='Fred Flinstone', password='blah')])

```

同样,我们如果觉得Ed的密码不太安全,也可以更改密码:

```
>>> ed_user.password = 'f8s7ccs'
```

而会话则时刻注意着这些变化,例如,他检测到了`Ed Jones`已经被更改了:

```
>>> session.dirty
IdentitySet([<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>])
```

同时,３个新的`User`对象处于等待提交的状态:

```
>>> session.new
IdentitySet([<User(name='wendy', fullname='Wendy Williams', password='foobar')>,
<User(name='mary', fullname='Mary Contrary', password='xxg527')>,
<User(name='fred', fullname='Fred Flinstone', password='blah')>])
```

提交会话

```
>>> session.commit()
```

---

## 回滚(Rolling Back)

```
>>> session.rollback()
```

----

## 查询(Quering)


一个`Query`对象是通过`Session`里的`query()`方法来创建的.这个方法有一些参数,参数可以是一些内置的类或者描述符.下面我们声明一个`User`实例的查询对象.当我们执行这些语句的时候,就可以看到`User`对象返回来的查询列表:

```
>>> for instance in session.query(User).order_by(User.id):
...     print(instance.name, instance.fullname)
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone
```

`Query`也可以接受ORM内置的描述符当参数,任何时候多个类实体或者基于列的实体也可以作为查询方法`query()`的参数,返回如下的结果:

```
>>> for name, fullname in session.query(User.name, User.fullname):
...     print(name, fullname)
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone
```

`Query`返回的结果称之为元组(tuples),通过`KeyedTuple`class实现,同时可以被当做Python的原生对象来处理.参数的名称和参数一样,类名和类一样(不知道咋翻译,原文: The names are the same as the attribute’s name for an attribute, and the class name for a class,看例子理解的意思就是:row对应的是User, 想获取name就使用row.name,这样row和row.name分别都有其对应的User,User.name了):

```
>>> for row in session.query(User, User.name).all():
...    print(row.User, row.name)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')> ed
<User(name='wendy', fullname='Wendy Williams', password='foobar')> wendy
<User(name='mary', fullname='Mary Contrary', password='xxg527')> mary
<User(name='fred', fullname='Fred Flinstone', password='blah')> fred
```

可以使用类元素衍生的一个对象`lable()`构造(construct)来给一列起另外的称呼,任何一个类的参数都可以这样使用(功能就像名字一样,打标签,起别名):

```
>>> for row in session.query(User.name.label('name_label')).all():
...    print(row.name_label)
ed
wendy
mary
fred
```

这里把这个名字给了`User`(实际上是给了User里的name),但是如果有两个参数呢(query()里有两个参数的情况,上面的例子只有一个)？可以使用`aliased()`来解决(和bash里的alias差不多):

```
>>> from sqlalchemy.orm import aliased
>>> user_alias = aliased(User, name='user_alias')

>>> for row in session.query(user_alias, user_alias.name).all():
...    print(row.user_alias)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
<User(name='wendy', fullname='Wendy Williams', password='foobar')>
<User(name='mary', fullname='Mary Contrary', password='xxg527')>
<User(name='fred', fullname='Fred Flinstone', password='blah')>
```

`Query`的基本操作包括了`LIMIT`和`OFFSET`,但是更简单的是使用Pyhton的切片或者更典型的是使用`ORDER_BY`:

```
>>> for u in session.query(User).order_by(User.id)[1:3]:
...    print(u)
<User(name='wendy', fullname='Wendy Williams', password='foobar')>
<User(name='mary', fullname='Mary Contrary', password='xxg527')>
```

过滤结果使用`filter_by()`来实现,使用的参数是关键字:

```
>>> for name, in session.query(User.name).filter_by(fullname='Ed Jones'):
...    print(name)
ed
```

或者使用`filter()`,`filter()`使用更灵活的SQL语句的结构来过滤.这可以让你使用规律的Python操作符来操作你映射的类参数:

```
>>> for name, in session.query(User.name).filter(User.fullname=='Ed Jones'):
...    print(name)
ed
```

`Query`对象是完全可繁殖的(fully generative),意味着大多数方法的调用都返回一个新的`Query`对象,此对象仍可进行查询操作,例如,你可以调两次`filter()`函数来查用户名为ed并且全名为Ed Jones的用户,相当于SQL中的AND操作:

```
>>> for user in session.query(User).\
...          filter(User.name=='ed').\
...          filter(User.fullname=='Ed Jones'):
...    print(user)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
```


---
## 常用过滤操作(Common Filter Operators)

这里是一份常用过滤操作的摘要:

* `equals`

```
query.filter(User.name == 'ed')
```

* `not equals`

```
query.filter(User.name != 'ed')
```

* `LIKE`

```
query.filter(User.name.like('%ed%'))
```

* `IN`

```
query.filter(User.name.in_(['ed', 'wendy', 'jack']))

# works with query objects too:
query.filter(User.name.in_(
        session.query(User.name).filter(User.name.like('%ed%'))
))
```

* `NOT IN`

```
query.filter(~User.name.in_(['ed', 'wendy', 'jack']))
```

* `IS NULL`

```
query.filter(User.name == None)

# alternatively, if pep8/linters are a concern
query.filter(User.name.is_(None))
```

* `IS NOT NULL`

```
query.filter(User.name != None)

# alternatively, if pep8/linters are a concern
query.filter(User.name.isnot(None))
```

* `AND`

```
# use and_()
from sqlalchemy import and_
query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))

# or send multiple expressions to .filter()
query.filter(User.name == 'ed', User.fullname == 'Ed Jones')

# or chain multiple filter()/filter_by() calls
query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')
```

* `OR`

```
from sqlalchemy import or_
query.filter(or_(User.name == 'ed', User.name == 'wendy'))
```

* `MATCH`

```
query.filter(User.name.match('wendy'))
```

**注意** `match()` 使用`MATCH` 或者 `CONTAINS` 来实现的,所以和数据库底层有关,在一些数据库下不能使用,比如说SQLite


---

## 查询返回的列表以及标量(Returning Lists and Scalars)

`Query`的一些函数立刻去执行SQL语句并返回数据库里的一些查询结果,这里有一个简短的介绍:

* `all()`返回一个列表:

```
>>> query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
>>> query.all()
[<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>,
      <User(name='fred', fullname='Fred Flinstone', password='blah')>]
```

* `first()` 对查询结果进行了一个限制-返回列表的第一个值:

```
>>> query.first()
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
```

* `one()`完全匹配所以行,如果匹配不到,则返回一个错误,或者匹配到多个值也会返回错误:

```
# 多个值
>>> user = query.one()
Traceback (most recent call last):
...
MultipleResultsFound: Multiple rows were found for one()

# 匹配不到
>>> user = query.filter(User.id == 99).one()
Traceback (most recent call last):
...
NoResultFound: No row was found for one()
```

`one()`对于那些希望分别处理查询不到与查询到多个值的系统是十分好的,比方说在RESTful API中,查询不到可能会返回404页面,多个结果则可能希望返回一个应用错误.

* `one_or_none()`和`one()`很像,除了在查询不到的时候.查询不到的时候`one_or_none()`会直接返回None,但是在找到多个值的时候和`one()`一样.

* `scalar()`援引自`one()`函数,查询成功之后会返回这一行的第一列参数,如下:

```
>>> query = session.query(User.id).filter(User.name == 'ed').\
...    order_by(User.id)
>>> query.scalar()
1
```
---

## 计数(Counting)

`Qurey`里包括了一个十分好用的的计数函数`count()`:

```
>>>session.query(User).filter(User.name.like('%ed')).count()
2
```

需要我们对每一项分别计数的时候,我们需要在`func`模块里通过`func.count()`来直接指定`count()`函数,下面我们可以单独计算一下每个名称的数量:

```
>>> from sqlalchemy import func
SQL>>> session.query(func.count(User.name), User.name).group_by(User.name).all()
[(1, u'ed'), (1, u'fred'), (1, u'mary'), (1, u'wendy')]
```

为了实现`SELECT count(*) FROM table`的功能,我们可以这样做:

```
>>> session.query(func.count('*')).select_from(User).scalar()
4
```

如果我们直接根据`User`的主键来计算,那么`select_from()`可以去掉:

```
>>> session.query(func.count(User.id)).scalar()
4
```
