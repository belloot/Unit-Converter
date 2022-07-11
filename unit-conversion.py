# AMDG
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry ('285x130')
root.title('Unit Conversion')

# list of units
unitType = ["Length", "Weight", "Speed (per second)", "Speed (per hour)"]
weightUnit = ["milligram", "centigram", "gram", "kilogram", "pound"]
lengthUnit = ["inch","millimeter", "centimeter", "meter", "kilometer","foot", "yard", "mile"]
speedUnitSECOND = ["meters/s","kilometers/s","feet/s", "miles/s"]
speedUnitHOUR = ["kilometers/hr", "miles/hr"]

# WEIGHT
pound_kilogram = 0.4535924
pound_gram = 453.5924
pound_centigram = 45359.24
pound_milligram = 453592.4
kilogram_pound = 1/(0.4535924)
gram_pound = 1/(453.5924)
centigram_pound = 1/(45359.24)
milligram_pound = 1/(453592.4)

kilogram_gram = kilogram_pound * pound_gram
kilogram_centigram = kilogram_pound * pound_centigram
kilogram_milligram = kilogram_pound * pound_milligram
gram_kilogram = 1/kilogram_gram
centigram_kilogram = 1/kilogram_centigram
milligram_kilogram = 1/kilogram_milligram

gram_centigram = gram_kilogram * kilogram_centigram
gram_milligram = gram_kilogram * kilogram_milligram
centigram_gram = 1/gram_centigram
milligram_gram = 1/gram_milligram

centigram_milligram = centigram_kilogram * kilogram_milligram
milligram_centigram = 1/centigram_milligram

# LENGTH
mile_yard = 1760
mile_foot = 5280
mile_kilometer = 1.609344
mile_meter = 1609.344
mile_centimeter = 160934.4
mile_millimeter = 1609344
mile_inch = 63360
yard_mile = 1/mile_yard
foot_mile = 1/mile_foot
kilometer_mile = 1/mile_kilometer
meter_mile = 1/mile_meter
centimeter_mile = 1/mile_centimeter
millimeter_mile = 1/mile_millimeter

yard_foot = yard_mile * mile_foot
yard_kilometer = yard_mile * mile_kilometer
yard_meter = yard_mile * mile_meter
yard_centimeter = yard_mile * mile_centimeter
yard_millimeter = yard_mile * mile_millimeter
yard_inch = yard_mile * mile_inch 
foot_yard = 1/yard_foot
kilometer_yard = 1/yard_kilometer
meter_yard = 1/yard_meter
centimeter_yard = 1/yard_centimeter
millimeter_yard = 1/yard_millimeter
inch_yard = 1/yard_inch

foot_kilometer = foot_mile * mile_kilometer
foot_meter = foot_mile * mile_meter
foot_centimeter = foot_mile * mile_centimeter
foot_millimeter = foot_mile * mile_millimeter
foot_inch = foot_mile * mile_inch
kilometer_foot = 1/foot_kilometer
meter_foot = 1/foot_meter
centimeter_foot = 1/foot_centimeter
millimeter_foot = 1/foot_millimeter
inch_foot = 1/foot_inch

kilometer_meter = kilometer_mile * mile_meter
kilometer_centimeter = kilometer_mile * mile_meter
kilometer_millimeter = kilometer_mile * mile_millimeter
kilometer_inch = kilometer_mile * mile_inch
meter_kilometer = 1/kilometer_meter
centimeter_kilometer = 1/kilometer_centimeter
millimeter_kilometer = 1/kilometer_millimeter
inch_kilometer = 1/kilometer_inch

meter_centimeter = meter_mile * mile_centimeter
meter_millimeter = meter_mile * mile_millimeter
meter_inch = meter_mile * mile_inch
centimeter_meter = 1/meter_centimeter
millimeter_meter = 1/meter_millimeter
inch_meter = 1/meter_inch

centimeter_millimeter = centimeter_mile * mile_millimeter
centimeter_inch = centimeter_mile * mile_inch
millimeter_centimeter = 1/centimeter_millimeter
inch_centimeter = 1/centimeter_inch

millimeter_inch  = millimeter_mile * mile_inch
inch_millimeter = 1/millimeter_inch

