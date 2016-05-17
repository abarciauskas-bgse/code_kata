## Pseudo Code for 2.1

**Write code to remove duplicates from an unsorted linked list**
**How would you solve this problem if a temporary buffer is not allowed?**

`remove_duplicates` pseudo code:

1. Sort the list (say use quicksort), initiate i = 1
2. While i < length(sorted_list)
   - if sorted_list[i-1] == sorted_list[i]
       - sorted_list = sorted_list[0:(i-1)] + sorted_list[(i+1):-1]
       - # an item is removed, don't increment i
   - else
       - i += 1

Tests:

remove_duplicates("aabb") == "ab"
remove_duplicates("abb") == "ab"
remove_duplicates("ab") == "ab"
remove_duplicates("") == ""
remove_duplicates("aabbbcccc") == "abc"
