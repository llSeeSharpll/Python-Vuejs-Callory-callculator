import jwt
import sys

from sqlalchemy.sql.expression import null
from datetime import datetime, timedelta
from sqlalchemy import and_, or_, update
from datetime import date
sys.path.append('../')
from entities.user import App_User,Food_User
from entities.databaseSessionManager import SessionManager

JWT_EXP_DELTA_SECONDS = 20
SESSION_TIMEOUT_IN_HOURS = 24


class Item_User():
    dbSession = SessionManager().session


    def SaveFood(self,username,name,fat,prot,carb,callories):
        if username is not None:
            user_id=self.dbSession.query(App_User.userId).filter_by(username=username).first()
            datetoday = date.today()
            newFood = Food_User(userId=user_id[0],name=name,fat=fat,prot=prot,carb=carb,callories=callories,date=datetoday)
            self.dbSession.add(newFood)
            self.dbSession.commit()
            return True
        return False

    def GetFood(self, username):
        if username is not None:
            user_id = self.dbSession.query(App_User.userId).filter_by(username=username).first()
            datetoday = date.today()
            Foods= self.dbSession.query(Food_User.name,Food_User.fat,Food_User.prot,Food_User.carb,Food_User.callories).filter_by(date=datetoday).filter_by(userId=user_id[0]).all()
            return Foods
        return null

    def GetDetail(self,username):
        if username is not None:
            user_id = self.dbSession.query(App_User.userId).filter_by(username=username).first()
            Details = self.dbSession.query(App_User.gender,App_User.weight,App_User.height,App_User.age).filter_by(userId=user_id[0]).all()
            return Details
        return null

    def UpdateHeight(self,username,height):
        if username is not None:
            user_id = self.dbSession.query(App_User.userId).filter_by(username=username).first()
            self.dbSession.query(App_User.height).update({App_User.height: height})
            self.dbSession.commit()
            return True
        return null

    def UpdateWeight(self,username,weight):
        if username is not None:
            user_id = self.dbSession.query(App_User.userId).filter_by(username=username).first()
            self.dbSession.query(App_User.weight).update({App_User.weight: weight})
            self.dbSession.commit()
            return True
        return null

    def UpdateAge(self,username,age):
        if username is not None:
            user_id = self.dbSession.query(App_User.userId).filter_by(username=username).first()
            self.dbSession.query(App_User.age).update({App_User.age: age})
            self.dbSession.commit()
            return True
        return null