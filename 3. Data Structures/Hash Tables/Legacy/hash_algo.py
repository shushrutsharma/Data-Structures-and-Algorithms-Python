class AlgoHashTable:

    def __init__ (self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


    
    def set_val(self, key, value):

        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]

        found_key = False

        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, value)
        
        else: 
            bucket.append((key, value))

    def get_val(self, key):
        
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_value
        
        else: 
            return f"{key} not found"




hash_table = AlgoHashTable(200)

file = open("data.txt")

lines = file.readline().strip().split(':')

for line in file:
    key, value = line.split(":")
    hash_table.set_val(key, value)


print(hash_table)

print("-"*100)

print(hash_table.get_val("ahlrdmukjn@yaexample.com"))