# dictionary to keep length conversions
conversionsLENGTH = {
    'mile_yard' : 1760,
    'mile_foot' : 5280,
    'mile_kilometer' : 1.609344,
    'mile_meter' : 1609.344,
    'mile_centimeter' : 160934.4,
    'mile_millimeter' : 1609344,
    'mile_inch' : 63360,
    'yard_mile' : 1/mile_yard,
    'foot_mile' : 1/mile_foot,
    'kilometer_mile' : 1/mile_kilometer,
    'meter_mile' : 1/mile_meter,
    'centimeter_mile' : 1/mile_centimeter,
    'millimeter_mile' : 1/mile_millimeter,

    'yard_foot' : yard_mile * mile_foot,
    'yard_kilometer' : yard_mile * mile_kilometer,
    'yard_meter' : yard_mile * mile_meter,
    'yard_centimeter' : yard_mile * mile_centimeter,
    'yard_millimeter' : yard_mile * mile_millimeter,
    'yard_inch' : yard_mile * mile_inch ,
    'foot_yard' : 1/yard_foot,
    'kilometer_yard' : 1/yard_kilometer,
    'meter_yard' : 1/yard_meter,
    'centimeter_yard' : 1/yard_centimeter,
    'millimeter_yard' : 1/yard_millimeter,
    'inch_yard' : 1/yard_inch,

    'foot_kilometer' : foot_mile * mile_kilometer,
    'foot_meter' : foot_mile * mile_meter,
    'foot_centimeter' : foot_mile * mile_centimeter,
    'foot_millimeter' : foot_mile * mile_millimeter,
    'foot_inch' : foot_mile * mile_inch,
    'kilometer_foot' : 1/foot_kilometer,
    'meter_foot' : 1/foot_meter,
    'centimeter_foot' : 1/foot_centimeter,
    'millimeter_foot' : 1/foot_millimeter,
    'inch_foot' : 1/foot_inch,

    'kilometer_meter' : kilometer_mile * mile_meter,
    'kilometer_centimeter' : kilometer_mile * mile_meter,
    'kilometer_millimeter' : kilometer_mile * mile_millimeter,
    'kilometer_inch' : kilometer_mile * mile_inch,
    'meter_kilometer' : 1/kilometer_meter,
    'centimeter_kilometer' : 1/kilometer_centimeter,
    'millimeter_kilometer' : 1/kilometer_millimeter,
    'inch_kilometer' : 1/kilometer_inch,

    'meter_centimeter' : meter_mile * mile_centimeter,
    'meter_millimeter' : meter_mile * mile_millimeter,
    'meter_inch' : meter_mile * mile_inch,
    'centimeter_meter' : 1/meter_centimeter,
    'millimeter_meter' : 1/meter_millimeter,
    'inch_meter' : 1/meter_inch,

    'centimeter_millimeter' : centimeter_mile * mile_millimeter,
    'centimeter_inch' : centimeter_mile * mile_inch,
    'millimeter_centimeter' : 1/centimeter_millimeter,
    'inch_centimeter' : 1/centimeter_inch,

    'millimeter_inch'  : millimeter_mile * mile_inch,
    'inch_millimeter' : 1/millimeter_inch
}

# dictionary to keep speed (second) conversions
conversionsSPEEDSECOND = {
    'miles/s_feet/s' : mile_foot,
    'miles/s_kilometers/s' : mile_kilometer,
    'miles/s_meters/s' : mile_meter,
    'feet/s_miles/s' : 1/mile_foot,
    'kilometers/s_miles/s' : 1/mile_kilometer,
    'meters/s_miles/s' : 1/meter_mile,

    'feet/s_kilometers/s' : foot_kilometer,
    'feet/s_meters/s' : foot_meter,
    'kilometers/s_feet/s' : 1/foot_kilometer,
    'meters/s_feet/s' : 1/foot_meter,

    'kilometers/s_meters/s' : kilometer_meter,
    'meters/s_kilometers/s' : 1/kilometer_meter
}

# dictionary to keep speed (hour) conversions
conversionsSPEEDHOUR = {
    'miles/hr_kilometers/hr' : mile_kilometer,
    'kilometers/hr_miles/hr' : kilometer_mile,
}

