import asyncio
from pydantic import PositiveInt, ValidationError, validate_arguments


@validate_arguments
async def get_user_email(user_id: PositiveInt):
    # `conn` is some fictional connection to a database
    email = await conn.execute('select email from users where id=$1', user_id)
    if email is None:
        raise RuntimeError('user not found')
    else:
        return email


async def main():
    email = await get_user_email(123)
    print(email)
    #> testing@example.com
    try:
        await get_user_email(-4)
    except ValidationError as exc:
        print(exc.errors())
        """
        [
            {
                'loc': ('user_id',),
                'msg': 'ensure this value is greater than 0',
                'type': 'value_error.number.not_gt',
                'ctx': {'limit_value': 0},
            },
        ]
        """


asyncio.run(main())
