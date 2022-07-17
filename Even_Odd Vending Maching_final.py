#Function to know even or odd
def even_odd(num):
    if num % 2 ==0:
        print('Even');
    else:
        print('Odd')
    i = 1
    while i <= 9:
        num += 2
        print (num)
        i += 1
          

#Main Function
if __name__== '__main__':

    try:
        num = float(input('Give number: '))
        if num.is_integer():
            even_odd(int(num))
        else:
            print('Enter integer ONLY: ' )
    except ValueError:
        print('Invaid input')
        
        
