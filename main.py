# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    for i in range(m):
        start, index = heapq.heappop(threads)
        end = start + data[i]
        output.append((index, start))
        heapq.heappush(threads, (end, index))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for index, start in result:
        print(index, start)



if __name__ == "__main__":
    main()
