import random, time

class Algorithm:
    def __init__(self, name):
        self.array = random.sample(range(512), 512)
        self.name = name

    def update_display(self, swap1=None, swap2=None):
        import sorting_visualiser

        sorting_visualiser.update(self, swap1, swap2)

    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed


class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.update_display(self.array[i], self.array[min_idx])


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            self.update_display(self.array[j], self.array[j+1])


class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            cursor = self.array[i]
            idx = i
            while idx > 0 and self.array[idx-1] > cursor:
                self.array[idx] = self.array[idx-1]
                idx -= 1
            self.array[idx] = cursor
            self.update_display(self.array[idx], self.array[i])


class ShellSort(Algorithm):
    def __init__(self):
        super().__init__("ShellSort")

    def algorithm(self):
        gap = len(self.array) // 2

        while gap > 0:
            for i in range(gap,len(self.array)):
                temp = self.array[i]
                j = i
                while j >= gap and self.array[j-gap] > temp:
                    self.array[j] = self.array[j-gap]
                    j -= gap
                self.array[j] = temp
                self.update_display(self.array[j], self.array[self.array[i]])
            gap //= 2


class RadixSort(Algorithm):
    def __init__(self):
        super().__init__("RadixSort")

    def algorithm(self):

        def counting_sort(self, exp):
            output = [0] * len(self.array)
            count = [0] * (10)
            for i in range(0, len(self.array)):
                idx = (self.array[i]//exp)
                count[int((idx)%10)] += 1
            for i in range(1,10):
                count[i] += count[i-1]
            i = len(self.array)-1
            while i >= 0:
                idx = (self.array[i]/exp)
                output[count[int((idx)%10)]-1] = self.array[i]
                count[int((idx)%10)] -= 1
                i -= 1
            i = 0
            for i in range(len(self.array)):
                self.array[i] = output[i]
                self.update_display(self.array[i])

        maximum = max(self.array)
        exp = 1
        while maximum // exp > 0:
            counting_sort(self, exp)
            exp *= 10


class CocktailSort(Algorithm):
    def __init__(self):
        super().__init__("CocktailSort")

    def algorithm(self):
        swapped = True
        start = 0
        end = len(self.array) - 1
        while swapped == True:
            swapped = False
            for i in range(start, end):
                if (self.array[i] > self.array[i+1]):
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
                    swapped = True
            self.update_display(self.array[i], self.array[self.array[i+1]])
            if swapped == False:
                break
            swapped == False
            end -= 1
            for i in range(end-1, start-1, -1):
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
                    swapped = True
            self.update_display(self.array[i], self.array[self.array[i+1]])
        start += 1


class GnomeSort(Algorithm):
    def __init__(self):
        super().__init__("GnomeSort")

    def algorithm(self):
        idx = 0
        while idx < len(self.array):
            if idx == 0:
                idx += 1
            if self.array[idx] >= self.array[idx - 1]:
                idx += 1
            else:
                self.array[idx], self.array[idx-1] = self.array[idx-1], self.array[idx]
                self.update_display(self.array[idx], self.array[self.array[idx-1]])
                idx -= 1

class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, array=[]):
        if array == []:
            array = self.array
        if len(array) < 2:
            return array
        mid = len(array) // 2
        left = self.algorithm(array[:mid])
        right = self.algorithm(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            self.update_display()
        result += left[i:]
        result += right[j:]
        self.array = result
        self.update_display()
        return result

class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self, array=[], start=0, end=0):
        if array == []:
            array = self.array
            end = len(array) - 1
        if start < end:
            pivot = self.partition(array,start,end)
            self.algorithm(array,start,pivot-1)
            self.algorithm(array,pivot+1,end)

    def partition(self, array, start, end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.update_display(array[i], array[j])
        return i

class HeapSort(Algorithm):
    def __init__(self):
        super().__init__("HeapSort")

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.array[i] < self.array[left]:
            largest = left
        if right < n and self.array[largest] < self.array[right]:
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.update_display(self.array[i], self.array[largest])
            self.heapify(n, largest)

    def algorithm(self):
        n = len(self.array)
        for i in range(n,-1,-1):
            self.heapify(n, i)
        for i in range(n-1,0,-1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(i, 0)


#Note this algorithm only works on arrays with a length that is a power of 2
class BitonicSort(Algorithm):
    def __init__(self):
        super().__init__("BitonicSort")

    def compare(self, i, j, dire):
        if (dire==1 and self.array[i] > self.array[j]) or (dire==0 and self.array[i] < self.array[j]):
            self.array[i],self.array[j] = self.array[j],self.array[i]
            self.update_display(self.array[i], self.array[j])

    def bitonic_merge(self, low, cnt, dire):
        if cnt > 1:
            k  = cnt // 2
            for i in range(low, low+k):
                self.compare(i, i+k, dire)
            self.bitonic_merge(low, k, dire)
            self.bitonic_merge(low+k, k, dire)

    def bitonic_sort(self, low, cnt, dire):
        if cnt > 1:
            k = cnt // 2
            self.bitonic_sort(low, k ,1)
            self.bitonic_sort(low+k, k, 0)
            self.bitonic_merge(low, cnt, dire)

    def algorithm(self):
        self.bitonic_sort(0, len(self.array), 1)


class BucketSort(Algorithm):
    def __init__(self):
        super().__init__("BucketSort")

    def insertion_sort(self, b):
        for i in range(1, len(b)):
            up = b[i]
            j = i - 1
            while j >=0 and b[j] > up:
                b[j + 1] = b[j]
                j -= 1
            b[j + 1] = up
        return b

    def algorithm(self):
        bucket_size = 100
        min = self.array[0]
        max = self.array[0]
        for i in range(1, len(self.array)):
            if self.array[i] < min:
                min = self.array[i]
            elif self.array[i] > max:
                max = self.array[i]
        bucket_count = ((max - min) // bucket_size) + 1
        buckets = []
        for i in range(0, bucket_count):
            buckets.append([])
        for i in range(0, len(self.array)):
            buckets[(self.array[i] - min) // bucket_size].append(self.array[i])
        k = 0
        for i in range(0, len(buckets)):
            self.insertion_sort(buckets[i])
            for j in range(0, len(buckets[i])):
                self.array[k] = buckets[i][j]
                self.update_display(self.array[k])
                k += 1





import sorting_algorithms, time, os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

dimensions = (1024, 512) # The y value should be equal to the array length
algorithms = {"SelectionSort": sorting_algorithms.SelectionSort(), \
              "BubbleSort": sorting_algorithms.BubbleSort(), \
              "InsertionSort": sorting_algorithms.InsertionSort(), \
              "ShellSort": sorting_algorithms.ShellSort(), \
              "RadixSort": sorting_algorithms.RadixSort(), \
              "CocktailSort": sorting_algorithms.CocktailSort(), \
              "GnomeSort": sorting_algorithms.GnomeSort(), \
              "MergeSort": sorting_algorithms.MergeSort(), \
              "QuickSort": sorting_algorithms.QuickSort(), \
              "HeapSort": sorting_algorithms.HeapSort(), \
              "BitonicSort": sorting_algorithms.BitonicSort(), \
              "BucketSort": sorting_algorithms.BucketSort()}

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algorithms.keys(): print(key, end=" ")
        print("")
        sys.exit(0)

# Pygame Initialisation
pygame.init()
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
display.fill(pygame.Color("white"))

# Plays a sound if you are on Ubuntu/Debian
# First install sox with: sudo apt install sox
# Note: This makes the program a lot slower
def play_sound(swap):
    duration = 0.01
    freq = 20
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq+swap*10))

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

def update(algorithm, swap1=None, swap2=None, display=display):
    display.fill(pygame.Color("white"))
    pygame.display.set_caption("Sorting Visiualiser     Algorithm: {}     Time: {:.3f}      Status: Sorting".format(algorithm.name, time.time() - algorithm.start_time))
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        colour = (0,0,0)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)
        pygame.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))
    #play_sound(swap2) # - Uncomment if you want sound to play with each swap
    check_events()
    pygame.display.update()

def keep_open(algorithm, display, time):
    pygame.display.set_caption("Sorting Visiualiser     Algorithm: {}     Time: {:.3f}      Status: Done".format(algorithm.name, time))
    while True:
        check_events()
        pygame.display.update()

def main():
    if len(sys.argv) < 2:
        print("Error: Enter a sorting algorithm")
    else:
        try:
            algorithm = algorithms[sys.argv[1]]
            try:
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, display, time_elapsed)
                pass
            except:
                pass
        except:
            print("Error: {} is not a valid sorting algorithm".format(sys.argv[1]))
            print("Note: Sorting algorithms are in Camel Case")

if __name__ == "__main__":
    main()
