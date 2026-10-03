#This check for duplicate numbers 
#Returns true if the number appears twice and false fr once


# Solution 0(n) complexity

# Declare a new hash set or hashMap
# Loop over your array and then before you add to your hashset, 
# Check if the item already exist in the hashset
# If it does return True, else add and continue

nums = [ 1,2,3,4,5,6,5]
hash_set = set() ## This can be a list or python set, is just used for a check


def check_duplicate():
    for n in nums:
        if n in hash_set:
            print("Found duplicate", n, )
            return True
        print(hash_set)
        hash_set.add(n)
    return False

        



check_duplicate()
