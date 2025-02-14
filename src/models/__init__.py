from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .customer import Customer
from .verification_token import VerificationToken
from .product import Product
from .store import Store
from .coupon import Coupon
from .payment_detail import PaymentDetail
from .shipping_address import ShippingAddress
from .payment_method import PaymentMethod
from .order import Order
from .status import Status