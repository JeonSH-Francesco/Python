from flask import Flask, request
import sqlite3, random
#from datetime import datetime

# cursor.execute("create table good_click_table\
#         (no integer PRIMARY KEY AUTOINCREMENT, user_id varchar(12), user_pw varchar(32), cookie varchar(255), target integer,crawlingtime Datetime);"
#         )

#app 변수에 flask 모듈을 선언
app = Flask(__name__)
#request.json["Title"],request.json["content_body_text"]
@app.route("/test",methods=["GET","POST"])
def test():
    con = sqlite3.connect("2023-08-22_DarkwebCrawling.db")
    #cursor 변수는 DB 파일을 핸들링 하는 변수
    cursor=con.cursor()
    #print(request.args.get('a'))
    #print(request.json)
    #id=request.json["id"]
    #user_id=request.json["user_id"]
    try:
        cursor.execute("create table DarkWeb (Depth varchar(3),title varchar(30), url varchar(200),content varchar(500) )")
        
    except:
        pass
    cursor.execute("insert into DarkWeb values(?, ?,?,?)",\
    (request.json["Depth"], request.json["title"], request.json["url"], request.json["content"]
     )
    
    )
    print(request.json)
    con.commit()
    return "ok", 200

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8000)
