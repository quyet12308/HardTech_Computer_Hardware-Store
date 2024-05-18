from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    ForeignKey,
    Numeric,
    func,
    MetaData,
    Table,
    text,
    select,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    order_date = Column(DateTime, server_default=func.now())
    order_status = Column(String)
    total_price = Column(Numeric)
    shipping_address = Column(String)
    payment_method = Column(String)
    user = relationship("User", backref="orders")

    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


engine = create_engine("sqlite:///orders.db")
Session = sessionmaker(bind=engine)
session = Session()

# Thêm cột `updated_at` vào bảng hiện có
Base.metadata.alter(Order, table_args={"extend_existing": True})
session.commit()
