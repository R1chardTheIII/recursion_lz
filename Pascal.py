def main():
#-----------------------------------------------------    
    def pascal(z):
        if z == 1:
            return [[1]]
        triangle = pascal(z - 1)
        last_row = triangle[-1]
        new_row = [1] + [last_row[i - 1] + last_row[i] for i in range(1, len(last_row))] + [1]
        return triangle + [new_row]
#-----------------------------------------------------    
    numb_one = int(input('Сколько строчек треугольника Паскаля вывести: '))
    triangle = pascal(numb_one)
#-----------------------------------------------------    
    for row in triangle:
        print(row)
#-----------------------------------------------------        
if __name__ == '__main__':
    main()
        