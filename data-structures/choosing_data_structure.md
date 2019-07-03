do you need random access?
do you perform a lot of insertions? how about deletions?
do you allow duplicates?
are you searching for elements frequently?
does your data need to be ordered?
would you need to traverse the elements?
how big is your data?

these and other questions need to be considered before choosing which data structure to use. it is a good idea to start from the simplest structure to see if it satisfies your criteria. it would be a waste of time to slave over implementing a complicated structure when an array can fulfill all your needs.

//THE PROCESS


start with arrays...
arrays are a suitable structure to use when you know the size you'll need and the number of elements is reasonably small. if fast insertion is needed and you do not need to traverse the elements in a specified order, use an unordered array. however, if you need search to be fast use binary search and an ordered array. this however, will make insertion slower, so if you need fast insertion and fast search, choose another structure. deletion is always slow in any kind of an array, so if you are doing a lot of deletions, array is probably not the best structure for you to use. additionally, if you overestimate or underestimate the size of the array, you will either have to expand the array (make a new bigger array and copy all elements from original array into the new one - costly operation), or you will have wasted memory. the biggest detriment of arrays is that size must be known beforehand, as failure to do so results in slow operations or memory waste. also, deletions are always slow, regardless of whether the array is sorded or not.

when arrays are not good enough, move on to linked lists
if you need a more flexible structure that does not require you to know the size ahead of time, a linked list is a good starting point. unordered linked lists offer constant time insertion (at the end or beginning of the list) since only references are being changed and no items need to be shifted. deletion runs in O(N) time since the element we're deleting needs to be found first. this is still faster than the array because, as with insertion, no items are shifted. searching is slow in the linked list because it can only be linear. remember that binary search is not possible to use with an ordered list since we cannot access elements from the middle of the list. also, if you need random access, use arrays or hash tables; linked lists are not the structure to use since they are built on relationships and every element can only be accessed from the first node.

linked lists still not good enough, move on to binary trees
if you have looked at arrays and linked lists and decided that they are not satisfactory, a binary search tree might be what you need. it provides fast O(logN) time for all operations: search, insertion, and deletion. you can easily find the minimum and maximum value of the data, and traversal in order is possible with the use of recursion. however, trees degrade to O(N) speed when they become unbalanced. if you are sure that data will be inserted in random order, a regular binary tree might be a sufficient solution. otherwise, a red-black tree or 2-3-4 tree that retains balance would be your best choice.

the end of the line: hash tables
as we've seen in the last post, hash tables offer close to O(1) search and insertion. deletion also runs in O(1) time assuming the deleted item is simply replaced with a special flag object that the search and insertion algorithms treat as an empty cell. hash tables are very fast if the load factor is suitable: .5 or .66 for open addressing, and around 1 for separate chaining. beware though, that any sort of traversal of the elements inside the hash table is not possible. we are only able to search, insert, and delete (in the special way described earlier). hash tables are much faster than trees, but can degrade catastrophically when the load factor gets too big. since hash tables are based on arrays, it is important to have a rough idea of how many elements you would be expecting. if you cannot accurately predict the size of your elements beforehand, using the separate chaining method would be a better choice over open addressing in implementing your hash table.

//EXTERNAL STORAGE
i mentioned external storage in the post on b-trees. recall that accessing data on in external storage is much slower than access in main memory, so to increase efficiency while working with external storage we need to minimize the number of disk accesses. this happens if we increase the number of data per node, which can be done with a multi-way tree. this way, we can read in a whole block into main memory, and work from there to search for our key (supposing we are doing insertion). if the block contains 1000 data items, by fitting all these items into a single block we have reduced the number of disk accesses from 1000 to 1. this is the direction of thinking you need to be aware of while working with external storage and deciding which data structure to use.

//ABSTRACT DATA TYPES

stack:                       O(1) insertion, O(1) deletion
queue:                     O(1) insertion, O(1) deletion
priority queue:        O(N) insertion, O(1) deletion

to review, there are three types of ADTs: the stack, the queue, and the priority queue. these are interfaces and can be implemented with either an array or linked list (in the case of a priority queue, a heap can be used). the stack is a last-in-first-out data structure, and offers constant time insertion and deletion. the queue has the same efficiency, except that it is a first-in-first-out structure. priority queue is a sorted queue by priority (from greatest to lowest key) - meaning it is sorted. insertion in a priority queue runs in O(N) time, while removal is still in constant time.

//A WORD ON SORTS

                     average               worst
bubble:         O(N^2)                same
selection:      O(N^2)                same
insertion:      O(N^2)                same
shellsort:       O(N^3/2)             same
mergesort:    O(NlogN)            same                [note: requires extra memory]
quicksort:     O(NlogN)           O(N^2) 

if you need to sort your data, first start with the simple sorts. insertion is the best of the O(N^2) sorts, so if you have a relatively small amount of data this sort will work fine for your needs, and is also easy to implement. if you have roughly 1,000-5,000 items (figures are estimated), insertion sort is probably not good enough and shellsort can be examined next. if you have a large data set, you can finally turn to the more complex sorting algorithms: mergesort and quicksort, which run in fastest O(NlogN) time. mergesort requires twice the amount of space as the original array, so if you are limited on memory this would not be the best choice. quicksort can then be used. however, beware of quicksort's catastrophic degradation to O(N^2) time if the items are not random. the table above summarizes these points.
