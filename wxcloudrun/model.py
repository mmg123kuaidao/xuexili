from wxcloudrun import db

class LogisticsInfo(db.Model):
    __tablename__ = 'logistics_info'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(20), nullable=False)
    tracking_number = db.Column(db.String(50), nullable=False)
    courier_company = db.Column(db.String(50), nullable=False)
