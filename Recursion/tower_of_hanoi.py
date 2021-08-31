def tower_of_hanoi(n, source, aux, dest):
    if n ==  1:
        print("move 1 from ",source," to ",dest)
        return
    tower_of_hanoi(n-1, source, dest, aux)
    print("move", n,"from ", source, " to ", dest)
    tower_of_hanoi(n-1, aux, source, dest)
    return pow(2,n)-1


print(tower_of_hanoi(2,1,2,3))