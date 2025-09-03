all_task = {
    1: {
        'description':'Task Test 1',
        'status':'todo',
        'createdAt':True,
        'updatedAt':False
    },
    2: {
        'description':'Task Test 2',
        'status':'in-progress',
        'createdAt':True,
        'updatedAt':True
    },
}
def get_id(agenda) -> int:
    new_id = max([i for i in agenda], default=0) + 1
    return new_id

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
    print(get_id())

if __name__ == '__main__':
    main()