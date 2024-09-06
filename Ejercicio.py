def getTasks(priority,duration=0):
    task_db = {
        "high": [
            {"name":"Sacar al perro","duration":180},
            {"name":"Estudiar","duration":120}
        ],
        "medium": [
            {"name":"Hacer ejercicio","duration":60},
            {"name":"Sacar la basura","duration":45}
        ],
        "low": [
            {"name":"Jugar","duration":90},
            {"name":"Ver series","duration":45}
        ]
    }

    def filter_tasks(tasks):
        #definir la función de filtro usando filter y una función lambda
        return list(filter(lambda x: x["duration"] == duration, tasks))

    task_list = task_db.get(priority,[])  
    task_list = filter_tasks(task_list)

    def task_stream(index=0):
        if index < len(task_list):
            yield task_list[index]                      #head
            yield from task_stream(index+1)             #tail
    return task_stream()

#Prueba del stream de tareas por prioridad y duración:
priority = input("De qué prioridad desea ver las tareas?: ")
duration = int(input("Qué duración máxima?: "))
tasks_by_priority_duration = getTasks(priority,duration)

try:
    print(next(tasks_by_priority_duration))
    print(next(tasks_by_priority_duration))
except StopIteration:
    print("Son todos")