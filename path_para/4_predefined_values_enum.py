#if you want the possible valid path parameter values to be predefined,can use a standard Python Enum

#import Enum
from enum import Enum

from fastapi import FastAPI

#create a sub-class that inherits from str and from Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()


@app.get("/models/{model_name}")

#declare a path parameter using the enum class
async def get_model(model_name: ModelName):

    #compare with the enum member with ModelName
    if model_name == ModelName.alexnet:
        
        #return enum members,even nested in a JSON body (e.g. a dict)
        #They'll be converted to their corresponding values(string) before returning to the client
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    #get actual value using model_name.value or your_enum_member.value : ModelName.lenet.value
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
