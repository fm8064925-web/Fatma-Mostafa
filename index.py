def remove_from_list():
    
    my_list = ['Apple', 'Banana', 'Cherry', 'Data']
    
    
    item_to_remove = input("Enter the item you want to remove: ")
    
    
    if item_to_remove in my_list:
        
        my_list.remove(item_to_remove)
        print(f"{item_to_remove} has been removed successfully.")
    else:
        
        print(f"{item_to_remove} was not found in the list.")
    

    print("Updated list:", my_list)
remove_from_list()