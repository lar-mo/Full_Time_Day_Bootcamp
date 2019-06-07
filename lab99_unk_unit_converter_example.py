# unit_convert_example.py

meter_dict = {'ft': 3.28, 'in': 39.37}

def to_meter(in_num, in_unit):
    # takes in a number and unit, converts to meters
    meters = in_num / meter_dict[in_unit]
    return meters

def from_meter(meter_num, out_unit):
    # takes in a number of meters and unit, converts to unit
    out_num = meter_num * meter_dict[out_unit]
    return out_num

# getting inputs
input_amount = float(input("How many: "))
input_unit = input("From what: ")
output_unit = input("To what: ")

meters = to_meter(input_amount, input_unit) # converting to meters
print(meters)

output_amount = from_meter(meters, output_unit) # converting from meters
print(output_amount)
