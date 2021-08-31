[TOC]

### 1. Outline some details on your chosen method to detect sentiment in the Email body. What are some of the alternative approaches you considered?

 >- I used the current mode from TextBlob because there are no labeled data. 
 >-  If there are some labeled data, I can train a model to fit our data. Basically, there are two main methods, based on rules or statistics and based on machine learning (map the text to vectors, then use SVM, GBDT, LR). 
 >- The most important thing is how to find the proper features to fit the specific task.   


### 2. Outline some details on your chosen method to detect if the Email body is related to Enron's oil & gas business. What are some of the alternative approaches you considered?
>- I planned to train an LDA model based on the Enron data set. However, it cost too much time to run the pr-processing function. So I have to stop the process and generate a sample set to finish the task in 8 hours.  
>- There are several ways to find the topics of the emails, like TF-IDF, page rank, or word2vec clustering.    


### 3. For both items above (in 1 & 2) describe the constraints of the methodology. i.e. How fast is the method? What is the max text length that the method(s) can support? Is the method perfect? If not, why? 
>- The method I used in this project are both very quick. Generally, the response time of the models is lower than the communication time between APIs. The maximum text length is the JSON parser limit, which is 4,194,304 bytes.  
>- Of course, it is not perfect. For example, suppose there is a very big email. Then the interface would time out since it requires too much to pre-process the data and call the model. In this case, we can split the text and assign it to different servers through Nginx when the length of the text is too long. Also, the models need to be optimized. 

### Result
>- Here are the reponses of my APIs.
>- http://localhost:7000/models/sentiment {"status": "200", "error_code": -1, "res": {"polarity": -0.10714285714285714, "subjectivity": 0.17857142857142858}}
>- http://localhost:7000/models/topic  {"status": "200", "error_code": -1, "res": {"oil": "false", "gas": "true"}}