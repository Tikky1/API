from fastapi import FastAPI
from fastapi import Body, Header


app = FastAPI()

tasks = [
    {"id": 1, "title": "nefes al", "done": True},
    {"id": 2, "title": "nefes ver", "done": False},
    {"id": 3, "title": "tekrar nefes al", "done": False},
]


@app.get("/task")
def list_tasks(
    done: bool | None = None,
    q: str | None = None,
    limit: int = 10,
    offset: int = 0,
):
    sonuc = []
    sonuc2 = []
    list = []
    low = []
    list.extend(tasks[offset:offset+limit])
            
    if done is not None:
        
        for task in list:
            
            if task["done"] == done:
                
                sonuc.append(task)

    if done is None:
        
        return list


    if not sonuc == []:
        if q is not None:
            L = q.lower()
            for task in sonuc:
                low = task["title"].lower()
                if L in low:
                    sonuc2.append(task)
            if sonuc2 == []:
                return sonuc
            else:
                return sonuc2
        if q is None:
            return sonuc

    return sonuc


@app.get("/task/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "bulunamadi"}
    
@app.post("/tasks")
def create_task(
    title: str = Body(),
    done: bool = Body(default=False),
    x_client_name: str | None = Header(default=None),
):
    tasks[]tasks.len()