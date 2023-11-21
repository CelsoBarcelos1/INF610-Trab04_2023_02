import numpy as np

class BinPackingSolver:
    def __init__(self):
        self.cont = 0  # Counter for the basic operation

    def quicksort(self, array):
        if len(array) <= 1:
            return array

        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        self.cont += len(left) + len(right)

        return self.quicksort(left) + middle + self.quicksort(right)

    def validation(self, solution):
        count = 0
        if len(solution) == 2:
            count += 1
            print('\nThe Set Partition Problem is Polynomially Reducible to the Bin-Packing Problem.')
            print('Basic Operation (VALIDATION): The Basic Operation was executed %d times.' % count)
            return True
        else:
            count += 1
            print('\nThe Set Partition Problem is NOT Polynomially Reducible to the Bin-Packing Problem since exactly 2 bins were NOT found.')
            print('Basic Operation (VALIDATION): The Basic Operation was executed %d times.' % count)
            return False

    def bin_packing(self, items, bin_capacity):
        bins = [[]]  
        count = 0
        items = self.quicksort(items)  # Sort the list in ascending order

        for item in items:
            # Check if the item fits in the last bin
            if sum(bins[-1]) + item <= bin_capacity:
                bins[-1].append(item)
            else:                
                bins.append([item]) # Create a new bin and add the item to it
            count += 1
        print('\nTo find the number of bins => the Basic Operation was executed %d times!' % count)
        return bins

def main():
    solver = BinPackingSolver()

    # Example 1 => Set with Bin-Packing != 2
    # -------> Step 1) Translation f1(Pi) -> Qi

    # ----- Inputs:
    # S = [1, 3, 2, 5, 1]
    S = [1, 3, 5, 4, 1, 4]
    bin_capacity = 1

    print('========================================')
    print('Step 1) Translation f1(Pi) -> Qi')
    print('The provided set S is: S = ', S)
    print('Whose bin capacity is set to C =', bin_capacity)

    Sum = 0
    count1 = 0
    for i in S:  # Calculate the sum of S
        Sum = Sum + i
        count1 += 1  # Count how many times the Basic Operation was executed
    print('Sum of S = sum(S) = ', Sum, end='')
    print('. The Basic Operation (SUM) was executed %d times!' % count1)

    S1 = [] # S'
    count2 = 0
    for i in range(0, len(S)):  # Calculate S'
        S1.append(round(2 * (S[i] / Sum), 2))
        count2 += 1  # Count how many times the Basic Operation was executed
    print('New set S\' = 2*S/sum(S)) = ', S1)
    print('The Basic Operation (CALCULATE S\') was executed %d times!' % count2)

    # -------> Step 2) Solution A(Qi) -> Qo
    print('\n========================================')
    print('Step 2) Solution A(Qi) -> Qo | Bin-Packing Calculation!')
    solution = solver.bin_packing(S1, bin_capacity)

    print('Given the provided set, there are %d bins with C = %d.' % (len(solution), bin_capacity))
    print('\nThe bins found in the provided list are:')
    for i in solution:
        print(i)

    # -------> Step 3) Translation f2(Qo) -> Po
    print('\n========================================')
    print('Step 3) Translation f2(Qo) -> Po')

    A = [round(i) for i in np.array(solution[0]) * (Sum / 2)]
    B = [round(i) for i in np.array(solution[1]) * (Sum / 2)]

    print('Subset A = (bin1 * Sum/2) = ', A)
    print('Subset B = (bin2 * Sum/2) =', B)

    # -------> Step 4) Verification
    print('\n========================================')
    print('Step 4) Verification')
    print('Let\'s check if sum(A) == sum(B):')
    print('sum(A) =', sum(A), '   |   sum(B) =', sum(B))
    if sum(A) == sum(B):
        print('\nSince sum(A) = sum(B) => A and B ARE solutions to the Set Partition Problem!')
    else:
        print('\nSince sum(A) != sum(B) => A and B are NOT solutions to the Set Partition Problem!')

    print('\n----------------------')
    print('Validation using the found bins:')
    validation_result = solver.validation(solution)
    # print('CONCLUSION: sum(bin1) == sum(bin2) ?', validation_result)
    print('\n*CONCLUSION: Are there exactly 2 bins in the set S with capacity = 1?')
    print('In other words, len(bin) == 2 ?', validation_result)

if __name__ == "__main__":
    main()
