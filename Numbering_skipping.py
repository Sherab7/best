for i in range(1, 10):
    if i == 7:
        print(f"Reachedd{1}, breaking outer loop")
        break
    
    elif i == 3:
        print(f"skipping {i} in the inner loop")
        continue
    print(i)
    