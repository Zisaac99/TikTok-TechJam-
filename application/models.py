from application import db, login
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__='user'

    # User table columns

    # Primary Key
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    accountId = db.Column(db.Integer)
    fullname = db.Column(db.String(1000))
    email = db.Column(db.String(1000))
    username = db.Column(db.String(1000))
    password = db.Column(db.String(1000))
    fullname = db.Column(db.String(1000))
    balance = db.Column(db.String(1000))

    # Establish relationship with transaction table
    transaction = db.relationship('Transaction')

    def get_id(self):
        return (self.user_id)
    
# Transaction Table
class Transaction(db.Model):
    __tablename__ ='transaction'

    # Transaction table columns

    # Primary Key
    transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.String(1000))
    type = db.Column(db.String(1000))
    accountId = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True))
    # Foreign Key
    fk_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

class ATM(db.Model):
    __tablename__ ='atm'

    # Transaction table columns

    # Primary Key
    atm_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    atmNumber = db.Column(db.Integer)
    withdrawAmount = db.Column(db.Integer) # store balance as string will convert back for calculation

# Code Table
class Code(db.Model):
    __tablename__ ='code'

    # Code table columns

    # Primary Key
    code_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(1000))
    amount = db.Column(db.String(1000))
    isActivated = db.Column(db.Boolean)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
