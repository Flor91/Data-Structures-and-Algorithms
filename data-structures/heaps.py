import heapq

H = [21,1,45,78,3,5]

# Use heapify to convert list to heap
heapq.heapify(H)

print(H) #[1, 3, 5, 78, 21, 45]

# Add element, gets added at the end
# To reorder we need to call heappify again
heapq.heappush(H,8)
print(H)

# Remove first element from the heap
heapq.heappop(H)
print(H)

# Replace smaller element
heapq.heapreplace(H,6)
print(H)
