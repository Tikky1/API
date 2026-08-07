from fastapi import FastAPI
from fastapi import Body, Header
from fastapi import HTTPException
from models import TaskCreate
from models import Task
from models import TaskOut
from service import task as service_task
from service.task import Duplicate, Missing
from fastapi import Depends, APIRouter



app = FastAPI()


# def zorunluluk(x_client_name:str=Header(default=None)):
    # print("test")
    # if x_client_name == None:
        # raise HTTPException(status_code=400, detail="x_client_name boş olamaz")

# , dependencies=[Depends(zorunluluk)]

router = APIRouter(prefix="/tasks", tags=["tasks"])



def common_params(q: str | None = None, limit:int=10, offset:int=0) -> dict:
    params = {"q":q, "limit":limit, "offset":offset}
    return params

@router.get("/", response_model=list[TaskOut])
def list_tasks(
        done: bool | None = None,
        params:dict=Depends(common_params)
):
    return service_task.listele(done,params)
    




@router.get("/{task_id}",response_model=TaskOut)
def get_task(task_id: int):
    return service_task.task_getir(task_id)




@router.post("/", status_code=201, response_model=TaskOut)
def create_task(
        gorev: TaskCreate = Body(),
        x_client_name: str | None = Header(default=None),
):
    try:
        return service_task.task_üret(gorev, x_client_name)
    except Duplicate:
        raise HTTPException(status_code=409, detail="Görev ismi var olan bir görev ismi ile çakışıyor")




@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    try:
        return service_task.task_sil(task_id)
    except Missing:
        raise HTTPException(status_code=404, detail="Bu id de bir task yok")




@router.patch("/{task_id}")
def patch(task_id: int, done: bool):
    return service_task.düzelt(task_id, done)