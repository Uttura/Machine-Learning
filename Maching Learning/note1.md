# Eighth Day of Machine learning
## How Models Work

- There are lot's of different models or method of making the models, but we will be learning the most basic and the simplest of all called Decision Tree.
- The Machine learning works exactly the way we do prediction, analysis and valuation of the property using the data from past while considering the method or data and variables used to do those.
- There are other fancier models which gives more accurate results but the decision tree is easy to understand, and they are the basic building block for some of the best models in data science.

-Link to the diagram: https://storage.googleapis.com/kaggle-media/learn/images/7tsb5b1.png
- Here, we divided houses into two categories. The predicte price for any house under consideration is the historical average price of house in the same category.

- We use data to decide how to break the house into two groups, and then again to determine the predicted  price in each group.
- This step of capturing patterns from data is called fitting or training the model. The data used to fit the model is called the training data.
- From the above decision tree we cannot conclude the house price in the most accurate way cause it is only considering one thing were as there are lot's of thing to see for the price of house like bathroom, size, location and soon.
- So now if we add atleast one more variable or factor affecting the house price then it will be more accurate compare to previous one.
- let's add of the preice one more thing in the same tree but it is filter aftet the does it have more then two bedrooms or not and after the final output we can predict the price.

- link to the diagram: https://storage.googleapis.com/kaggle-media/learn/images/R3ywQsR.png
- now we can predict the price aftrer all the characteristics it has and the final predicte price is at the bottom of the tree.
- The point at the bottom where we make a prediction is called `leaf`
