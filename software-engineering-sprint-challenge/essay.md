### Part 7 - Questions (and your Answers)

Acme Corporation isn't just a few `.py` files. If you want to grow in your
career here, you'll have to answer the following:

- What, in your opinion, is an important part of code reviews? That is, what is
  something you pay attention to when you review code, and that you appreciate
  when others do the same for your code?

**In my limited experience reviewing code, I really appreciate comments, specifically meta-comments describing the intent of a method. 'Self documentation' in the sense of variable names that are conceptually related to what the operation is performing is also very helpful.

As I am a new programmer, my approach is usually quite direct and doesn't necessarily take advantage of all of the python built in methods so when I do attempt something 'pythonically' I will leave a comment describing my intention, that may be overkill but I would rather overcommunicate with my future self then relearn each program I've written.**

- We have an awful lot of computers here, and it gets pretty confusing with
  slightly different things running on all of them. How could containers help us
  improve this situation?

**Well, I actually just spent yesterday at a Devcon-Cloud Edition in Seattle and this question was the underlying theme of that conference. My understanding is that containerization of code/programs/modules simplifies deployment because the machine you are deploying to only needs to be configured to run various types of containers (docker for example). 

Inside the container, we've already fully configured the environment that our code needs in order to run bug free. By having standardized containers, we can deploy code without complex environmnet troublshooting because the container system is very standardized with how it interacts accross operating systems.**