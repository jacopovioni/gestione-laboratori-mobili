from typing import Union
import webbrowser
from fastapi import FastAPI, HTTPException
from fastapi import Depends
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
import os
from http import HTTPStatus as stat
import xml.etree.ElementTree as ET
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel
import pymysql.cursors
import mysql.connector
import hashlib

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Consentire tutte le origini (o specifica le tue origini consentite)
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Specifica i metodi HTTP consentiti
    allow_headers=["*"],  # Consentire tutti gli header nelle richieste
)

SECRET = os.urandom(24).hex()
manager = LoginManager(SECRET, '/login', use_cookie=True)

fake_db = {"username": "admin", 'password': '1234'}

class User(BaseModel):
    password: str
    username : str

@manager.user_loader()
def load_user(user: str):  # could also be an asynchronous function
    nome_user = fake_db
    return nome_user

@app.get("/")
def read_item():
    with open("C:/Users/simon/OneDrive/Desktop/progetto prenotazioni/loggiii.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get("/prenotazioni")
def read_item():
    with open("C:/Users/simon/OneDrive/Desktop/progetto prenotazioni/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)



@app.post("/login")
async def registrazione(user: User):
    print(user.username, user.password)
    # Connessione al database MySQL su XAMPP
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='progetto_lab_mobili',
        port=3306,
    )

    cur = connection.cursor()
    salt = "5gz"    # Eseguire la query SQL utilizzando i valori JSON ricevuti
    psw=user.password+salt
    hashed = hashlib.md5(psw.encode())
    print(hashed.hexdigest())
    sql = f"""SELECT * FROM utenti WHERE username='{user.username}' AND psw='{hashed.hexdigest()}'"""
    cur.execute(sql)
    dati = cur.fetchall()
    print(dati)
    
    if dati == 'user':
        with open("C:/Users/simon/OneDrive/Desktop/progetto prenotazioni/homep_user.html", "r") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)
    elif dati== 'admin':
        with open("C:/Users/simon/OneDrive/Desktop/progetto prenotazioni/homep_admin.html", "r") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)
    else:
        # Se non ci sono righe interessate, solleva un'eccezione
        raise HTTPException(status_code=500, detail="Errore durante il login...nome utente non e/o password non valide")
    
@app.get("/homepage")
async def registrazione(user: User):
    print(user.username, user.password)
    # Connessione al database MySQL su XAMPP
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='progetto_lab_mobili',
        port=3306,
    )
    
    cur = connection.cursor()
    # Eseguire la query SQL utilizzando i valori JSON ricevuti
    sql = f"""SELECT tipo FROM utenti WHERE username='{user.username}' AND psw='{user.password}'"""
    cur.execute(sql)
    dati = cur.fetchall()
    print(dati)
    if dati == 'user':
        with open("C:/Users/simon/OneDrive/Desktop/progetto prenotazioni/homep_user.html", "r") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)
    else:
        with open("C:/Users/simon/OneDrive/Desktop/progetto prenotazioni/homep_admin.html", "r") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)




