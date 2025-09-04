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

def add_task():
    pass

def update_task(id):
    pass

def delete_task(id):
    pass

def mark_task(arg, id):
    pass

def list_task(arg):
    pass

def main():
    print(get_id(all_task))

if __name__ == '__main__':
    main()