

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))
# ******************************
# Make your Code
# ******************************
for i in range(len(numbers)):
   if (insval > numbers[i]) and (insval < numbers[i+1]):
    numbers.insert(i+1,insval)
   if (insval > max(numbers)):
        numbers.append(insval)
   if (insval < min(numbers)):
       numbers.insert(0, insval)     
print (numbers)
