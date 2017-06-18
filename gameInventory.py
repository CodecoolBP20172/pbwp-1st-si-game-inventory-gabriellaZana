import csv
from operator import itemgetter

def display_inventory(inventory):
    print("Inventory:\n")
    v = 0
    for key,value in inventory.items():
        print (value,key)
        v += value
    print("\nTotal number of items: %g\n" % v)

def add_to_inventory(inventory, added_items):
        y = dict((x,added_items.count(x)) for x in added_items)
        for v,k in y.items():
            if v in inventory:
                inventory[v] += k
        return inventory

def print_table(inventory, order=None):
    def print_table_2(inventory,order):
        if order is None:
            for key,value in inventory.items():
                print(str(value).rjust(len(" count")," ")," ",key.rjust(max(len(key) for key in inventory)," "))
        if order == "count,asc":
            for key,value in sorted(inventory.items(),key=itemgetter(1)):
                print(str(value).rjust(len(" count")," ")," ",key.rjust(max(len(key) for key in inventory)," "))
        if order == "count,desc":
            for key,value in sorted(inventory.items(),key=itemgetter(1), reverse=True):
                print(str(value).rjust(len(" count")," ")," ",key.rjust(max(len(key) for key in inventory)," "))

    print("Inventory:\n","count","item name".rjust(18," "))
    print("-"*25)
    print_table_2(inventory,order)
    print("-"*25)
    print("\nTotal number of items: %d\n" % sum(inventory.values()))

def import_inventory(inventory, filename="import_inventory.csv"):
    my_file = open(filename,'r')
    for line in my_file:
        if line.endswith('\n'):
            line = line[:-1]
        my_list = line.split(',')
    my_file.close()
    for x in my_list:
        if x in inventory:
            inventory[x] = inventory.get(x)+1
        else:
            inventory[x] = 1

def export_inventory(inventory, filename="export_inventory.csv"):
    export = []
    for key,value in inventory.items():
        export.extend([key]*value)
    with open(filename,'w') as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(export)
    f.close()
    
   
inv = {'magic wand':1, 'owl':2, 'galleon':30, 'broomstick':1, 'potion':8, 'book with spells':3}
dragon_loot = ['book with spells', 'potion', 'broomstick', 'potion', 'owl', 'book with spells', 'potion']
inv = add_to_inventory(inv,dragon_loot)
