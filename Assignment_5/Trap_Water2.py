def trap_water(heights):
    
    size=len(heights)
   

    left =size*[0]
    right = size*[0]
    
    
    max_so_far_left=heights[0]
    for index in range(0, size):
        if(max_so_far_left < heights[index]):
            max_so_far_left=heights[index]
            left[index]=max_so_far_left
        else:
            left[index] = max_so_far_left

    max_so_far_right = heights[-1]
    for index in range(size-1, -1, -1):
        if(max_so_far_right < heights[index]):
            max_so_far_right = heights[index]
            right[index]=max_so_far_right
        else:
            right[index] = max_so_far_right

    unit_water = 0
    for index in range(0,size):
        unit_water = unit_water + min(left[index],right[index])-heights[index]
    return unit_water


def main():
    # Open the input and output files.
    input_file = open("map.txt")
    output_file = open("result.txt", 'w')
    
    # Read the line or list from the input file.
    heights = input_file.readlines()
    print(heights)
    heights = heights[0].split()
    heights = [int(i) for i in heights]
    ''' for i in range(0, len(heights)):
        heights[i] = int(heights[i])'''
    
    units_water_calc = trap_water(heights)
    output_file.write("%d\n" % units_water_calc)
    
    # Close the files.
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()