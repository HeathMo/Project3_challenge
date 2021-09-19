# Where the Wild Things Are - Out of This World?

Topic: UFOs 

Objective: Obtain, clean, organize, visualize data regarding UFO & Bigfoot sightings.

![alien](images/flying_saucer.png)


We created a website to help show where ufo sightings have occurred around the world.

## CURRENTLY UNDER CONSTRUCTION 

**YouTube Declassified Navy UFO Video**

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/2TumprpOwHY/0.jpg)](https://www.youtube.com/watch?v=2TumprpOwHY)

**YouTube: Patterson - Gimlin Bigfoot Video, Stabilized by MK Davis**

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/Q60mSMmhTZU/0.jpg)](https://www.youtube.com/watch?v=Q60mSMmhTZU)

Step 1 
     -Identified UFO & BIGFOOT Dataset in Kaggle; Aligned with team to focus on only UFO dataset due to data size
    - Established CSV file and loaded on the group repo
    - Define Dependecies via jupyter notebook
    - Cleaned Data 
        - Dropped 2 columns as they were not required in the data set (duration (hours/min), date posted)
        - Aligned on dropping ~ 10K lines of data as there was missing city, state in the file 
        - Validated that there was no missing empty cells in the dataset
        - Re-established a new index count of the data 
        - update repo with CSV with 4 digit year vs 2 digit year.  The data structure was needed in order to complete the DB queries 
    - Aligned including Word cloud and included the following library in the virtual enviornment ( !pip install wordcloud   )
           - conda install -c conda-forge wordcloud
           - Saved with WordCloud PNG files
           /Users/petagaye/Desktop/DSCloned/Project3_challenge/word_cloud_first_review.png
           
           
           
           /Users/petagaye/Desktop/Screen Shot 2021-09-19 at 7.38.08 PM.png

### Team Members
- [Byron Pineda](https://github.com/byronpineda225)
- [Carlyse Thomas](https://github.com/CLyseT)
- [Felicia Felix](https://github.com/Felicia620)
- [Heather Mott](https://github.com/HeathMo)
- [Peta-Gaye Lysius](https://github.com/petagaye2001)
- [Ryan Flammia](https://github.com/rflammia-py)



    
Sources:
    https://data.world/timothyrenner/ufo-sightings
    https://www.kaggle.com/chemcnabb/bfro-bigfoot-sighting-report 
    https://stackoverflow.com/questions/59538815/how-can-i-create-index-for-python-pandas-dataframe
    
