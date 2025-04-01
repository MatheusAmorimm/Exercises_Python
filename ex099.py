def bigger(*nums):
    print("-"*30)
    maior = 0
    counter = 0
    while counter < len(nums):
        for i in nums:
            if counter == 0:
                maior = i
            if i > maior:
                maior = i
            counter += 1
        print(f"O maior numero informado foi: {maior}")

bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger(6)
bigger(0)