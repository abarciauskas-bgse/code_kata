# Tips

## 5 Algorithm Approaches

1. **Examplify:** Work through an example and generalize
2. **Pattern Matching:** Identify similar problems and their solutions, evaluate if any of them may be helpful.
3. **Simplify and Generalize:** Simplify a constraint of the problem, solve it and then try to generalize
4. **Base Case and Build:** Solve the problem for a base case (e.g. just one element), then 2 and on.

## Clarifying Object-Oriented Design Questions (Chapter 7)

1. What are the goals?
2. What are the restrictions?

## Recommended Approach for Recursive Solutions (Chapter 8)

1. What is the subproblem? How many will be solved in each recursion (for linked lists it will usually be one and for binary trees 2).
2. Solve for a base case f(0) (where f(n) is the subproblem for n items) and build to iteration 2
3. Understand how to solve for f(3) using f(2) (or other previous solutions)
4. Generalize for f(n)

#### Other things to watch out for:

* All recursive problems can also be solved iteratively, talk about the trade-offs
* Recursive algorithms can be space inefficient, each recursive call adds another layer to the stack (O(n) calls use O(n) memory)