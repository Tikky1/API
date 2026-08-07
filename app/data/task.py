from models import Task
import sqlite3
from data.base import curs



def get_all():
    
    tasks=[]
    
    curs.execute("SELECT * FROM tasks")
    satirlar=curs.fetchall()
    
    for satir in satirlar:
        tasks.append(Task(**satir))
        
    return tasks
        