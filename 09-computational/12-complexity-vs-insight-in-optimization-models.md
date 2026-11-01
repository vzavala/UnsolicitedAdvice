# Complexity vs. Insight in Optimization Models

> Posted on LinkedIn on [December 4, 2025](https://www.linkedin.com/feed/update/urn:li:activity:7402342389698527232/).

It is always tempting to build a stochastic + multi-objective + mixed-integer +  nonlinear + multi-scale optimization model. 

But, even if we could solve this model, the question is: What insight(s) will you gain from such a model?

I often feel that we push for complexity more than what we push for understanding. I am guilty as charged; earlier in my career I wanted to solve the most complex problems that I could find.  

But over time I have realized that the real value of an optimization model is ultimately the insight. This is not to say that we should not strive to solve more complex models (as those actually appear in real applications), but at some point complexity will start blurring the insight gained and will hinder explainability/interpretability.  What does this optimal solution even mean? How do I explain this to a manager/operator/taxpayer? What is the system actually doing? Then we spend as much time analyzing/explaining the solution as we spend time building the model. 

I still wonder about how to break this vicious cycle of complexity vs. interpretability. Perhaps the answer is to build a hierarchy of problems of different complexity; this can be helpful in identifying what features are truly critical and to identify a minimum working unit. But this still remains an art and requires significant expert/domain knowledge; I hope emerging tools of AI can help facilitate this.
