s1 = {2,3,1}

s2 = {"b","c","a"}
result = list(zip(s1,s2))
print(result)

list1 = [10,20,30,40]
list2 = [100,200,300,400]

for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks = ["infosys","reliance","jk tryes"]
prices = [2175,3000,2582]

new = list(zip(stocks,prices))
print(new)

new_dict = {stocks:prices for stocks,prices in zip(stocks,prices)}
print(new_dict)