# Input: { apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]
# Output: [{ dm: { apple: 5 }}, { owd: { apple: 5 } }]

from collections import defaultdict, OrderedDict


class inventoryAllocator:
    def __init__(self):
        self.orders = defaultdict(int) 
        self.consolidatedInv = defaultdict(int)    #Consolidated Inventory
        self.finalOrder = []                       #Final Order
    
    # Helper Method to merge Two Dictionaries
    def Merge(self, dict1, dict2): 
        res = {**dict1, **dict2} 
        return res 

    # Main Method to find order fulfillment 
    def fulfillOrder(self, orders, inventory):
        self.orders = orders
        for items in inventory:
            for item in items['inventory']:
                self.consolidatedInv[item] += items['inventory'][item]

        # Check if order can be fulfilled, if not return [], else go ahead    
        for fruit in self.orders:
            if self.orders[fruit] > self.consolidatedInv[fruit]:
                return []
                
        #Prepare Final Order
        while not all(value == 0 for value in self.orders.values()):
            for warehouse in inventory:
                entry = dict()
                for item in self.orders:
                    if item in warehouse['inventory']:
                        if self.orders[item] > 0:
                            if any(warehouse['name'] in d for d in self.finalOrder):
                                for i in self.finalOrder:
                                    if warehouse['name'] in i:
                                        oldict = i[warehouse['name']]
                                        newdict = { item : warehouse['inventory'][item]}
                                        entry[warehouse['name']] = self.Merge(oldict, newdict)
                            else:     
                                entry[warehouse['name']] = { item : warehouse['inventory'][item]}

                            self.orders[item] -= warehouse['inventory'][item]
                            if self.orders[item] < 0:
                                self.orders[item] = 0    
     
                    if entry is not None:
                        self.finalOrder.append(entry)                    
                

        if len(self.finalOrder) > 0:
            # print(self.finalOrder)
            print([i for n, i in enumerate(self.finalOrder) if i not in self.finalOrder[n + 1:]])
        else:
            print([])
