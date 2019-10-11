from inventoryAlloc import inventoryAllocator
# import pdb
# pdb.set_trace()

# Test Case 1
# Expected Output : [{ 'dm': { 'apple': 5 }}, { 'owd': { 'apple': 5 } }]
order1 = inventoryAllocator()
print('test Case one output')
order1.fulfillOrder({ 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}])

# Test Case 2
# Expected Output : []
order2 = inventoryAllocator()
print('test Case two output')
order2.fulfillOrder({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 0 } }])

# Test Case 3
# Expected Output : [{ 'owd': { apple: 1 } }]
order3 = inventoryAllocator()
print('test Case three output')
order3.fulfillOrder({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }])

# Test Case 4
# Expected Output : [{ 'dm': { 'apple': 5, 'banana': 2 }}, { 'owd': { 'apple': 5 } }]
order4 = inventoryAllocator()
print('test Case four output')
order4.fulfillOrder({ 'apple': 10, 'banana' : 2 }, [{ 'name':'owd', 'inventory': { 'apple': 5, 'banana' : 2 } }, { 'name':'dm', 'inventory': { 'apple': 5 }}])

# Test Case 5
# Expected Output : [{ 'dm': { 'apple': 5 }}, { 'owd': { 'apple': 5, 'banana': 2 } }]
order5 = inventoryAllocator()
print('test Case five output')
order5.fulfillOrder({ 'apple': 10, 'banana' : 2 }, [{ 'name':'owd', 'inventory': { 'apple': 5 } }, { 'name':'dm', 'inventory': { 'apple': 5, 'banana' : 2 }}])