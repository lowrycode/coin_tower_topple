# Coin Tower Topple

**Coin Tower Topple** is a 2-player game where players add coins to a tower until it gets too high and "topples". A player wins the game when their opponent causes the tower to topple.

![Coin Tower Topple](readme-images/coin-tower-topple.jpg)

The game makes use of a machine learning technique called **Reinforcement Learning**, specifically *Q-Learning*, to train an AI agent to learn the optimal moves to maximize its chances of winning.

The game is written in Python and played in a terminal window. It is deployed on Heroku using Code Institute's mock terminal. You can access the live game <a href="https://coin-tower-topple-754aefe8d2c6.herokuapp.com/" target="_blank" rel="noopener">**here**</a>.

# Project Planning

The [**Project Planning**](project_planning.md) document outlines my personal goals for this project and includes flowcharts illustrating the code logic. I chose to create this game because:
- It provided an opportunity to explore Reinforcement Learning techniques in machine learning.
- My children and I have enjoyed playing a similar maths-based strategy game while walking to and from school!

# Target Audience

The target audience for this game is users who enjoy playing maths-based strategy games.

The game settings (*Difficulty Level*, *Topple Height*, and *Possible Actions*) can be adjusted to add variety and accommodate players of all skill levels.





# Deployment

The project was deployed using <a href="https://www.heroku.com/" target="_blank" rel="noopener">**Heroku**</a> using the following steps:

## 1. Login to Heroku (or create an account)

If you don't already have an account then you'll need to create one. Heroku have stopped offering their free tier service so you will also be required to enter your bank details and choose a payment plan.

The website also requires 2-factor authentication (e.g. using an authenticator app on your smartphone).

## 2. Create app

On the dashboard, click **New** > **Create new app** and follow the prompts to create a new app.

<details>

<summary>Step-by-step visual instructions</summary>

![Instructions for how to create app - part 1](readme-images/heroku-create-app-1.jpg)

![Instructions for how to create app - part 2](readme-images/heroku-create-app-2.jpg)

</details>

## 3. Choose App Settings

*If still on the main dashboard, click on the link for the relevant app to go to the app page.*

In the **Settings** tab:
- scroll down to the **Config Vars** section and add the following Key/Value pair:
  - KEY: **PORT**
  - VALUE: **8000**
- scroll to the **Buildpacks** section and add buildpacks for **Python** and **Nodejs** (ensuring they are in that order)

<details>

<summary>Step-by-step visual instructions</summary>

### Add Config Vars (environment variables)

![Instructions for how to set Config Vars](readme-images/heroku-settings-1.jpg)

### Add Buildpacks

![Instructions for how to add Buildpacks](readme-images/heroku-settings-2.jpg)

</details>

## 4. Deploy App
In the **Deployment** tab, choose Github as deployment method, connect to the relevent repository and choose your preferred method of deployment.

***NOTE:*** *I chose manual deployment so the project was not redeployed every time I made changes to the README file.*

<details>

<summary>Step-by-step visual instructions</summary>

### Set deployment method and connect to GitHub

![Instructions for how to deploy app - part 1](readme-images/heroku-deploy-1.jpg)

### Choose automatic or manual deployment

![Instructions for how to deploy app - part 2](readme-images/heroku-deploy-2.jpg)

</details>