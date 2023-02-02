#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date:02/01/23
#This program is designed to use bubble sorting and insertion sorting for lists of integers, and return
#the number of comparisons and exchanges that occur during sorting as a tuple.




def bubble_count(a_list):
  """
  Sorts a_list in ascending order using bubble sorting and returns the number of comparisons
  and exchanges made as a tuple.
  """
  comparisons = 0 #setting starting value of comparisons to zero
  exchanges = 0 #setting starting value of exchanges to zero

  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      comparisons += 1 #number of compared elements in the list
      if a_list[index] > a_list[index + 1]: #comparing first two elements in the list
        temp = a_list[index]
        a_list[index] = a_list[index + 1] #passing through list again to do further exchanges if needed
        a_list[index + 1] = temp
        exchanges +=1 #number of exchanged elements in the list
  return (comparisons, exchanges) #returns tuple of comparisons and exchanges made while bubble sorting a list



def insertion_count(a_list):
  """
  Sorts a_list in ascending order, and returns the numbers of exchanges and comparisons as a tuple.
  """
  comparisons = 0 #setting starting value of comparisons to zero
  exchanges = 0 #setting starting value of comparison to zero

  for index in range(1, len(a_list)):

    value = a_list[index] #item in list at each index
    pos = index - 1 #comparing value to each item to the left in the list
    while pos >= 0: #separated from "if a_list[pos] > value:" so comparisons aren't ran on on comparing the index to zero
      comparisons +=1 #checking for comparisons in values of the list
      if a_list[pos] > value: #compares values in the list
        exchanges += 1 #checking for exchanges in the list
        a_list[pos + 1] = a_list[pos]
        pos -= 1
      else:
        break #break loop
    a_list[pos + 1] = value
  return (comparisons, exchanges) #returns tuple of comparisons and exchanges made while insertion sorting through a list

