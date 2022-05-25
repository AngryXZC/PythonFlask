from application import app,db
from www import*
if __name__=="__main__":
    #建立表
    db.create_all()
   # app.run(host="0.0.0.0",debug=True)