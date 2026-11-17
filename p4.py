import time

"""
  Project#4

  Add the name of groupmates and their tasks: ----

  You are free to create as many classes within the p4.py file or across 
  multiple files as you need. However, ensure that the hw5.py file is the 
  only one that contains a __main__ method. This specific setup is crucial 
  because your instructor will run the p4.py file to execute and evaluate 
  your work.

"""
"""
1- => Lambda was used in line/s: LatLonGen(), line 3
2- => Filter or map was used in line/s: ...........
3- => yield was used in line/s: .........
"""

# Andrew Albert
# Function to generate the LatLon.txt file
def latLonGen():
  # Helper set to check if we have already seen a value in zipcodes.txt
  # if so we want to skip it so that we take the first value
  seen = set()
  # Helper lambda to check if a value is in the seen set and if not add
  # it to the seen set
  isFirst = lambda k: not seen.add(k) if k not in seen else False

  # Open zipcodes.txt
  with open("zipcodes.txt", "r") as file:
    # Dictionary Comprehension to add each Zipcode as a key with a Tuple of
    # Lat and Lon as its value. This comprehension uses the lambda made prior
    # to verify that each result is the first we have seen
    zipLatLon = {line[1]: (line[6], line[7])
                  for line in [line.strip().split("\t") for line in file if line.strip()]
                  if isFirst(line[1]) and
                  line[1] != "Zipcode"}

  # Write the dictionary to the LatLon.txt file with the correct styling
  with open("LatLon.txt", "w") as file:
    file.write("\n".join(f"{z} {la} {lo}" for z, (la, lo) in zipLatLon.items()))


if __name__ == "__main__": 
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inisde the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''

    
    # WRITE YOUR CODE HERE

    latLonGen()

    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  
    

