#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4


    attributes = dir(hidden_4)
    for i in attributes:
        if i[:2] != "__":
            print(attributes)
