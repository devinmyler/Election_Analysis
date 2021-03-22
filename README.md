# Election Audit Analysis
## Overview of Election
The purpose of the assignment was to audit votes in an election using a csv dataset of the individual, tabulated votes. Using only a list of individual votes, we will ascertain the total amount of votes, the total votes for each county and candidate involved, the percentage of votes for each county and candidate, which county had the largest voter turnout, and which candidate won the election.
## Election Audit Results
Looping through the data, we wrote a code to return the information we needed. Counting votes from each county and for each candidate, one by one. The code returned these results:

![election_results_printout](https://user-images.githubusercontent.com/78869891/111926424-2883b080-8a83-11eb-98c1-7be31352e0f8.png)

## Election-Audit Summary
This code could likely be used for any election without too many changes to the base code. 

Because the code was built using variables, the type of information wouldn't matter, as long as the structure was similar. For example, if you were tabulating votes for people's choice awards instead of elections, you could have this code find the winner by only changing the csv file and the wording of the printed results. The printed results are easy to find and replace for a new data set. 
![printed results](https://user-images.githubusercontent.com/78869891/111928408-e316b180-8a89-11eb-8bba-750388088ba3.png)

And even if the dataset was arranged a little differently, we could replace our csv query with a new number to return data from a different column. 

![candidate rows](https://user-images.githubusercontent.com/78869891/111928173-45bb7d80-8a89-11eb-8802-6275bb2d4163.png)

As for other elections, the code isn't built using any information than what was supplied in the csv, so the general structure of the code should be applicaple to any type of general election by county without changing the code. The only thing you would have to change is which csv file was being looked at.

![filepath_csv](https://user-images.githubusercontent.com/78869891/111928515-3d177700-8a8a-11eb-8075-1c77dbcda202.png)

I believe this general code structure could be used for a lot of different applications. If the variables were named more generically, it's reach could extend beyond elections, as well.
