#Functions_to _add_elements_to_list
my_list = [1,2,3,'aqua',4,5]
print(my_list)
my_list.append(['arizona','ohio',53]) #append_function
print(my_list)
my_list.extend(['arizona','chicago','new york']) #extend_function
print(my_list)
my_list.insert(0,"United States") #insert_function
print(my_list)
#Functions_to _remove_elements_from_list
del my_list[4] #del_function
print(my_list)
x = my_list.pop(7) #pop_function
print('popped element = '+ x)
print(my_list)
my_list.remove(1) #remove_function
print(my_list)
#Accessing_list_elements
print(my_list) #Using_print_function_to print_all_elements_is_list
for element in my_list: #Loop_to_access_all_elements_in_list
    print(element)
print(my_list[5:8])  #Access_by_interval  
print(my_list[::-1]) #Accessing-elements_in_reverse