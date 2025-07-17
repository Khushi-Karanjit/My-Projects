from datetime import datetime, timedelta
from read import read_lands, write_lands
from write import print_invoice

FINE_RATE = 0.10  # 10% fine on the monthly rent

def get_valid_input(prompt, input_type):
    """
    Prompts the user for input and validates it.
    """
    while True:
        try:
            value = input_type(input(prompt))
            if input_type is str and not value.strip():
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a valid ",input_type.__name__)

def get_valid_name(prompt):
    """
    Prompts the user for a name and ensures it contains only alphabets.
    """
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        else:
            print("Invalid input. Please enter a valid name with alphabets only.")

def rent_land(file_path, kitta_numbers, customer_name, duration_months):
    """
    Rents one or more lands and generates an invoice.
    """
    lands = read_lands(file_path)
    rented_lands = []
    total_amount = 0
    
    for kitta_number in kitta_numbers:
        for land in lands:
            if land['kitta_number'] == kitta_number and land['status'].lower() == 'available':
                land['status'] = 'Not Available'
                rented_lands.append(land)
                total_amount += land['price'] * duration_months
    
    if rented_lands:
        start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print_invoice(rented_lands, customer_name, start_date, duration_months, total_amount, 'Rent')
        write_lands(file_path, lands)
        return "Lands " + ', '.join(kitta_numbers) + " rented by " + customer_name + " for " + str(duration_months) + " months."
    else:
        return "One or more lands are not available for rent."

def return_land(file_path, kitta_numbers, customer_name, rented_months):
    """
    Returns one or more lands, calculates fines if applicable, and generates an invoice.
    """
    lands = read_lands(file_path)
    returned_lands = []
    total_amount = 0
    total_fine = 0
    while True:
        try:
            initial_months = get_valid_input("Enter initial rented months: ", int)
            if initial_months <= 0:
                print("The number of months must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number of months.")

            

    late_months = rented_months - initial_months
    
    for kitta_number in kitta_numbers:
        for land in lands:
            if land['kitta_number'] == kitta_number and land['status'].lower() == 'not available':
                land['status'] = 'Available'
                returned_lands.append(land)
                end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                if rented_months>initial_months:    
                    fine = late_months * land['price'] * FINE_RATE
                    total_fine += fine
                    total_amount += (land['price'] * rented_months) + fine
                else:
                    total_amount += land['price'] * rented_months
    
    if returned_lands:
        print_invoice(returned_lands, customer_name, end_date, rented_months, total_amount, 'Return', total_fine)
        write_lands(file_path, lands)
        return "Lands " + ', '.join(kitta_numbers) + " returned by " + customer_name + "."
    else:
        return "No lands were rented under these kitta numbers."
