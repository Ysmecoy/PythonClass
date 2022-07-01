def trap_water(ele_map):
    """Calculates the units of water trapped in an elevation map.
    :param ele_map: a non-empty elevation map
    :type ele_map: List[int]
    :returns: units of water trapped in {ele_map}
    :rtype: int
    """
    result = 0
    for i in range(1, len(ele_map)-1):
        #Pick the smaller between "max on the left side" and max on the right
        smaller = min(max(ele_map[:i]), max(ele_map[i + 1:]))
        
        print('Max:', max(ele_map[i:]), max(ele_map[i+1:]))
        print('_______________________________________')
        print('smaller:', min(max(ele_map[i:]), max(ele_map[i+1:])))
        #print(smaller)
        # if the smaller is greater than the current, add their difference to the result.
        if smaller > ele_map[i]:
            result += smaller - ele_map[i]
            
            print('/////////////////////////')
            print(' item[i]:', ele_map[i])
            print('*************************')
            print('result;', result)
    return result 

ele_map =[1,0,5,3,6,2]
print(trap_water(ele_map))

def main():
    #Open the input and output files.
    input_file = open("map.txt")
    output_file = open("result.txt", "w")
    
    # Read the elevation map stored in the input file.
    ele_map = [int(val) for val in input_file.read().split()]
    
    #call the "trap_water()" function to calculate the units of water trapped.
    result = trap_water(ele_map)
    
    #Write the result to the output file
    output_file.write(str(result))
    
    #Close the files
    input_file.close()
    output_file.close()
    
    if __name__ == "__main__":
        main()
        


        