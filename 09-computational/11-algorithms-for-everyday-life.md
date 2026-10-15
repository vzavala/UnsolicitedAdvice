# Algorithms for Everyday Life

> *Unsolicited advice for young scientists doing computational research.* Posted on LinkedIn on [December 22, 2023](https://www.linkedin.com/feed/update/urn:li:activity:7143972905163403264/).

Algorithms are much more than frameworks to solve mathematical problems, they are frameworks/paradigms that help you navigate and solve problems that arise in your daily life. 

I like to joke that I live my life as if it was a multi-scale, multi-objective, stochastic optimization problem :)

For instance, I like to think of writing a paper from the perspective of an algorithmic paradigm called "multi-grid", which is widely used for solving multi-scale problems. The idea is to construct a hierarchy of representations of a system, each capturing features at different scales; in the figure below you see finer at the top and coarser at the bottom, but you can also reverse the order with coarser at the top and fine at the bottom (I prefer this view). 

You can find a solution of the top level that captures the coarse features of the problem (gives you the skeleton, if you wish) and then this solution is passed to a lower level problem that aims to correct details/defects. At the lower level, you can decompose the system into subdomains and progressively refine each subdomain (by iterating over each subdomain, and you can refine it by looking at subdomains in different order). 

Writing a paper feels just like this, you can start writing a skeleton/scaffold of the full thing without capturing finer details. Once you have the skeleton, you jump into into different subdomains/sections and refine; you can iterate over the different sections in different order (e.g., beginning->end, end->beginning). The interesting observation that you learn from multi-grid is that, if you start iterating over subsections without having a skeleton, you will converge to a solution (e.g., to a coherent story), but you will converge slowly... this is why it is important to have a skeleton that captures the broad aspects of the story. You can also decide to have multiple levels of resolution, this becomes particularly important when working on large projects, such as writing a thesis or book. 

What I like about the multigrid framework is that there are many ways to design it, depending on what are your goals or problem at hand. Overall, this is just a convenient framework to decompose large projects (e.g., carpentry and construction). 

I enjoy finding real-life applications of algorithms; I few years ago I read this book ("Algorithms to Live By" of Christian and Griffiths), which I highly recommend: https://lnkd.in/gVQhQRUQ

Overall, I think that trying to find applications of the algorithms that you work on can be fun and also help you develop your abstraction skills. 

Figure credit: https://lnkd.in/gBHC5A6r

:::{note}
The original post included a multigrid diagram, which isn't reproduced here. See the LinkedIn post for the figure.
:::
