from operations import *
from read import *
from write import *

def main(): 
    """
    Main function to run the land rental system program.
    """
    #to display details about the company   
    print("\n")
    print("\t\t\t\t\t\tTechnorental_services")
    print("\n")
    print("\t\t\t\t\t       Kamal pokhari, Kathmandu  ")
    print("\n")
    print("\t\t\t\tContact: 9807655432 || Email: propertyLandNepal@gmail.com" )
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------")
    print("Available lands and its information in our company")
    print("---------------------------------------------------------------------------------------------------------------------")
    print("\n")
    


    file_path = 'lands.txt'
    
    while True:
        display_lands(file_path)
        print("Please choose the option you want to continue: ") 
        print("\n1. Rent Land")
        print("2. Return Land")
        print("3. Exit")
        choice = get_valid_input("Enter your choice: ", int)
        
        if choice == 1:
            kitta_numbers = get_valid_input("Enter kitta number you want to rent: ", str).split(',')
            kitta_numbers = [kitta.strip() for kitta in kitta_numbers]
            customer_name = get_valid_name("Enter customer name: ")
            #duration_months = get_valid_input("Enter duration in months: ", int)
            
            while True:
                try:
                    duration_months = get_valid_input("Enter duration in months: ", int)
                    if duration_months <= 0:
                        print("The number of months must be a positive integer.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number of months.")
            print(rent_land(file_path, kitta_numbers, customer_name, duration_months))
        
        elif choice == 2:
            kitta_numbers = get_valid_input("Enter kitta numbers you want to return : ", str).split(',')
            kitta_numbers = [kitta.strip() for kitta in kitta_numbers]
            customer_name = get_valid_name("Enter customer name: ")
            
            while True:
                try:
                    rented_months = get_valid_input("Enter actual rented months: ", int)
                    if rented_months <= 0:
                        print("The number of months must be a positive integer.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number of months.")
            print(return_land(file_path, kitta_numbers, customer_name, rented_months))
        
        elif choice == 3:
            print("---Thanks for using Technorental Services---")
            break
        
        else:
            print("Invalid choice. Please try again.")
def display_lands(file_path):
    """
    Displays the available lands.
    """
    with open("lands.txt",'r') as file: #read lands.txt file
        myDictionary={}
        print("\n")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("\tKitta No.  \tLocation        faced          Aana       Price          Status              ")
        print("---------------------------------------------------------------------------------------------------------------------")
        kitta=101
        for line in file:
            line=line.replace('\n','')
            myDictionary[kitta]=(line.split(','))
            kitta=kitta+1
        



    with open("lands.txt",'r') as file:
        
        for line in file:
            print("     \t ",line.replace(',','   \t '))
            
    return myDictionary
    
if __name__ == "__main__":
    main()
