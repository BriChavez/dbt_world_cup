# _WORLD CUP DATA_


### By _**Bri Chavez**_

#### _This Code takes a CSV, puts in BigQuery, transforms it with DBT, then off to Google Data Studio to make pretty interactive graphs_



## Description

_This data was scraped from the world cup wiki page by one Pratap Vardhan; git hub link to the csv https://github.com/pratapvardhan/FIFAWorldCup/blob/master/squads.csv. /n I took the repo file csv as raw github user data, uploaded it into a pandas dataframe to do some transformations and renaming. Then I sent it off to BigQuery to be Uploaded to DBT. Inside DBT, the data was transformed further to follow a snowflake style modeling system. Afterwards, it was brought into Google Data Studio to make crazy cool interactive maps following our dbt model. Feel free to explore the graph below to find out more in depth information on world cup teams and players._

[!Click here for my Google Data Studios interactive map](data/map.jpg)](https://brichavez.github.io/dbt_world_cup/)


## Technologies Used

* _Python_
* _Pandas_
* _Numpy_
* _Google Cloud Storage_
* _Google Cloud BigQuery_
* _Google Cloud APIs_
* _Google Data Studio_
* _Jinja_
* _YAML_
* _DBT_
* _SQL_
* _HTML_
* _Markdown_



## Navigating the map

* _You can click on countries on the map to see some of their team information in the table to the left. You will also notice the Player bar graph on the bottom of the page update its information, limiting the players to only be in the country you clicked on. Also updating will be the Clicker counters to the right of the map. You may dive deeper, clicking on any field you find interesting. Keep in mind, if you find the map to be stuck or unresponsive, you are trying to query larger than the parameters. Look around for any text in bold, unselect it by clicking on it again, and you will be good to go to keep exploring as your heart desires._


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


## License

_Come holler at me if you have questions, comments, suggestions. Im open to feedback or csv requests._

Copyright (c) _July 2022_ _Bri Chavez_