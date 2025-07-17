import csv

def read_lands(file_path):
    """
    Reads land data from a file and returns a list of land records.
    """
    lands = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 6:
                    kitta_number, city, direction, area, price, status = row
                    
                    try:
                        lands.append({
                            'kitta_number': kitta_number.strip(),
                            'city': city.strip(),
                            'direction': direction.strip(),
                            'area': int(area.strip()),
                            'price': int(price.strip()),
                            'status': status.strip()
                        })
                    except ValueError:
                        print("Skipping invalid line: ",row)
    except FileNotFoundError:
        print("File ",file_path, "not found.")
    return lands

def write_lands(file_path, lands):
    """
    Writes the updated land data back to the file.
    """
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            for land in lands:
                writer.writerow([
                    land['kitta_number'],
                    land['city'],
                    land['direction'],
                    land['area'],
                    land['price'],
                    land['status']
                ])
    except IOError:
        print("Error writing to file ",file_path)
