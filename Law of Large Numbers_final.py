import random

'''
Calculating the average of continuous rolls
'''

def get_trail_average(trail):
    
    roll = []

    for i in range(trail):
        
        roll.append(random.randint(1, 6))
        
    return sum(roll)/trail

if __name__ == '__main__':
    #trails = 500000


    trail_runs = [100, 1000, 10000, 100000, 500000]

    print('Expected value: 3.5')


    for trails in trail_runs:

        average = get_trail_average(trails)
        
    #print('Trials: {0} Trial average {1}'.format(trail_runs, average))

        print('Trials: {0} Trial average {1}'.format(trails, average))
