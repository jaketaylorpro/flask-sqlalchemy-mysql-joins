# config = {
#     'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://'
#                                'root:'
#                                'ricultTest@'
#                                'ricult-test-db.cu1axvaq2cpb.us-east-1.rds.amazonaws.com:'
#                                '3306/'
#                                'test'
# }
config = {
    'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://'
                               'root@'
                               'outside:'
                               '3306/'
                               'testdb',
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    'SQLALCHEMY_ECHO': True

}

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'\
                               'root@'\
                               'outside:'\
                               '3306/'\
                               'testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True