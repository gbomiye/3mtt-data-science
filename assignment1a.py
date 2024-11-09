a) # program to calculate basic statistics
A = int (input(“Enter 1 for arithmetic operation or 2 for basic statistics)
If A = 2,
def calculate_basic_stat(numbers):
  	  if len(numbers) == 0:
    	    return None  # Handle case of empty list
    
  	  total_sum = sum(numbers)
  	  average = total_sum / len(numbers)
   	 minimum = min(numbers)
   	 maximum = max(numbers)
    
      	  return {
        	'sum': total_sum,
     	   'average': average,
      	  'min': minimum,
      	  'max': maximum
    	}
	
# Example usage
	numbers = [10, 20, 30, 40, 50]

	statistics =  calculate_basic_stat (numbers)

	if statistics:
    print(f"Sum: {statistics['sum']}")
 	   print(f"Average: {statistics['average']}")
 	   print(f"Minimum: {statistics['min']}")
 	   print(f"Maximum: {statistics['max']}")
	Else:
    print("The list is empty.")

Else, 
number2 = Int(Input(” Enter number “))
def Arithmetica(number2):
 if len(number2) == 2: 
subtract = number2[0] - number2[1] 
Sum = number2[0] + number2[1] 
Division = number2[0] / number2[1] 
Product = number2[0] * number2[1] 
  return {
        	'sum': Sum,
     	   'subtract': subtract,
      	  'division': Division,
      	  'product’': Product
    	}
	
statistica =  Arithmetica (numbers)

if statistica:
    print(f"Sum: {Arithmetics['sum']}")
 	   print(f"subtract: {Arithmetics['subtract']}")
 	   print(f"Product: {Arithmetics['Product']}")
 	   print(f"Division: {Arithmetics['Division']}")
 else: return "Error: Please provide a list with exactly two numbers." 




