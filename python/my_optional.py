from typing import Optional

def nice_message(name:Optional[str])->None:
    if name is None:
        print('hey random person')
    else:
        print(f'hi there,{name}!')

nice_message(None)