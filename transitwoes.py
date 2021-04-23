def function():
    total_time = 0
    line_of_input = input().split()
    start = int(line_of_input[0])
    class_starts = int(line_of_input[1])
    n_routes = int(line_of_input[2])
    new_line_of_input = input().split()
    time_to_get_to_class = int(new_line_of_input[n_routes])
    time_from_home_to_station = int(new_line_of_input[0])
    buses = input().split()
    intervals = input().split()
    total_time = time_from_home_to_station
    for i in range(n_routes): 
        if int(intervals[i]) - total_time > 0:  #we got this bus 
            total_time +=  int(intervals[i]) - total_time 
            total_time += int(buses[i])
        else:
            #we need to sit for the next bus 
            total_time += (i + 1) * int(intervals[i]) - (total_time + int(new_line_of_input[i + 1])) + int(buses[i])
    total_time += time_to_get_to_class
    return 'yes' if total_time < class_starts else 'no'
print(function())
            

