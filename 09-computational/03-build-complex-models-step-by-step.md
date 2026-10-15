# Build Complex Models Step by Step

> *Unsolicited advice for young scientists doing computational modeling.* Posted on LinkedIn on [September 21, 2023](https://www.linkedin.com/feed/update/urn:li:activity:7110432672971165696/).

When implementing a highly complex model, it is important to develop a strategy to *progressively* build this up, debug it, and validate it. 

Start simple; implement a minimum model that captures some of the initial features of your problem. Make necessary assumptions (e.g., linear behavior, steady-state, ignore constraints) so that you obtain results that you expect. 

Once your initial model yields expected behavior, start to progressively implement features, and do this in a way that you can isolate effects. Try not to make abrupt jumps in model complexity (take baby steps) and try to validate behavior at every step.

Try to avoid implementing the full complex model first; this is asking for trouble. A lot of things can go (and will go) wrong when implementing and running a model, and it will be difficult to identify problems if you start with the complex model. For instance, you need to isolate issues associated with model features from numerical issues. 

Also, by building your model progressively, you will learn more about system behavior and about aspects that influence such behavior. Moreover, it is much easier to do experiments with simple models than with complex ones. 

Overall, I feel that an essential skill in dealing with complexity is to build and analyze things in a modular manner. To do this you need to identify ways to create “surrogates” of varying levels of complexity. This is a highly useful skill in model development (and science in general).
