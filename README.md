# MindSister

## Getting Started
VSCode users:
* You can clone this repo by going into your terminal and running the command `git clone "https://github.com/JackTubby/hackathon-team-7.git"`

## Working with the project

### Keep Your Code Updated
Many people will be working on this repo so following these steps will help ensure that we keep our code in its own branches and we can merge it as we go.

### Start New Features on New Branches
* Regularly run git pull to ensure your local code is synchronized with the latest updates from the main branch.
* When beginning work on a new feature, create a new branch by using: - `git checkout -b "BRANCH NAME"` - This command switches you to a new branch dedicated to your feature.

### Commit Your Changes Incrementally
* As you develop the feature, think about dividing the work into manageable parts. For each part, use the following commands to commit your changes to your branch: 
`
git add .
`
`
git commit -m "Brief description of changes"
`
`
git push
`
This sequence stages your changes, commits them with a brief message, and pushes them to your branch on GitHub.

### Create a Pull Request When Ready
Once your feature is complete and ready for integration, initiate a pull request:
* Go to the 'Pull Requests' tab in the GitHub repository.
* Click 'New Pull Request'.
* Select your feature branch and the main branch to merge into.
* Click 'Create Pull Request'.
