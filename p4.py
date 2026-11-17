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
# AJ Marin and Leah Johnston
# Generates a list of states from states.txt
def readStates():
   with open("states.txt", 'r') as stateFile:
      states = [state.strip() for state in stateFile if state.strip() != ""]
      return states

# Creates a generator that yields the city and state from each line of zipcodes.txt
def readZipCodes():
   with open("zipcodes.txt", 'r') as zipFile:
      for line in zipFile:
        parts = line.strip().split('\t')
        yield parts[3], parts[4]

# Inserts the common city names between the states in states.txt into common_citites.txt
def getCommonCityNames():
  stateCities = {state: set() for state in readStates()}

  for city, state in readZipCodes():
     if state in stateCities:
        stateCities[state].add(city)

  commonCities = sorted(set.intersection(*stateCities.values()))

  with open("common_cities.txt", 'w') as outFile:
      outFile.writelines(f"{city}\n" for city in commonCities)

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

# Ranold Antwi

def cityStatesGen():
  # Read the cities we need to look up. We us upper() b/c
  # zipcodes.txt stores every city name in all capital letters
  with open("cities.txt", "r") as file:
    cities = [line.strip().upper() for line in file if line.strip()]

  # each city starts with an empty set of states.
  # A set is used so each state can only be saved once per city
  cityStates = {city: set() for city in cities}

  # Go through zipcodes.txt one line at a time
  with open("zipcodes.txt", "r") as file:
    next(file)  # skip the header line
    for line in file:
      parts = line.split("\t")
      # skip blank or broken lines
      if len(parts) < 5:
        continue
      city = parts[3]   
      state = parts[4] 
      # only save the state if this is one of the cities we care about
      if city in cityStates:
        cityStates[city].add(state)

 
  # the states sorted and separated by a space
  lines = [" ".join(sorted(cityStates[city])) for city in cities]

  # Write the lines to the CityStates.txt file
  with open("CityStates.txt", "w") as file:
    file.write("\n".join(lines))



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
    

