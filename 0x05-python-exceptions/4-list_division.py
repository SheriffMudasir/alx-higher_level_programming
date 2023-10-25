#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_of_divisions = []

    for i in range(list_length):
        try:
            element1 = my_list_1[i] if i < len(my_list_1) else 0
            element2 = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(element1, (int, float)) or not isinstance(element2, (int, float)):
                raise TypeError("wrong type")
            
            if element2 == 0:
                raise ZeroDivisionError("division by 0")

            division_result = element1 / element2
            list_of_divisions.append(division_result)
        
        except ZeroDivisionError:
            print("division by 0")
            list_of_divisions.append(0)
        except TypeError:
            print("wrong type")
            list_of_divisions.append(0)
        except IndexError:
            print("out of range")
            list_of_divisions.append(0)
        finally:
            pass

    return list_of_divisions
