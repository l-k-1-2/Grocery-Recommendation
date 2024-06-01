# The Grocery Recommendation Algorithm
With the rising e-commerce market, local groceries and supermarkets are finding it tough to give their customers a good experience and generate enough order value to keep themselves afloat. This recommendation algorithm could help the store achieve both these targets.

## Objective

The purpose of this project is to use a grocery database and determine the items that are bought together, allowing the manager to group products together and recommend them to the customers, enhancing customer experience and generating order value.

## Need of the project

While it is argued that one could simply group items together based on their relevance to each other, we often fail to recognize a lot of underlying patterns which are waiting to be uncovered. A lot of these patterns could be area-specific, for example, generally it wouldn't make a lot of sense to recommend an umbrella to a backpack buyer, however, a city with unpredictable rains and a lot of young working professionals / students would be interested in buying an umbrella with the backpack. In such a way, data helps you uncover patterns which might not seem logical at first, but would help sell more items.

## Project in detail

The dataset used for the project contains the data of member id and the items they bought on a particular date. The project starts with exploratory data analysis on the data set to understand the data better. The dataset is a flat one where the items are not recorded by order, but by member id and date. An assumption was taken that a member visited the store only once on a particular date and everything they bought that day is part of a single order. Following this assumption, the sales were categorized based on year of sale, date of month, day of the week, the product and others independently. A comparative chart for each of the category was also developed to unearth undelying patterns.

The given scenario suggested that Apriori algorithm could be a good choice to determine the frequently bought together items. We determined the frequently bought items in a itemset of 1,2,3 and 4 items. With a minimum support of 25%, the algorithm identified 37 such combinations which were bought together frequently. Out of these we only picked the conbinations where 4 or more things were bought together. Taking those items, we used associate rule mining to determine the combinations with a minimum confidence of 50%. 
