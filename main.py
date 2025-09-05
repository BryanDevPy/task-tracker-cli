import json
from pathlib import Path

AGENDA_FILE = Path('agenda.json')

def load_agenda():
    """
    Carga la agenda desde el archivo JSON.
    - Si el archivo existe, devuelve el diccionario de contactos.
    - Si no existe, devuelve un diccionario vacío {}
    - Si el archivo está corrupto (ej: contenido inválido), también devuelve {}.
    """
    if AGENDA_FILE.exists():
        try:
            with open(AGENDA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f) # -> {{}}
        except json.JSONDecodeError:
            # Archivo corructo o vacío: arrancamos con un diccionario vacío
            return {}
    return {}

def get_id(agenda: dict) -> str:
    """ Generates a new incremental ID based on the calendar keys.
    Args:
        calendar (dict): Dictionary of tasks, where the keys are IDs in string format.
    Returns:
        str: New ID as a string.
    """
    new_id = max(map(int, agenda), default=0) + 1
    return str(new_id)

def add_task(description: str):
    """ Agrega una nueva tarea a la agenda.

    La función carga la agenda desde el archivo JSON,
    genera un nuevo ID para la tarea y la guarda 
    con estado "todo"

    Args:
        description (str): Descripción de la tarea.

    Returns: None
    """
    task = load_agenda() # Cargamos el dict actual
    task_id = get_id(task) # Obtenemos el id disponible

    content_task = {
        'description':description,
        'status':'todo',
        'createdAt':True,
        'updatedAt':False
    }

    task[task_id] = content_task # Insertamos la nueva tarea

    # Persistimos la agenda actualizada en el archivo
    with open(AGENDA_FILE, 'w', encoding='utf-8') as f:
        json.dump(task, f, ensure_ascii=False, indent=4)

def update_task(id):
    pass

def delete_task(id):
    pass

def mark_task(arg, id):
    pass

def list_task():
    for k, v in all_task.items():
        if v["updatedAt"]:
            print(f'ID: {k}\nCreation date: {v["createdAt"]}\nUpdate date: {v["updatedAt"]}')
        else:
            print(f'ID: {k}\nCreation date: {v["createdAt"]}')
        print(f'Description: {v["description"]}')
        print(f'Status: {v["status"]}')
        print('='*100)
        

def main():
    add_task('descripción para test')

if __name__ == '__main__':
    main()