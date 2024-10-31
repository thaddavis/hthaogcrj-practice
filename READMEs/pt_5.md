# PART 5 - Adding CrewAI Agents

Now we’re going to add in some AI…

- Let’s update the requirements.txt file to contain the following 3rd-party packages
    - And make sure to specify these exact versions
    - I’ve tested a few different versions of CrewAI but this one seems to work most reliably to me and just so we are on the same page let’s use the same exact versions for all these packages
    - pip install -r requirements.txt
- Next let’s update the `main.py` file to include a some CrewAI-related code (we’ll take a close look at it shortly)
    - And you can see we’re importing a helper function and a pydantic type as well…
    - So let’s add the files for supporting these imports…
        - touch helpers/replace_yaml_variables.py
        - mkdir application_schema
        - touch application_schema/news_results.py
        - mkdir config
        - touch config/tasks.yaml
        - touch config/agents.yaml

- If you look closely at this config, you can see we’re creating a group of agents specialized in reporting news about Haiti
- You can easily tweak this config to report information about whatever niche matters to you btw
- For example, at the end of this walkthrough we’ll adjust these prompts to focus on reporting the latest news in the world of Insurance Technology
- Anyways!
- Let’s now try running this script and see what happens - `python main.py`
- We can see an ERROR has been thrown due to a missing OPENAI_API_KEY
    - CrewAI, aka the Multi-Agent framework we’re using, supports a number of LLMs but by default CrewAI is set up to use OpenAI
    - If your new to all this Agent stuff, here’s a quick little diagram that sheds some light on what I just said…
        - An Agent, in the context of this video, is like a virtual person and an LLM acts as this virtual person’s brain
    - You can get an OPENAI_API_KEY by coming over to https://platform.openai.com/ and signing up…
    - And after you’re signed up, make sure to add some credits to your balance. OpenAI’s API is pay-per-use, just like a gas station, so you will need some credits.
    - I recommend adding whatever the minimum allowed amount is as the cost of what we’ll be doing will only be in the pennies
    - After you have credits added come over to the Dashboard > API keys section and create an API key
        - And let’s copy this API key’s value into our project by adding a new line in the .env file that reads, in all caps, OPENAI_API_KEY=<API_KEY_HERE>
    - Then we’ll add these lines to the top of our `main.py` file to make the entries in the .env file available to our code
    - And when that’s all set up let’s run our script again and see what happens
    - `python main.py`
    - This is great! Things look like they’re working…
    - If we take a close look at this CrewAI code we just added, we can see we’re creating 2 Agents (A Manager Agent and a Researcher Agent) and 1 Task (performing research across a list of web pages)
    - This configuration gets tied together with the Crew object provided by CrewAI on line blah
        - As of the time of recording CrewAI let’s you run your Agents in 2 modes: Sequential Mode and Hierarchical Mode
        - Sequential Mode means the Agents will perform the tasks outlined in the tasks.yaml file sequentially one-by-one
            - In Sequential Mode, you must manually map each task to one of the agents in your project 
    - Hierarchical Mode, which is what we’re using, means we delegate one of the Agents in our Crew as the “Manager” of the other Agents and then assign tasks to the Manager Agent. The Manager Agent will break these task into sub-tasks as needed and automatically assign each sub-task to one or more Agents in the Crew.
    - Depending on the LLM and other implementation details, the reliability of Hierarchical Mode can be either impressive or atrocious BUT for the job of synthesizing information across a number of web pages in a particular niche, I found it to be a worthy match

    - Let’s run our Crew a few times to get feel for what it’s doing…
    - Each time we run our Crew we’ll add another website to this list of web pages and review the output

- We don’t need to save the report.md file as it will be generated on the fly so let’s add it to the .gitignore

- And yea things generally look like they’re working so let’s move on to part 6 where we’ll send this A.I.-generated report via email to a list of “subscribers”