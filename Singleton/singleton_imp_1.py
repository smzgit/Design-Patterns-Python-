class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            print('creating 1st instance....')
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == '__main__':
    obj1 = Singleton()
    obj1.val = 200
    print(f'obj1 val = {obj1.val}')

    obj2 = Singleton()
    print(f'obj2 val = {obj2.val}')
    print(f'obj1 is obj2 ? = {obj1 is obj2}')