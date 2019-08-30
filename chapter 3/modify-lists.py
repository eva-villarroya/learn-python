motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

motorcycles[0] = 'ducati' 
print(motorcycles)

motorcycles.append('harley')
print(motorcycles)

motorcycles.insert(0, 'vespa')
print(motorcycles)

del motorcycles[0] 
print(motorcycles)


popped_motorcycle = motorcycles.pop(0) 
print(motorcycles)
print(popped_motorcycle)


motorcycles.remove('suzuki') 
print(motorcycles)

motorcycles.sort()
print(motorcycles)


motorcycles.sort(reverse=True)
print(motorcycles)


print(sorted(motorcycles))
print(motorcycles)

motorcycles.reverse()
print(motorcycles)

print(len(motorcycles))



