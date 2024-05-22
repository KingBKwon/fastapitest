from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # 허용할 origin을 설정하세요
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
class Settop_id(BaseModel):
    settop_num : str


@app.post('/login')
async def login(settop_id : Settop_id):
    user = {
        'user_list' : [
            {
            'user_name' : '이민정',
            'user_id' : 1
            },
            {   
            'user_name' : '이세숑',
            'user_id' : 2
            },  
            {   
            'user_name' : '이다빈',
            'user_id' : 3
            },  
            {   
            'user_name' : '막세민',
            'user_id' : 4
            }   
        ]
    }
    return JSONResponse(user)
