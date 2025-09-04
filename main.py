all_task = {
    '1': {
        'description':'Task Test 1',
        'status':'todo',
        'createdAt':True,
        'updatedAt':False
    },
    '2': {
        'description':'Task Test 2',
        'status':'in-progress',
        'createdAt':True,
        'updatedAt':True
    },
}
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
    task_id = get_id(all_task)
    new_task = {
        'description':description,
        'status':'todo',
        'createdAt':True,
        'updatedAt':False
    }
    all_task[task_id] = new_task

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
    list_task()

if __name__ == '__main__':
    main()