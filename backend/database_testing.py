from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from work_with_database import User, add_user, delete_user, update_user

# add_user(
#     username="user2",
#     address="",
#     email="",
#     fullname="",
#     img="",
#     is_admin=False,
#     password="user123",
#     phone_number="",
# )

# delete_user(user_id=2)

# new_data = {
#     "username": "new_username",
#     "email": "new_email@example.com",
#     "fullname": "New Fullname",
#     "phone_number": "987654321",
#     "address": "New Address",
#     "img": "new_image.jpg",
#     "is_admin": False,
# }

# update_user(user_id=3, new_data=new_data)