# Schema de datos de Usuario
# se usa como interfaz de captura de Datos para luego
# pasar su contenido a el modelo de Usuario
from pydantic import BaseModel, Field
from typing import  Optional, List
from datetime import date, datetime

#clase que representa a un usuario en el sistema
class User(BaseModel):
    rut: str = Field (min_length=8, max_length=100)
    telefono: str = Field (min_length=9, max_length=9)
    sucursal : int = Field(ge=1, lt=100)
    horario : int = Field(ge=1, lt=13)
    correo: str = Field (min_length=5, max_length=250)
    comentario : str =Field (min_length=0, max_length=500)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "rut": "123456789-J",
                    "telefono":"123456789",
                    "sucursal" : 1,
                    "horario" : 1,
                    "correo": "jhonsmit@micorreo.cl",
                    "comentario" : "opcional"
                }
            ]
        }
    }    
