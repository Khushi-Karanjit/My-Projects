from datetime import datetime

def print_invoice(lands, customer_name, transaction_date, duration_months, total_amount, transaction_type, fine=0):
    """
    Prints an invoice for the transaction to the shell and writes it to a file.
    """
    invoice_content = []
    invoice_content.append("--- Invoice ---")
    invoice_content.append("Transaction Type: " + transaction_type)
    invoice_content.append("Customer Name: " + customer_name)
    invoice_content.append("Date of Transaction: " + transaction_date)
    invoice_content.append("Duration (months): " + str(duration_months))
    
    if transaction_type == 'Rent':
        invoice_content.append("Rented Lands:")
    elif transaction_type == 'Return':
        invoice_content.append("Returned Lands:")
    
    for land in lands:
        invoice_content.append("Kitta Number: " + land['kitta_number'])
        invoice_content.append("City: " + land['city'])
        invoice_content.append("Direction: " + land['direction'])
        invoice_content.append("Area: " + str(land['area']) + " anna")
        invoice_content.append("Price per Month: " + str(land['price']) + " NPR")
        invoice_content.append("")
    
    if fine > 0:
        invoice_content.append("Fine: " + str(fine) + " NPR")
        invoice_content.append("Total Amount after Fine: " + str(total_amount) + " NPR")
    else:
        invoice_content.append("Total Amount: " + str(total_amount) + " NPR")
    invoice_content.append("----------------")
    
    # Print to the shell
    for line in invoice_content:
        print(line)
    
    # Write to a file
    invoice_filename = customer_name + transaction_type.lower() + "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    try:
        with open(invoice_filename, 'w') as file:
            file.write("\n")
            file.write("\t \t \t \t \t Technorental_services\n")
            file.write("\n") 
            file.write("\t \t \t \tAddress: Kamalpokhari Kathmandu Metropolitan\n")
            file.write("\n") 
            file.write("\t\t\tContact: 923342223 || Email: propertyLandNepal@gmail.com" )
            file.write("\n") 
            for line in invoice_content:
                file.write(line + "\n")
        print("\nInvoice written to " + invoice_filename)
    except IOError:
        print("Error writing the invoice to file.")
