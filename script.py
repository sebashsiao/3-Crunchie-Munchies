import codecademylib3
import numpy as np

# generate array from csv file
calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

print(calorie_stats.size)
print(calorie_stats)

# There are 60 calories per serving of CrunchieMunchies. How much higher is the average calorie count of your competition?
average_calories = np.mean(calorie_stats)
print(average_calories)


# Does the average calorie count adequately reflect the distribution of the dataset? Let’s sort the data and see.
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

# Do you see what I’m seeing? Looks like the majority of the cereals are higher than the mean. Let’s see if the median is a better representative of the dataset.
median_calories = np.median(calorie_stats)
print(median_calories)

# While the median demonstrates that at least half of our values are over 100 calories, it would be more impressive to show that a significant portion of the competition has a higher calorie count that CrunchieMunchies.
# Calculate different percentiles and print them to the terminal until you find the lowest percentile that is greater than 60 calories. Save this value to the variable nth_percentile.
nth_percentile = np.percentile(calorie_stats, 3)
print(nth_percentile)


# While the percentile shows us that the majority of the competition has a much higher calorie count, it’s an awkward concept to use in marketing materials.
# Instead, let’s calculate the percentage of cereals that have more than 60 calories per serving. Save your answer to the variable more_calories and print it to the terminal.
more_calories = np.mean(calorie_stats > 60)
print(more_calories)

# Wow! That’s a really high percentage. That’s going to be very useful when we promote CrunchieMunchies. But one question is, how much variation exists in the dataset? Can we make the generalization that most cereals have around 100 calories or is the spread even greater?

# Calculate the amount of variation by finding the standard deviation. Save your answer to calorie_std and print to the terminal. How can we incorporate this value into our analysis?
calorie_std = np.std(calorie_stats)
print(calorie_std)

# Write a short paragraph that sums up your findings and how you think this data could be used to Yummy Corp’s advantage when marketing CrunchieMunchies.


