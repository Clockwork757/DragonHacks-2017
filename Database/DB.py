#!/usr/bin/python3
import pymysql 

host = "wristtape.c0cqpjhdxjue.us-west-2.rds.amazonaws.com"
port = 3306
user = "Admin"
passwd = "adminpassword"
db = "WristTape"

class DB():
    def __init__(self):
        self._conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
        self._cur = self._conn.cursor()
        
    def execute(self, q, args = ()):
        self._cur.execute(q, args)
        
    def insert(self, q, args):
        self.execute(q, args)
        self._conn.commit()
        
    def fetchall(self):
        return self._cur.fetchall()
        
    def fetchone(self):
        return self._cur.fetchone()
    
    def get_UID(self, username):
        """
            Gets UID based on username
        """
        q = """SELECT UID from Users where username = %s"""
        self.execute(q, (username))
        return self.fetchone()[0]
        
    def check_user(self, username):
        """
            Checks if a user exists based on username
        """
        self.execute("SELECT username from Users")
        users = self._clean_list(self._cur.fetchall())
        return username in users
        
    def add_user(self, username, arm_length = None):
        """
            Adds a user with a given username and arm length
            Automatically assigns and returns their UID
        """
        if not self.check_user(username):
            q = """INSERT into Users(username, arm_length)
                    VALUES (%s, %s)"""
            self.insert(q ,(username,arm_length))
        
        return self.get_UID(username)
    
    def add_house(self, UID):
        """
            Adds a house with a given UID
            Returns new HID
        """
        q = """INSERT into Houses(UID)
                VALUES (%s)"""
        self.insert(q, UID)
        
        #Finds the HID of the House just added
        q = """SELECT HID FROM Houses
                ORDER BY HID DESC LIMIT 1"""
        
        self.execute(q)
        return self.fetchone()[0]
    
    def check_level(self, HID, level):
        """
            Checks if a house already contains a floor level
        """
        q = """SELECT level from Floors where HID = %s"""
        self.execute(q, HID)
        levels = self._clean_list(self.fetchall())
        return level in levels
        
    def add_floor(self, HID, level):
        """
            Adds a floor to a house with a given HID and level
            Returns new FID
        """
        if not self.check_level(HID, level):
            q = """INSERT into Floors(HID, level)
                    VALUES (%s, %s)"""
            self.insert(q, (HID, level))
            
        q = """SELECT FID FROM Floors
                where HID = %s and level = %s"""
        
        self.execute(q, (HID, level))
        return self.fetchone()[0] 
    
    def get_HIDs(self, UID):
        """
            Returns a list of HIDS that a user owns
        """
        q = """SELECT HID from Houses where UID = %s"""
        self.execute(q, UID)
        return self._clean_list(self.fetchall())
    
    def get_FIDs(self, HID):
        """
            Returns a list of FIDs from a given HID
        """
        q = """SELECT FID from Floors where HID = %s"""
        self.execute(q, HID)
        return self._clean_list(self.fetchall())
        
    def get_RIDs(self, FID):
        """
           Returns a list of RIDs from a given FID
        """
        q = """SELECT RID from Rooms where FID = %s"""
        self.execute(q, FID)
        return self._clean_list(self.fetchall())
        
    def get_room(self, RID):
        """
            Returns room data with a given room ID
        """
        q = """SELECT * from Rooms where RID = %s"""
        self.execute(q, RID)
        return self._clean_list(self.fetchall())
    
    def get_floor(self, HID, level):
        """
            Returns a FID from a given HID and level
        """
        q = """SELECT * from Floors where HID = %s and level = %s"""
        self.execute(q, (HID, level))
        return self.fetchone()[0]
        
    def add_room(self, room, FID):
        """
            Adds a room to the database
        """
        if room.type == 0:
            self._add_circle(room, FID)
        elif room.type == 1:
            self._add_rectangle(room, FID)
            
    def _add_circle(self, circle, FID):
        q = """INSERT into Rooms(TID, FID, radius, name)
            VALUES = (%s,%s,%s,"%s")"""
            
        TID = circle.type
        radius = circle.radius
        name = circle.name
        
        self.insert(q, (TID, FID, radius, name))
        
    def _add_rectangle(self, rectangle, HID, FID):
        q = """INSERT into Rooms(TID, FID, length, width, name)
            VALUES = (%s,%s,%s,%s,"%s")"""
            
        TID = rectangle.type
        length = rectangle.length
        width = rectangle.length
        name = rectangle.name
        
        self.insert(q, (TID, FID, radius, name))
        
    def _clean_list(self, bad_list):
        """
        Cleans up a list of single tuples and returns a 
        """
        clean = []
        for entry in bad_list:
            clean.append(entry[0])
        return clean

if __name__ == "__main__":
    db = DB()    
    UID = db.add_user("Wei")
    HIDs = db.get_HIDs(UID)
    HID = HIDs[0]
    FID = db.get_floor(HID, 1)
    print(FID)