# dictionary to keep weight conversions
conversionsWEIGHT = {
    'pound_kilogram' : 0.4535924,
    'pound_gram' : 453.5924,
    'pound_centigram' : 45359.24,
    'pound_milligram' : 453592.4,
    'kilogram_pound' : 1/(0.4535924),
    'gram_pound' : 1/(453.5924),
    'centigram_pound' : 1/(45359.24),
    'milligram_pound' : 1/(453592.4),

    'kilogram_gram' : kilogram_pound * pound_gram,
    'kilogram_centigram' : kilogram_pound * pound_centigram,
    'kilogram_milligram' : kilogram_pound * pound_milligram,
    'gram_kilogram' : 1/kilogram_gram,
    'centigram_kilogram' : 1/kilogram_centigram,
    'milligram_kilogram' : 1/kilogram_milligram,

    'gram_centigram' : gram_kilogram * kilogram_centigram,
    'gram_milligram' : gram_kilogram * kilogram_milligram,
    'centigram_gram' : 1/gram_centigram,
    'milligram_gram' : 1/gram_milligram,

    'centigram_milligram' : centigram_kilogram * kilogram_milligram,
    'milligram_centigram' : 1/centigram_milligram      
}

# functions
def pickUnit(event):
    unit_combo.set("Select Unit")
    convert_combo.set("Select Unit")

    if type_combo.get() == "Length":
        unit_combo.config(value = lengthUnit)
        convert_combo.config(value = lengthUnit)
        
    if type_combo.get() == "Weight":
        unit_combo.config(value = weightUnit)
        convert_combo.config(value = weightUnit)
    
    if type_combo.get() == "Speed (per second)":
        unit_combo.config(value = speedUnitSECOND)
        convert_combo.config(value = speedUnitSECOND)

    if type_combo.get() == "Speed (per hour)":
        unit_combo.config(value = speedUnitHOUR)
        convert_combo.config(value = speedUnitHOUR)
    
def calculate():
    unitType = unit_combo.get()
    unitConvert = convert_combo.get()
    unitValue = value_combo.get()

    unitConversion = unitType + "_" + unitConvert

    try:
        if type_combo.get() == "Weight" and unitConversion in conversionsWEIGHT:
            finalValue = float(unitValue) * conversionsWEIGHT[unitConversion]
            answer.config(text = str(finalValue))
        elif type_combo.get() == "Length" and unitConversion in conversionsLENGTH:
            finalValue = float(unitValue) * conversionsLENGTH[unitConversion]
            answer.config(text = str(finalValue))
        elif type_combo.get() == "Speed (per second)" and unitConversion in conversionsSPEEDSECOND:
            finalValue = float(unitValue) * conversionsSPEEDSECOND[unitConversion]
            answer.config(text = str(finalValue))
        elif type_combo.get() == "Speed (per hour)" and unitConversion in conversionsSPEEDHOUR:
            finalValue = float(unitValue) * conversionsSPEEDHOUR[unitConversion]
            answer.config(text = str(finalValue))
        elif unitType == unitConvert:
            answer.config(text = "same value")
        else: 
            answer.config(text = "Invalid")
    except ValueError:
        answer.config(value = "enter a valid number")



# drop down boxes
type_combo = ttk.Combobox(root, value = unitType)
type_combo.grid(row = 0, column = 0)
type_combo.set("Unit Type")
type_combo.bind("<<ComboboxSelected>>", pickUnit)
    

unit_combo = ttk.Combobox(root, value = [" "])
unit_combo.grid(row = 1, column = 0)
unit_combo.set("Select Unit")

sign_box = ttk.Label(root, text = "converted to")
sign_box.grid(row = 2, column = 0)

convert_combo = ttk.Combobox(root, value = [" "])
convert_combo.grid(row = 3, column = 0)
convert_combo.set("Select Unit")

value_combo = Entry(root)
value_combo.grid(row = 1, column = 1)

answer = Label(root, text = "")
answer.grid(row = 3, column = 1)
calculateButton = Button(root, text = "Calculate", command = calculate)
calculateButton.grid(row = 5, column = 0)

root.mainloop()