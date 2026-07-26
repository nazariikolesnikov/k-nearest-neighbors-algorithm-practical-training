import csv
import random


def generate_wine_data(num_rows = 178, filename = 'wine_data.csv'):
    headers = [
        '№', 'Alcohol', 'Malic and Apple Acid', 'Ash', 
        'Alcalinity of Ash', 'Magnesium', 'Total Phenols', 
        'Flavanoids', 'Nonflavanoid Phenols', 'Proanthocyanins', 
        'Color', 'Intensity', 'Hue', 'OD280_OD315_of_Deluted_Wines', 'Proline', 'Desired'
    ]
    wine_colors = ['Red', 'White', 'Rosé']

    with open(filename, mode = 'w', newline = '', encoding = 'utf-8-sig') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(headers)
        for i in range(1, num_rows + 1):
            row = [
                i,                                      # №
                round(random.uniform(13.0, 14.5), 2),   # Alcohol [13...14,5]
                round(random.uniform(1.7, 2.6), 2),     # Malic and Apple Acid [1,7...2,6]
                round(random.uniform(2.1, 2.9), 2),     # Ash [2,1...2,9]
                round(random.uniform(11.2, 21.0), 2),   # Alcalinity of Ash [11,2...21,0]
                random.randint(102, 130),               # Magnesium [102...130]
                round(random.uniform(2.6, 3.9), 2),     # Total Phenols [2,6...3,9]
                round(random.uniform(2.65, 3.5), 2),    # Flavanoids [2,65...3,5]
                round(random.uniform(0.23, 0.39), 2),   # Nonflavanoid Phenols [0,23...0,39]
                round(random.uniform(1.81, 2.82), 2),   # Proanthocyanins [1.81...2.82]
                random.choice(wine_colors),             # Color 
                round(random.uniform(4.32, 7.81), 2),   # Intensity [4.32...7.81]
                round(random.uniform(0.86, 1.05), 2),   # Hue [0.86...1.05]
                round(random.uniform(2.93, 3.92), 2),   # OD280_OD315_of_Deluted_Wines [2.93...3.92]
                random.randint(735, 1480),              # Proline [735...1480]
                random.randint(0, 1)                    # Desired [0...1]
            ]
            writer.writerow(row)
            
    print(f"Success! {num_rows} records generated.")
    print(f"The file was successfully saved with the name: {filename}")

if __name__ == '__main__':
    generate_wine_data(178)