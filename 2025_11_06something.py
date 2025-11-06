is_program_work = True       
temperature_celsius = 20
error = ''
while is_program_work:
    print("[ПУЛЬТ ТЕМПЕРАТУРЫ]")
    print('')
    print("Текущая температура: %i" % temperature_celsius)
    print('')
    print('1 - +1 градус')
    print('2 - -1 градус')
    print('0 - выход')
    print(error)
    print(">>> ", end='')
    
    user_choice = input().strip()
    
    error = ''
    
    if user_choice == "0":
        is_program_work = False 
    
    elif user_choice == "1":
        temperature_celsius += 1 
    
    elif user_choice == "2":
        temperature_celsius -= 1     
    
    else:
        error = 'ОШИБКА:уаказаны не верные данные'
        
    
    
    if temperature_celsius > 25:
        error = 'Ошибка температура слишком высокая'
        temperature_celsius -= 1
    
    elif temperature_celsius < 16:
        error = 'Ошибка температура слишком низкая'  
        temperature_celsius += 1
        
        


           
