# INTRO - How to host CrewAI Agents on Google Cloud Run

In this video we’ll take a close look at a PRODUCTION application involving the use of LLMs, AI agents, GCP, Python, and Docker.

If you’re new to these technologies, I’ll do my best to make them approachable but you will need at least some familiarity with Python, Cloud Computing, and CLIs to easily follow along.

If you’re already very familiar with these technologies, I’d love your feedback on this application’s overall design…

What we’re going to do in this video is build up from scratch a team of customizable A.I. news reporters that will synthesize information from a configurable list of websites and report it to us on a regular basis via email. By regular basis I mean hourly or daily, or whatever interval we’d like.

Here’s an architecture diagram for clarity…

This general design can be used as the foundation for many applications but to get your creative juices flowing, I’ll give you 2 that come to mind…

	1) a productivity hack for staying up-to-date on a niche that matters to you
	2) building your own A.I.-powered newsletter

We’ll build these news reporters using CrewAI (which is a Python-based tool for programming AI Agents) and we’ll design these A.I. news reporters to run on a hosting service managed by Google called “Cloud Run Jobs”.

Running our application in the Cloud means it’ll work for us regardless of if our personal computer is turned on or off

🔥

HERE’S AN OVERVIEW OF THE SECTIONS THAT FOLLOW SO YOU KNOW WHAT’S COMING
 
- PART 1? - Setting up our Dev Container
- PART 2? - Deploy a simple Job to Google Cloud Run with CICD
- PART 3? - CICD with GitHub Actions
- PART 4? - Set up a cron job using Cloud Scheduler
- PART 5? - Add CrewAI Agents
- PART 6? - Add Mailgun
- PART 7? - Deploy the application to Google Cloud
- PART 8? - Add AgentOps

And I 100% guarantee this is going to be incredible

You can simply sit back, watch & enjoy BUT for those interested in coding along, here’s what you’ll need…

- A) A PC aka: a Laptop or Desktop
- B) This PC will need 2 applications installed onto it namely Docker and VSCode
- C) After VSCode is installed you’ll need to add 2 VSCode extensions namely the “Docker” extension and “Dev Containers” extension
- D) A GitHub account
- E) A GCP account
- F) An OpenAI account
- G) A Mailgun Account
- H) And finally you’ll need an AgentOps Account

I know this sounds like a lot but it’s not too bad. Let me break it down if you’re new to all this…

For reference, I’ll play a short clip showing how I installed Docker, VSCode, and the 2 VSCode Extensions onto my M1 Macbook Pro at the end of this intro (so you get a feel for how easy it was for me) and even though my machine is Mac-based, the broad strokes should apply if you’re machine is Windows or Linux.

You can get a GitHub account by coming over to https://github.com/ and signing up

And you can get a GCP account by coming over to https://cloud.google.com and signing up OR by simply pressing the “Activation” button on the https://cloud.google.com/cloud-console page if you already have a gmail account you’d like to use GCP with…

GCP usually offers free credits on signup or activation PLUS the cost of what we’re doing here will be in the pennies. So the GCP side of things should be practically free assuming you tear down the project we create within a few days of building it. We will show how to tear down the GCP project at the end of this video.

When we get to the 2nd half of this walkthrough (aka PART 5) we will need…

- An OpenAI account
    - For powering our LLM-based Agents
- A Mailgun account - https://try.mailgun.com/api-1
    - For delivering our A.I. generated emails
- And an AgentOps account
    - For monitoring our Agents after they’ve been deployed

The design of this application we’re building is pretty modular so you could switch out certain components for others you prefer BUT this is what we’ll be using for demonstration purposes

So once again, if you want to code along, you’ll need a computer with Docker and VSCode installed (and make sure VSCode has the `Docker` and `Dev Containers` extensions too) and you’ll also need a GitHub account & a GCP account..

The remaining prerequisites (like the OpenAI, Mailgun, & AgentOps accounts) can wait till PART 5 if you prefer…

Let me know in the comments if you have any setup or installation issues and I also recommend pasting detailed descriptions of any issues you have into either Google or ChatGPT for assistance.

Good luck and I’ll see you in part 1 when you’re ready to go : )

[PLAY CLIP OF INSTALLING DOCKER AND VSCODE]