import os
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'maharaja-netflix'
    SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL') or 'mysql://root:root@localhost/register'
    SQLALCHEMY_TRACK_MODIFICATION = False