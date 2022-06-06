from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
user = User(**external_data)
#**external_data : variable length keyword arguments
print(user.id)
#> 123
print(repr(user.signup_ts))
#repr() : returns the string representation of the value passed to eval function by default.
#> datetime.datetime(2019, 6, 1, 12, 22)
print(user.friends)
#> [1, 2, 3]
print(user.dict())
"""
{
    'id': 123,
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'friends': [1, 2, 3],
    'name': 'John Doe',
}
"""
#If validation fails pydantic will raise an error with a breakdown of what was wrong
try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())
