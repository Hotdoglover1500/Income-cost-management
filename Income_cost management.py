class Measurement:

    Income = int(input("Total Income amount: "))

    n = int(input("Total cost pair: "))
    Cost_sector = {}
    for i in range(0,n,1):
        key = input("Enter the cost key: ")
        value = int(input("Enter the cost value: "))
        Cost_sector.update({key:value})

    print("My dict",Cost_sector)

    for cost_tags in Cost_sector:
        print(cost_tags,"-->",Cost_sector[cost_tags])

    Total_cost = sum(Cost_sector.values())
    print("Total cost:",Total_cost)

    if Income < Total_cost:
        print("WARNING: You have to pay the negetive amount:")
    
    def Calculate(self):
        return self.Income - self.Total_cost

M = Measurement()
calculation = M.Calculate()
print("Rest savings:")
print(calculation)
