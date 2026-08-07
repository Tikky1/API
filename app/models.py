from pydantic import BaseModel, Field, field_validator

class Task(BaseModel):
    id:int
    title:str = Field(min_length=3, max_length=200)
    done:bool=False
    priority:int = Field(default=3, ge=1, le=5)
    internal_note:str = ""
    
    
    @field_validator("title")
    @classmethod
    def strip_title(cls, title: str) -> str:
        temiz=title.strip()
        if temiz == "":
            raise ValueError("Başlık sadece boşluktan oluşmaz")
        return temiz

class TaskCreate(BaseModel):
    title:str
    done:bool
    priority:int
    
class TaskOut(BaseModel):
    id:int
    title:str
    done:bool
    priority:int
    