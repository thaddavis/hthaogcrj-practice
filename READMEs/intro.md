# INTRO - How to host CrewAI Agents on Google Cloud Run

We will now take a close look at a PRODUCTION application involving the use of LLMs, AI agents, GCP, Python, and Docker.

That’s right I said PRODUCTION. This is the real deal. Wake up!

If you’re new to these technologies, I’ll do my best to make them approachable but you will need at least some familiarity with Python, Cloud Computing, and CLIs to easily follow along.

If you’re already very familiar with these technologies, I’d love your feedback on the overall design being presented…

In this video we’re going to build a team of personalized A.I. Agents who will send us daily bullet points highlighting news updates happening across multiple websites

Here’s a diagram showing what we’ll be building for clarity…

This design can be used as the foundation for many applications BUT to get your creative juices flowing, here are 2 that come to mind…

	1) a productivity hack for staying up-to-date on a niche that matters to you
	2) building your own A.I.-powered newsletter

We’ll build these A.I. news reporters using CrewAI (which is a Python-based tool for programming AI Agents) and we’ll design these A.I. Agents to run on a popular and easy-to-use hosting service called “Cloud Run Jobs” so that our Agents work for us 24/7.

🔥

HERE’S AN OVERVIEW OF THE SECTIONS THAT FOLLOW SO YOU KNOW WHAT’S COMING
 
- PART 1 - Setting up our Dev Container
- PART 2 - Deploying a simple Job to Cloud Run
- PART 3 - CICD with GitHub Actions
- PART 4 - Setting up a cron job using Cloud Scheduler
- PART 5 - Adding CrewAI Agents
- PART 6 - Adding Mailgun
- PART 7 - Deploying our application to GCP
- PART 8 - Adding AgentOps
- PART 9 - Wrapping up

And I 100% guarantee this is going to be incredible

You will still get a ton of value by simply watching BUT, IF you want to code along, here’s what you’ll need…

- A) A PC aka: a Laptop or Desktop
- B) Docker (FREE)
- C) A code editor editor — VSCode or Cursor (VSCode is FREE / Cursor has a FREE trial)
    - FYI: Cursor is an altered version of VSCode so even tho I’ll be using VSCode you should be able to follow along
- D) After VSCode or Cursor is installed add 2 “VSCode” extensions
    - the “Docker” extension (FREE)
    - the “Dev Containers” extension (FREE)
- E) a GitHub account [FREE tier works]
- F) a GCP account [practically FREE]
- G) an OpenAI account [Costs between a few pennies to a few dollars depending]
- H) an AgentOps account [FREE tier works]
- I) & optionally you’ll need a domain [Will cost a few dollars depending on your domain]

I know this sounds like a lot but it’s not that bad. Let me break it down…

In regards to Docker, the Code Editor, and the 2 Extensions, I’ll be playing a clip shortly that shows how I installed them onto my M1 Macbook Pro in under a minute and even though my machine is Mac, the broad strokes of what you’ll see in that clip will apply for Windows or Linux.

In regards to the GitHub account, you can get an account by coming over to https://github.com/ and signing up

In regards to GCP, you can get an account by coming over to https://cloud.google.com and signing up OR you can simply press the “Activation” button on the https://cloud.google.com/cloud-console page if you already have a gmail account you’d like to use

GCP usually offers free credits on signup (or activation) PLUS the cost of what we’re doing will be in the pennies. So the GCP side of things should be practically free assuming you tear down the project we create within a few days after building it. We’ll show how to tear down the GCP project at the end of this video.

SO! I know that was a mouthful but what I’m saying is… setting up a PC with Docker, a Code Editor, 2 VSCode extensions, a GitHub account, and a GCP account is enough to get started…

Later in this video, aka in PART 5, is when we’ll need the remaining items…

Those being…

- the OpenAI account
    - Why? For powering our A.I. Agents
- the Mailgun account
    - Why? For delivering our A.I.-generated emails
- the AgentOps account
    - Why? For monitoring our Agents
- (Optional) A Domain
	- If you DON’T mind the A.I.-generated emails we create being sent to SPAM (which is ok for learning purposes), DON’T worry about setting up a domain
	- BUT if you DO want the A.I.-generated emails to be delivered properly to the recipients inbox you will need some “verified” domain
	- If you do decide set up a domain, which, once again, is NOT absolutely necessary if you’re here for learning purposes, I suggest buying one from whatever Domain Registrar you’re most familiar with (for example, I’ll be using Route 53 later in part 6)

OK! Take a deep breath (PAUSE)

For the advanced viewers watching, feel free to switch out these components for whichever ones you prefer BUT, to keep things simple, this is what we’ll be using for demo purposes

If you have any setup or installation issues, leave a comment so we’re aware, and you can also enter detailed descriptions of the errors you come across into either Google or ChatGPT for further assistance.

If you’re laser focused you can complete ALL of setup requirements in under 10 minutes. But if you find doing them all at once to be overwhelming, take care of A-F and worry about the rest later

So focus and I’ll see you in part 1 when you’re ready to go : )

I’ll now play the 1-minute clip showing how I installed Docker, VSCode, & the 2 extensions so you see how easy it was for me…

[PLAY CLIP OF INSTALLING DOCKER AND VSCODE]
