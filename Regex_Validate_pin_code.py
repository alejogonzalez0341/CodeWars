def validate_pin(pin):
    numbers_validate= "0123456789"
    list_pin= list(pin)
    if len(list_pin) != 4 and len(list_pin) != 6:
        return False
    else:
        for i in list_pin:
            if  i not in numbers_validate:
                return False
            
    return True

            



print(validate_pin("12345"))