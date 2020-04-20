import json
import mysql.connector
mydb = mysql.connector.connect(
  host="tnysystems.com",
  user="tnysyste_a2wp734",
  passwd="7SZ2s.8p]M",
  database="tnysyste_a2wp734"
)
mycursor = mydb.cursor()

with open('data.xml') as json_file:
    data = json.load(json_file)
    for p in data['response']:
        sql = "INSERT INTO COVID (country_name,new_cases,active_cases,serious_critical,total_recovered,cases,new_deaths,deaths, dayupdated) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
        val = (p['country'],p['cases']['new'],p['cases']['active'],p['cases']['critical'],p['cases']['recovered'],p['cases']['total'],p['deaths']['new'],p['deaths']['total'],p['day'])
        mycursor.execute(sql, val)
        mydb.commit()
print(mycursor.rowcount, "record inserted.")

with open('data.xml') as json_file:
    data = json.load(json_file)
    for p in data['response']:
        sql = "INSERT INTO COVID (country_name,new_cases,active_cases,serious_critical,total_recovered,cases,new_deaths,deaths, dayupdated) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
        val = (p['country'],p['cases']['new'],p['cases']['active'],p['cases']['critical'],p['cases']['recovered'],p['cases']['total'],p['deaths']['new'],p['deaths']['total'],p['day'])
        mycursor.execute(sql, val)
        mydb.commit()
print(mycursor.rowcount, "record inserted.")