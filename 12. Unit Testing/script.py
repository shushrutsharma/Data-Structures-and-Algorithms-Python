
def add(num):
    try: 
        return int(num) + 5
    except ValueError as err:
        return err
