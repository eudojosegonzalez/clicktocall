
#importamos FASTAIP
from fastapi import FastAPI, Request
from fastapi.responses import  RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import requests


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
        200: {
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
def create_peticion(idTask: str = Body(), rut: str = Body(),telefono:str = Body(), sucursal:str = Body() , horario:int = Body(), correo:str = Body(), comentario: str = Body())->dict:
    estado=1

    data={
        "idTask":6,
        "rut": rut,        
        "telefono": telefono,
        "sucursal": sucursal,
        "horario": horario,
        "correo": correo,
        "comentario": comentario        
    }


    response = requests.get("http://192.168.10.30/neoapi/webservice.asmx/ExecuteTask06", params=data)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Procesar la respuesta
        data = response.json()
    else:
        # Manejar el error
        print(response.status_code)
        print(response.headers)
        print(response.text)    

        '''if (estado==1) :
            # se inserto el registro sin problemas
            return JSONResponse (status_code=201,content={"message":"Se creo la peticion en el sistema","data":data})     
        else:
            return JSONResponse (status_code=520,content={"message":"Ocurrió un error que no pudo ser controlado"})   '''  




