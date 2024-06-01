# The Grocery Recommendation Algorithm

With the increasing popularity of e-commerce, local groceries and supermarkets are facing challenges to provide their customers a positive experience and generate sufficient order value to sustain themselves. This recommendation algorithm can help the store achieve both these objectives.

## Objective

The purpose of this project is to use a grocery database and determine the items that are bought together, allowing the manager to group products together and recommend them to the customers, enhancing customer experience and generating order value.

## Need of the project

While it is often argued that one can simply group items together based on their relevance, we often fail to recognize the underlying patterns. A lot of these patterns could be area-specific. For instance, it wouldn't make much sense to recommend an umbrella to a backpack buyer. However, in a city with unpredictable rains and a lot of young working professionals or students, it would be more logical to recommend an umbrella with the backpack. Data helps in uncovering such patterns, which are not always immediately apparent but can help sell more items.

## Project in detail

The dataset used for the project contains data on member id and the items they bought on a particular date. The project starts with exploratory data analysis to understand the data better. The dataset is a flat one in the sense that the items are not recorded by order, but by member id and date. An assumption is taken that a member visited the store only once on a particular date and everything they bought that day is part of a single order. Following this assumption, the sales are categorized based on year of sale, date of month, day of the week, the product, and others. A comparative chart for each of the category is developed to unearth underlying patterns.

The given scenario suggests that the Apriori algorithm could be a good choice to determine the frequently bought together items. We have determined the frequently bought items in a itemset of 1,2,3, and 4 items. With a minimum support of 25%, the algorithm identified 37 such combinations. Out of these, we have only picked the combinations where 4 or more things are bought together. Taking these items, we used associate rule mining to determine the combinations with a minimum confidence of 50%.

