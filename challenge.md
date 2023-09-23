## Data Science Dashboard

We will use Streamlit as our prototype dashboard tool, but we need to embed that streamlit app into a Docker container.

### References

- [download](https://www.learntospark.com/2021/04/download-data-from-dbfs-to-local.html)
- [Streamlit and Docker](https://maelfabien.github.io/project/Streamlit/#)
- [Docker and Heroku Streamlit setttings](https://www.r-bloggers.com/2020/12/creating-a-streamlit-web-app-building-with-docker-github-actions-and-hosting-on-heroku/)
- [Dockerfile cheat sheet](https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index)
- [Publish container to Heroku](https://devcenter.heroku.com/articles/container-registry-and-runtime)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Heroku sign-up](https://signup.heroku.com/)
- [The Actual Difference Between Statistics and Machine Learning](https://towardsdatascience.com/the-actual-difference-between-statistics-and-machine-learning-64b49f07ea3)
- [Statistics versus machine learning](https://www.nature.com/articles/nmeth.4642.pdf)

#### Technologies for coding challenge

- __Required:__ [Streamlit Dashboard](https://streamlit.io/)
- __Required:__ [Docker](https://www.docker.com/)
- __Required:__ [PySpark](https://spark.apache.org/docs/latest/api/python/#:~:text=PySpark%20is%20an%20interface%20for,data%20in%20a%20distributed%20environment.) and [DataBricks](https://databricks.com/)

#### Repo Structure

Your repo should be built so that I can clone the repo and run a Docker command as described in your `readme.md` that allows me to see your app in my web browser without requiring me to install Streamlit on my computer.

1. Fork this repo to your private space
2. Add me to your private repo in your space
3. Build your app and Docker container
4. Update your `readme.md` with details
5. Publish your app to Heroku.
6. Submit the link to your repo to me in Canvas

#### Driving needs

_Each of the items below must be addressed by your app._

1. Use the Chipotle data provided during the last challenge and Pyspark/Databricks to build a display dataset for your dashboard.
    - Facilitate a compelling story comparing same_day_brands and same_month_brands for Chipotle stores.      
    - Build a dataset that is easy to use in Pandas in your app.   
    - Display your Pyspark code in your app and a description of your data format.      
2. Display your table of SafeGraph data that includes;
    - Filter option to see locations with more than X visits.   
    - At least the following columns should be displayed - `placekey, location_name, street_address, city, date_range_start, latitude, longitude, raw_visit_counts` and the brands columns.   
4. Multiple visualizations/tables.
    - A spatial map that displays insight about related brands.   
    - Charts facilitate comparison of brands insights.   
5. An additional interactive element that allows the user to investigate the visualizations.

### Vocabulary/Lingo Challenge

_Within a `.md` file in your repository and as a submitted `.pdf` or `.html` on Canvas, address the following items;_

1. Provide a link to your project repo.
2. Provide a link to your published Heroku app.
3. Explain the added value of using DataBricks in your Data Science process (using text, diagrams, and/or tables).
4. Compare and contrast PySpark to either Pandas or the Tidyverse (using text, diagrams, and/or tables).
5. Explain Docker to somebody intelligent but not a tech person (using text, diagrams, and/or tables).
6. Detail the difference between statistical regression and machine learning regression (compare and contrast).

_Your answers should be clear, detailed, and no longer than is needed. Imagine you are responding to a client or as an interview candidate._

- _Clear:_ Clean sentences and nicely laid out format.
- _Detailed:_ You touch on all the critical points of the concept. Don't speak at too high a level.
- _Brevity:_ Don't ramble. Get to the point, and don't repeat yourself.
