# playback.py

def process_input(input_str):
    if input_str[1:-1] == ' ':
        dblspace = input_str[1:-1]
        print(dblspace)
        return dblspace.replace(" ", "...")
    unspace = input_str.strip()
   
    return unspace.replace(" ", "...") 
    
 

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    output = process_input(user_input)
    print(output)




