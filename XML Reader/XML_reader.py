# This program reads data from Plant Catalog and builds parallel arrays
# for the plant items. It then displays the plant items and the total number of
# items in the catalog and the average price per item.
# Created by Frank Boxenbaum
# References: https://harpercollege.pressbooks.pub/programmingfundamentals/
# https://www.w3schools.com/python/
# https://docs.python.org/3/library/exceptions.html

def read_file_data():
    with open('plant_catalog.xml', 'r') as file_content:
        data = file_content.readlines()
        file_content.close()

    return data


def build_array(xml_tag, data):
    xml_values = []
    for line in data:
        if xml_tag in line:
            split_xml_tag = line.replace(xml_tag, "").replace("<", "")
            replace_xml = split_xml_tag.replace(">", "")
            final_xml = replace_xml.replace("/", "").strip()
            xml_values.append(final_xml)
        pass

    return xml_values


def calculate_average(price):
    try:
        price_calc = [float(item.replace("$", "")) for item in price]
        price_average = float(round(sum(price_calc) / len(price_calc), 2))

        return price_average

    except ValueError:
        print('Error: Missing or bad data')


def display_results(common, botanical, zone, light, price, price_average):
    for index in range(len(common)):
        print((common[index]) + " " + "(" + (botanical[index]) + ")" + 
              " " + "-" + " " + (zone[index]) + " " + "-" + " " + 
              (light[index]) + " " + "-" + " " + (price[index]))

        pass

    print(str(len(price)) + " " + "items" + " " + "-" + " " + 
              "$" + str(price_average) + " " + "average" + " " + "price")


def main():
    try:
        data = read_file_data()
        common = build_array("COMMON", data)
        botanical = build_array("BOTANICAL", data)
        zone = build_array("ZONE", data)
        light = build_array("LIGHT", data)
        price = build_array("PRICE", data)
        price_average = calculate_average(price)
        display_results(common, botanical, zone, light, price, price_average)
    except FileNotFoundError:
        print('File is missing.')

    except ValueError:
        print('Invalid price')

    except ZeroDivisionError:     
        print('File is empty')


main()
