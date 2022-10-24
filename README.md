# Write a story plot with LLMs

The goal of this script is to write a plot story using an initial idea given by the user.
In the example we include in the repo, under ```first_synopsis.txt```, we provide a short idea about 
a character that is cryopreserved and wakes up in the future.  The program takes it from there.


## Method
In order to understand why the plot is the way it is, and what was the reasoning and ideas 
behind it, we simulate a brainstorming between two literary authors (in the example case we
chose Umberto Eco and Ray Bradbury).

The way we do this is with two different prompts, chained, essentially feeding each other the
outputs of the conversation so far and updating the synopsis of the story.

As you may see in the ```agent.txt``` file, I hardcoded it to not do time travel to go back to the past.
You may need to do some of this to avoid bad ideas that often come up.

### Prompts

The templates are in the ```prompt.txt```, ```prompt_summary.txt``` and ```agent.txt``` files.

## Conclusion

In my tests it takes a few tries to get a decent plot idea, and it's fun to watch the simulated 
discussions.  An example plot result:

``
Our protagonist wakes up from his cryogenic sleep to find himself on a strange new world. He is disoriented and confused, struggling to make sense of his surroundings. Everything has changed since he was frozen - humans have colonized Mars and established contact with intelligent alien life forms who are broker than us but more technologically advanced . Our protagonist is an alien who has crash-landed on Mars , and he sets out explore the planet in hopes of finding a way back home . He quickly discovers that Martian society is very different from anything he's ever known it's cold, harsh, and unforgiving . The Martians are also quite xenophobic , viewing our protagonist as nothing more than a curiosity at best and a threat at worst . Things become even more complicated when our hero meets an underground resistance movement fighting against Martian oppression . At first our hero doesn't know how to react or what side he should take but eventually comes realize that although the Martians may be more advanced than us, they're not necessarily better . He joins forces with the resistance fighters in order help free Earth from Martian rule once and for all.
``



### Mention

I took the initial structure and some code/functions from a repo of David Shapiro, who is doing an amazing 
job investigating and educating on language and cognition.  His github is 
https://github.com/daveshap and has a great youtube channel which I recommend. Thanks for all your work and open sourcing to the community :)

 