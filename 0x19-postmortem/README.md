# Project Title: Postmortem

## Table of Contents
1. About
2. Learning Objectives
3. Requirements
4. Getting Started
5. Contributing
6. License

## About <a name="about"></a>
This project is part of the curriculum of the ALX Software Engineering program. The main objective of this project is to understand and implement the On-call part of being a proficient software engineer, by writing a Postmortem
### Background Context
Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:
- To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
- And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

## Learning Objectives <a name="learning-objectives"></a>
At the end of this project, I am expected to be able to explain to anyone, without the help of Google:
To be on call you need at least 4 components:
- A service or website you want to monitor
- A monitoring tool
- An oncall management system
- A software engineer (that’s you)

## Requirement <a name="requirement"></a>
to write a comprehensive post-mortem detailing
- Issue Summary (that is often what executives will read) must contain:
	- duration of the outage with start and end times (including timezone)
	- what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
	- what was the root cause
- Timeline (format bullet point, format: `time - keep it short, 1 or 2 sentences`) must contain:
	- when was the issue detected
	- how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
	- actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
	- misleading investigation/debugging paths that were taken
	- which team/individuals was the incident escalated to
	- how the incident was resolved
- Root cause and resolution must contain:
	- explain in detail what was causing the issue
	- explain in detail how the issue was fixed
- Corrective and preventative measures must contain:
	- what are the things that can be improved/fixed (broadly speaking)
	- a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
- Be brief and straight to the point, between 400 to 600 words

## Getting Started <a name="getting-started"></a>
1. Clone this repository: `git clone https://github.com/Pritchad25/alx-system_engineering-devops.git`
2. Access the project directory: `cd 0x19-postmortem`
3. Read the readme file to get the context of the project

## Contributing <a name="contributing"></a>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License <a name="license"></a>
ALX 2024 - [alxafrica](https://www.alxafrica.com)
