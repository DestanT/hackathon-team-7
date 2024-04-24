# MIND SISTER

[Link to the deployed site]()

# Project Overview

Mind Sister recognises women's specific needs when dealing with mental disorders and offers a platform where women can easily express themselves and reach out fo r help in a mental health forum.

This platform was built using Django, Python, HTML and CSS. The site was deployed on Heroku.

Mind Sister is Team 7 Mindful Coders' project submission for Code Institute's "Women's Health Reimagined" hybrid hackathon in London, April 2024.

## Meet the Development Team
- [Destan](https://github.com/DestanT) - Scrum Master | Backend

- [Jack](https://github.com/JackTubby) - Backend

- [Mikaela](https://github.com/mikavir) - Backend | Frontend

- [Istem](https://github.com/techistem) - Content

- [Taher](https://github.com/TaherCCG) - Frontend | Wireframes | Imagery

- [Lydia](https://github.com/Lydiajoy97) - Backend

- [Ren](https://github.com/Discoveren) - Frontend | Wireframes 

- [Karina](https://github.com/kkumyk) - README


### TABLE OF CONTENTS
- [User Experience](#user-experience)
    - [Strategy Plane](#strategy-plane)
    - [Scope Plane](#scope-plane)
    - [Structure Plane](#structure-plane)
        - [Database Design](#database-design)
        - [User Stories](#user-stories)
    - [Skeleton Plane](#skeleton-plane)
        - [Wireframes](#wireframes)
    - [Surface Plane](#surface-plane)
        - [Typography](#typography)
        - [Colour Palette](#colour-palette)
        - [Imagery](#imagery)
- [Credits](#credits)
- [Internal Docs](#internal-docs)

<hr>

# User Experience

## Strategy Plane

[Research shows ](https://www.bma.org.uk/media/2115/bma-womens-mental-health-report-aug-2018.pdf) that there are differences between women and men in how they express mental distress. This is seen in the prevalence of common mental disorder such as anxiety and depression, self-harm, substance misuse and suicide; pathways into treatment and support and in therapeutic preferences. Current gender neutral approaches to service provision fail to recognise the specific needs of women. If health care truly is to be personalised, it must respond appropriately to gendered differences in mental health:

- 1:6 adults (17.0%) had a common mental disorder.
- 1:5 women (20.7%) compared with 1:8 men (13.2%).
- the rate is largely stable in men compared with a steady increase in women.
- 1:5 16-25yr women report recent self-harm.
- Suicide rates in women are at their highest for a decade.

### Project Goals

This section aims to answer the key question: What problems are we trying to solve with MindSister? 

## Scope Plane
When planning the Mind Sister's features and scope, we drew up a Desirability, Importance and Viability analysis of all the features to be included in the project, and ranked each of these by order of importance from low (1) to high (5). The features that ranked the highest will be prioritised and delivered as part of the MVP.

<table>
<thead>
<tr>
<th>#</th>
<th>Feature</th>
<th>Target User</th>
<th>Desirability</th>
<th>Importance</th>
<th>Viability</th>
<th>Delivered</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Accounts</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>User Role Permissions</td>
<td>All Users <sup>1</sup></td>
<td>5</td>
<td>5</td>
<td>5</td>
<td>✅</td>
</tr>
<tr>
<td>2</td>
<td>Account Registration</td>
<td>All Users <sup>1</sup></td>
<td>5</td>
<td>5</td>
<td>5</td>
<td>✅</td>
</tr>
<tr>
<td>3</td>
<td>User Profile Page</td>
<td>Registered Users</td>
<td>5</td>
<td>5</td>
<td>5</td>
<td>✅</td>
</tr>
<tr>
<td>Navigation</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Top Navigation to include: logo and my account (register, login)</td>
<td>All Users <sup>1</sup></td>
<td>5</td>
<td>5</td>
<td>5</td>
<td>✅</td>
</tr>

<td>Profiles</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>User Profile page</td>
<td>All Users <sup>1</sup></td>
<td>5</td>
<td>5</td>
<td>5</td>
<td>✅</td>
</tr>
<td>Forum</td>
<td>Topic page</td>
<td>Registered Users</td>
<td>5</td>
<td>5</td>
<td>5</td>
<td>✅</td>
</tr>

</tbody>
</table>

1. All Users: site visitors and logged in users

## Structure Plane

### Database Design

#### Entity Relationship Diagram

### User Stories

<table>
<thead>
<tr>
<th>#</th>
<th>Target User</th>
<th>User Story</th>
</tr>
</thead>
<tbody>
<tr>
<td>VIEWING &amp; NAVIGATION</td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>Visitor</td>
<td>I want to be able to navigate around the site and understand how it can benefit me.</td>
</tr>
<tr>
<td>2</td>
<td>Visitor</td>
<td>I want to be able to navigate around the site to learn more about the team behind the site and confirm that this site is valid and secure to use and how users' personal information is handled on the site.</td>
</tr>
<tr>
<td>3</td>
<td>Visitor</td>
<td>I can click on Register button on Home Page so that I can navigate to Registration Page.</td>
</tr>
<tr>
<td>4</td>
<td>Visitor</td>
<td>on the Registration Page I can fill a form with my name, e-mail address and phone number so that I can create an account as a user.</td>
</tr>
<td>REGISTRATION &amp; USER ACCOUNTS</td>
<td></td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>User</td>
<td>I can easily register for an account, be able to view my profile and control what information about me other users can see.</td>
</tr>
<tr>
<td>6</td>
<td>User</td>
<td>after registration I will appear among the registered users and can start communicating with them.</td>
</tr>
<tr>
<td>7</td>
<td>User</td>
<td>after registration I will have options to start a thread on the Forum page and leave comments on the existing pages.</td>
</tr>
</tbody>
</table>


## Skeleton Plane

### Wireframes

<details>
  <summary>Initial Wireframes</summary>

<img src="documentation/initial-landing-page.png" style="width: 798px; max-width: 100%;">

<img src="documentation/initial-forum-page.png" style="width: 798px; max-width: 100%;">

<img src="documentation/initial-chatbox-page.png" style="width: 798px; max-width: 100%;">

</details>

<hr>
The initial wireframes in the above section were created based on the idea of building a Buddy System for women experiencing mental health problems. However, we identified that there are several issues with this idea that can potentially create more problems instead of solving them. The project's idea had to be changed, and so did the wireframes:

#### Visitor
<img src="documentation/thumbnail_new user landing page.png" style="width: 798px; max-width: 100%;">

<hr>

#### Registered User
<img src="documentation/thumbnail_returning user landing page.png" style="width: 798px; max-width: 100%;">


## Surface Plane

### Typography
<img src="documentation/nunito-sans.png" style="width: 798px; max-width: 100%;">

### Colour Palette

<img src="documentation/colour-palette.png" style="width: 798px; max-width: 100%;">

### Imagery
<strong>Mind Sister's Logo</strong>

<img src="documentation/logo.png" style="width: 198px; max-width: 100%;">




---
---

### Features

### Accessibility


## Technologies Used

- ### Languages:


- ### Frameworks and libraries:


- ### Databases:

- ### Other tools:


## Flowcharts


## Deployment and Local Deployment

## Testing

## Bugs

### Known Bugs

### Solved Bugs

## Media

## Credits

#### Mental Health Related Research Sources:

[Addressing unmet needs inwomen’s mental health](https://www.bma.org.uk/media/2115/bma-womens-mental-health-report-aug-2018.pdf)

#### Well Structured Documentation Examples:

- https://github.com/rachel-o-donnell/rising-women
- https://github.com/JoyZadan/shop-kbeauty

    
## Internal Docs
<details>
  <summary>Getting Started (Internal Use)</summary>

VSCode users:
* You can clone this repo by going into your terminal and running the command `git clone "https://github.com/DestanT/hackathon-team-7"`

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

Once you are ready to move on to the next feature run `git checkout main` to switch back to the main branch & then `git pull` to get the new changes and then follow the steps again.
</details>