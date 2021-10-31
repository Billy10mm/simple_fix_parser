from fix_parser import FIXParser

def data_processor(data):
    if data[35] == "8":
        if data[150] == "1" or data[150] == "2":
            print(data[55] + "," + data[54] + "," + data[32] + "," + data[31] + "," + data[17] + "," + data[49] + "," + data[56])

print("Symbol,Side,Quantity,Price,ExecID,SenderCompID,TargetCompID")
FIXParser("fix.log", data_processor)

