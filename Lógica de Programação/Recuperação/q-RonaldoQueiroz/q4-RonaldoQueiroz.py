def calculate_average_height():
    sum_of_heights = 0
    count = 0
    while True:
        input_data = input()
        age, height = map(float, input_data.split())
        
        if age == 0 and height == 0:
            break

        if age > 50:
            sum_of_heights += height
            count += 1
    
    if count > 0:
        average_height = sum_of_heights / count
        print(f"{average_height:.2f}")
    else:
        print()

calculate_average_height()
