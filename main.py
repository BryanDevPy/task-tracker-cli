import json
import argparse
from pathlib import Path
from datetime import datetime

AGENDA_FILE = Path('agenda.json')

def get_date() -> str:
    """Genera la fecha y hora actuales en formato legible.

    Returns:
        str: Cadena con el formato 'Day, DD of Month YYYY at HH:MM AM/PM.
    """
    brand_temporal = datetime.now()
    format_date = brand_temporal.strftime("%A, %d of %b %Y at %I:%M %p.")
    return format_date

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
    createdAt = get_date() # Obtenemos la fecha actual
    task = load_agenda() # Cargamos el dict actual
    task_id = get_id(task) # Obtenemos el id disponible

    content_task = {
        'description':description,
        'status':'todo',
        'createdAt':createdAt,
        'updatedAt':False
    }

    task[task_id] = content_task # Insertamos la nueva tarea

    # Persistimos la agenda actualizada en el archivo
    with open(AGENDA_FILE, 'w', encoding='utf-8') as f:
        json.dump(task, f, ensure_ascii=False, indent=4)
    
    print(f'Tarea agregada con éxito (ID: {task_id})')

def update_task(id_task: str, new_description: str = None):
    """ Actualiza la descripción de una tarea.

    Args:
        id_task (str): Id de la tarea a actualizar.
        new_description (str): Nueva descrición de la tarea.

    Returns:
        None 
    """
    updatedAt = get_date() # Obtenemos la fecha actual
    
    with open(AGENDA_FILE, 'r', encoding='utf-8') as f:
        agenda = json.load(f)

    if id_task in agenda:
        agenda[id_task]['updatedAt'] = updatedAt # Agregamos la fecha actualizada

        if new_description:
            agenda[id_task]['description'] = new_description # Agregamos la nueva descripción
    else:
        print('Tarea no encontrada.')

    
    
    with open(AGENDA_FILE, 'w', encoding='utf-8') as f:
        json.dump(agenda, f, ensure_ascii=False, indent=4)

def delete_task(id_task: str):
    """Elimina una tarea de la agenda.

    Args:
        id_task (str): id de la tarea a eliminar.
    
    Returns:
        None
    """
    with open(AGENDA_FILE, 'r', encoding='utf-8') as f:
        agenda = json.load(f)

    if id_task in agenda:
        del agenda[id_task]
        print(f'Tarea {id_task} eliminada')
    else:
        print('Tarea no encontrada.')
    
    with open(AGENDA_FILE, 'w', encoding='utf-8') as f:
        json.dump(agenda, f, ensure_ascii=False, indent=4)

def mark_task(arg: str, id_task: str):
    """Actualiza el status de la tarea y su fecha de modificación.

    Args:
        arg (str): status de la tarea.
        id_task (str): id de la tarea a marcar.
    
    Returns:
        None
    """
    update_task(id_task)
    
    with open(AGENDA_FILE, 'r', encoding='utf-8') as f:
        agenda = json.load(f)

    agenda[id_task]['status'] = arg # Agregamos el nuevo status
    
    with open(AGENDA_FILE, 'w', encoding='utf-8') as f:
        json.dump(agenda, f, ensure_ascii=False, indent=4)

def list_task(arg: str = None):
    """Lista las tareas almacenadas en la agenda, filtrando por estado opcional.

    Args:
        arg (str, optional): Estado de la tarea a filtrar. 
                             Puede ser 'todo', 'in-progress', 'done' o None para mostrar todas.
    """
    with open(AGENDA_FILE, 'r', encoding='utf-8') as f:
        agenda = json.load(f)

    for k, v in agenda.items():

        if arg and v['status'] != arg:
            continue

        print(f'ID: {k}')
        print('-'*115)
        if v["updatedAt"]:
            print(f'Create date: {v["createdAt"]:<} {"|":^10} Update date: {v["updatedAt"]:>}')
        else:
            print(f'Creation date: {v["createdAt"]}')
        print('-'*115)
        print(f'* Description: {v["description"]}')
        print(f'* Status: {v["status"]}')
        print('='*115)
        

def main():
    parser = argparse.ArgumentParser(prog='task-cli', description='task manager')

    subparser = parser.add_subparsers(dest='command', help='comandos disponibles')

    # subcomando 'add'
    parser_add = subparser.add_parser('add', help='agrega una tarea.')
    parser_add.add_argument('description', type=str, help='descripción de la tarea.')

    # subcomando 'update'
    parser_update = subparser.add_parser('update', help='actualiza una tarea.')
    parser_update.add_argument('id_task', type=str, help='id de la tarea.')
    parser_update.add_argument('description', type=str, help='nueva descripción de la tarea.')

    # subcomando 'delete'
    parser_delete = subparser.add_parser('delete', help='elimina una tarea.')
    parser_delete.add_argument('id_task', type=str, help='id de la tarea.')

    # subcomando 'mark-in-progress'
    parser_mark_in_progress = subparser.add_parser('mark-in-progress', help='marca la tarea como en progreso.')
    parser_mark_in_progress.add_argument('id_task', type=str, help='id de la tarea.')

    # subcomando 'mark-done'
    parser_mark_done = subparser.add_parser('mark-done', help='marca la tarea como terminada.')
    parser_mark_done.add_argument('id_task', type=str, help='id de la tarea.')

    # subcomando 'list'
    parser_list = subparser.add_parser('list', help='lista todas las tareas.')
    parser_list.add_argument('-m', choices=['todo', 'in-progress', 'done'])

    args = parser.parse_args()

    # CLI
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id_task, args.description)
    elif args.command == 'delete':
        delete_task(args.id_task)
    elif args.command == 'mark-in-progress':
        mark_task('in-progress', args.id_task)
    elif args.command == 'mark-done':
        mark_task('done', args.id_task)
    elif args.command == 'list':
        if args.m == 'in-progress':
            list_task(args.m)
        elif args.m == 'done':
            list_task(args.m)
        elif args.m == 'todo':
            list_task(args.m)
        else:
            list_task()

if __name__ == '__main__':
    main()