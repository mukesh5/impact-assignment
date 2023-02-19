### Impact Assignment
Assignment round for Impact Analytics


### Assignment Question
In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

### Setup


#### 1. Clone the Repo 

``git clone https://github.com/mukesh5/impact-assignment.git``

#### 2. Start the application

``python main.py {total_no_of_classes_in_int}``


### Approach

The problem can be divided into a recurrence relation based on whether the student attends the class or doesn't attend the class.
So there are two possibilities attend or miss and based on which we can come up with a below recurrence relation


```no of **valid** ways to attend classes = f(total_classes-1, 0) + f(total_classes-1, missed + 1)```

Here missed is keeping track of the missed classes till now.
The base case here is if we have reached maximum_misses then this combination becomes invalid and we return 0
and if we haven't and we have completed all classes then it is a valid way and we return 1

**Time Complexity** O(2^N) without caching; O(N*M) with caching