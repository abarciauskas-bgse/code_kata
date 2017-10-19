# System Design

## Resources

* [Le Cloud Blog: Scalability for Dummies / Posts tagged "scalability" (4-part series)](http://www.lecloud.net/tagged/scalability)
* [Hired in Tech: System Design](http://www.hiredintech.com/system-design/)

## System Design Process

1. Constraints and use cases
2. Abstract design
3. Understanding bottlenecks
4. Scaling the abstract design


## Golden Rules for Scalability

1. Servers should not contain user information such a sessions or images (load balanced), but should contain the exact same application code.
2. Database scaling can be obtained via master-replica of MySQL (master required RAM, RAM and more RAM)
3. Use an in-memory cache to store fully constructed objects (as opposed to caching db queries), this speeds up processing time and constructing objects can be done asynchronously.
4. Asynchronism.
    * Pattern 1: (pre-computation) pages are pre-rendered and stored as static content; pattern 2
    * Pattern 2: post-computation, response is given immediately but work is enqueued

### Notes on scalability

* sharding is a type of horiziontal partitioning that divides data tables into smaller tables using a shard key, duplicating the schema across these smaller databases.
* vertical partitioning divides up the schema.

