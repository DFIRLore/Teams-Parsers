with open("logs.txt", "r") as file: 
    for line in file: 
        splits = str.split('\t')
        if 'warning' in line: 
            print(line) 
            
       


    
      
