def main():
    try:
        numbers_file = open('numbers.txt', 'r')
        total = 0
        count = 0
    
        for line in numbers_file:
    
            total = total + float(line)
            count = count + 1
            print (f'I read in {count} number(s) Current number is: {float(line)} Total is: {total}')
            average = total / count
            print (f'Average:',average)
    except ValueError:
            print('Error, invalid value!!!')
    except IOError:
            print('File was not found!!!')
        
if __name__ == '__main__':
    main()
