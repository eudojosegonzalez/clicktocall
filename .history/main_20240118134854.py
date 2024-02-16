#importamos la libreria para cargar los archivos de entorno
import dotenv


#importamos FASTAIP
from fastapi import FastAPI
from fastapi.responses import  RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


#Importamos los archivos de conforuracion de la base de datos
from config.database import engine, Base


#importamos el routers
from routers.user import user_router
from routers.contacto import user_contact_router
from routers.ubicacion import user_ubicacion_router
from routers.files_users import files_user_router
from routers.pic_users import pic_user_router
from routers.bancarios_user import bancarios_user_router
from routers.bancos import bancos_router
from routers.afp import afp_router
from routers.basic_parameter import basic_parameter_router
from routers.eventos import eventos_router
from routers.nomina import nomina_router
from routers.sociedades import sociedades_router



#importamos el manejador de errores
from middleware.error_handler import ErrorHandler

#descripcion de los endpoints
tags_metadata = [
    {
        "name": "Auth",
        "description": "Operaciones de validación de usuario y generación de tokens",
    },
    {
        "name": "Usuarios",
        "description": "Operaciones relacionadas con los datos personales de los usuarios",
    },
    {
        "name": "Contacto",
        "description": "Operaciones relacionadas con los datos de contacto de los usuarios",
    },    
    {
        "name": "Localizacion",
        "description": "Operaciones relacionadas con los datos de localizacion de los usuarios",
    },     
    {
        "name": "Archivos de Usuarios",
        "description": "Operaciones relacionadas con los Archivos de los Usuarios",
    },    
    {
        "name": "Fotos de Usuarios",
        "description": "Operaciones relacionadas con las fotos de los Usuarios",
    },     
    {
        "name": "Bancarios Usuarios",
        "description": "Operaciones relacionadas con los datos de pago de los Usuarios",
    },        
    {
        "name": "Instituciones AFP",
        "description": "Operaciones relacionadas con las instituciones AFP",
    },    
    {
        "name": "Bancos",
        "description": "Operaciones relacionadas con las instituciones Bancarias",
    },
    {
        "name": "Parametros Basicos",
        "description": "Operaciones relacionadas con los Parámetros Básicos del Sistema",
    }, 
    {
        "name": "Eventos",
        "description": "Operaciones relacionadas con los Eventos de Nómina",
    },     
    {
        "name": "Nomina",
        "description": "Operaciones relacionadas con la Nómina",
    },     
            
]

#cargamos las variables de entorno
dotenv.load_dotenv()

#Cargamos la documentacion de las rutas
app = FastAPI(openapi_tags=tags_metadata)
app.title='Core B1 Nomina by Kyros'
app.version='V1.0'


# manejador de errores
app.add_middleware(ErrorHandler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
	expose_headers=["*"],
	max_age=3600,
)

#inclusión de los endpoints
app.include_router(user_router)
app.include_router(user_contact_router)
app.include_router(user_ubicacion_router)
app.include_router(files_user_router)
app.include_router(pic_user_router)
app.include_router(bancarios_user_router)
app.include_router(afp_router)
app.include_router(bancos_router)
app.include_router(basic_parameter_router)
app.include_router(eventos_router)
app.include_router(nomina_router)
app.include_router(sociedades_router)


# esto crea la base de datos si no existe al empezar la app
Base.metadata.create_all(bind=engine)


@app.get('/',tags=['Home'])
def home():
    # redireccionamos a la documentación de la API
    return RedirectResponse("/docs")


