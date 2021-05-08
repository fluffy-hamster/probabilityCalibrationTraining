# Introduction

ToDo

# What is calibration training?

> Calibrated probability assessments are subjective probabilities assigned by individuals who have been trained to assess probabilities in a way that historically represents their uncertainty. For example, when a person has calibrated a situation and says they are "80% confident" in each of 100 predictions they made, they will get about 80% of them correct. Likewise, they will be right 90% of the time they say they are 90% certain, and so on.
> 
> Calibration training improves subjective probabilities because most people are either "overconfident" or "under-confident" (usually the former).By practicing with a series of trivia questions, it is possible for subjects to fine-tune their ability to assess probabilities. For example, a subject may be asked:
> 
> Question. "A hockey puck fits in a golf hole"
> Answers: True , False
> Confidence: Choose the probability that best represents your chance of getting this question right...
> 
> 50% 60% 70% 80% 90% 100%
> 
> If a person has no idea whatsoever, they will say they are only 50% confident. If they are absolutely certain they are correct, they will say 100%. But most people will answer somewhere in between. If a calibrated person is asked a large number of such questions, they will get about as many correct as they expected. An uncalibrated person who is systematically overconfident may say they are 90% confident in a large number of questions where they only get 70% of them correct. On the other hand, an uncalibrated person who is systematically underconfident may say they are 50% confident in a large number of questions where they actually get 70% of them correct.
> 
> https://en.wikipedia.org/wiki/Calibrated_probability_assessment

# Technical details

* Questions are fetched via the https://opentdb.com/ API. 
* We save "session data" in an sqlite database. 

# How to use

* To run, first you will need to setup the local database. Please see the readme in 'backend' directory.
* Once the database is setup, you can run the frontend/MainConsole.py from the command line. 

# Future/work in progress

* Convert application to run on the Web (using Flask)
