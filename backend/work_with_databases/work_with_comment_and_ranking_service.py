from Database_initialization_and_structure import *
from sqlalchemy import desc
from setting import *


def get_user_comments(user_id, limit):
    # Tạo engine và session
    engine = create_engine(f"sqlite:///{DATA_BASE_PATH}")
    Session = sessionmaker(bind=engine)
    session = Session()
    # Truy vấn cơ sở dữ liệu để lấy ra các comment của người dùng theo user_id và giới hạn số lượng bằng limit
    comments = (
        session.query(Comment)
        .filter(Comment.user_id == user_id, Comment.is_deleted == False)
        .order_by(desc(Comment.created_at))
        .limit(limit)
        .all()
    )

    return comments
