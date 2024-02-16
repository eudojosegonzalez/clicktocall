#importamos la libreria para cargar los archivos de entorno
import dotenv


#importamos FASTAIP
from fastapi import FastAPI
from fastapi.responses import  RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi import APIRouter,Body,Path,Query, Depends
# dependencia que coinvierte los objetos tipo Bd a json
from fastapi.encoders import jsonable_encoder
#from fastapi import Path,Query, Depends
from fastapi.responses import JSONResponse


from datetime import datetime,timedelta

from typing import  List

# importamos el esquema de datos
from schemas.user import User



#Cargamos la documentacion de las rutas
app = FastAPI()
app.title='ClickToCall by 2Call'
app.version='V1.0'


# manejador de errores
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
	expose_headers=["*"],
	max_age=3600,
)



@app.get('/',tags=['Home'])
def home():
    # redireccionamos a la documentación de la API
    return RedirectResponse("/docs")


# Funcion para crear los datos personles de un usuario
@app.post ('/user/create_peticion',
tags=['Peticiones'],
responses=
    { 
        201: {
            "description": "Se creo la cita del usuario",
            "content": { 
                "application/json":{
                    "example":
                        {
                            "message":"Se creo la cita del usuario",
                            "newUserId":"1"
                        }
                    } 
                }       
            },
        403: {
            "description": "Forbiden",
            "content": { 
                "application/json":{ 
                    "example":
                        {
                            "message":"Not authenticated"
                        }
                    } 
                }       
            },             
        500: {
            "description": "Su session ha expirado",
            "content": { 
                "application/json":
                    { "example":
                        {
                            "message":"Su session ha expirado",
                            "estado":"Signature has expired"
                        }
                    } 
                }       
            },              
        520: {
            "description": "Ocurrió un error que no pudo ser controlado",
            "content": { 
                "application/json":
                    { "example":
                        {
                            "message":"Ocurrió un error que no pudo ser controlado",
                            "estado":"System Error"
                        }
                    } 
                }       
            },                       


    }
)
def create_peticion(usuario:User)->dict:
    estado=1

    if (estado=="1") :
        # se inserto el registro sin problemas
        newUserId=result["newUserId"]
        return JSONResponse (status_code=201,content={"message":"Se creo el usuario en el sistema","newUserId":newUserId})     
    elif  (estado=="-2"):
        # el username ya existe no puede volver a insertarlo
        userId=result["userId"]
        userName=result["userName"]
        return JSONResponse (status_code=409,content={"message":"Este Username ya fue registrado en el sistema, no puede volver a insertarlo","userId":userId,"userName":userName})     
    elif (estado=="-3"):
        userId=result["userId"]
        rut=result["rut"]
        return JSONResponse (status_code=422,content={"message":"Este RUT ya fue registrado en el sistema, no puede volver a insertarlo","userId":userId,"rut":rut})     

    else:
        return JSONResponse (status_code=520,content={"message":"Ocurrió un error que no pudo ser controlado","estado":result})     




