while True:
    n = int(input())
    
    if n == -1:
        break
    
    matrix = []
    
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    failed = set()
    for start in range(n):
        options1 = set()
        found = False
        
        for first in range(n):
            if matrix[start][first]:
                options1.add(first)
        
        options2 = set()
        for first in options1:
            for second in range(n):
                if matrix[first][second]:
                    options2.add(second)
        
        for second in options2:
            if matrix[second][start]:
                found = True
                break
        
        if not found:
            failed.add(start)
    
    for f in sorted(list(failed)):
        print(f, end=" ")
    print()