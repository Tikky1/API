from data.task import get_all 
from fastapi import Body, Header
from models import Task


tasks=get_all()


def task_getir(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return "hata"
    
    
    
    
    
def listele(
    done: bool | None = None,
    q: str | None = None,
    limit: int = 10,
    offset: int = 0,
):
    sonuc = []
    sonuc2 = []
    list = []
    low = []
    list.extend(tasks[offset:offset + limit])

    if done is not None:

        for task in list:

            if task.done == done:
                sonuc.append(task)

    if done is None:
        return list

    if not sonuc == []:
        if q is not None:
            L = q.lower()
            for task in sonuc:
                low = task.title.lower()
                if L in low:
                    sonuc2.append(task)
            if sonuc2 == []:
                return sonuc
            else:
                return sonuc2
        if q is None:
            return sonuc

    return sonuc





def task_üret(
    gorev: TaskCreate = Body(),
    x_client_name: str | None = Header(default=None),
):
    for task in tasks:
        if task.title == gorev.title:
            raise Duplicate("Aynı isimde 2 task bulunamaz")
    
    
    yeni_id = max((task.id for task in tasks), default=0) + 1

    yeni_task = Task(id=yeni_id, title=gorev.title, done=gorev.done, priority=gorev.priority)
    tasks.append(yeni_task)
    return yeni_task
    
    
    
    
    
def task_sil(task_id:int):
    Yanlis: bool = False
    for task in tasks:
        if task.id == task_id:
            Yanlis = True

    if Yanlis == False:
        raise Missing("Böyle bir task yok")

    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)





def düzelt(task_id: int, done: bool):
    for task in tasks:
        if task.id == task_id:
            task.done = done
            return task
            
            

class Missing(Exception):
    def __init__(self, message:str):
        self.message = message
        super().__init__(self.message)
        
class Duplicate(Exception):
    def __init__(self, message:str):
        self.message = message
        super().__init__(self.message)