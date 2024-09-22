# [Example]()

#### Example 1:
```
Input: 
Output: 
Explanation:
``` 

#### Example 2:
```
Input: 
Output: 
Explanation:
``` 

#### Example 3:
```
Input: 
Output: 
Explanation:
```

#### Constraints:

-


### Solution:

- Use a fixed number of buckets (e.g. 1000)
  - for each bucket, maintain a list
- For all operations, given the key, 
  - divide the key by the number of buckets and take the remainder as the bucket index
  - search for the key in the list associated with the bucket