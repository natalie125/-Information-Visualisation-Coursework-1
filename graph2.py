import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the uploaded CSV file
file_path = '/Users/natalieleung/Desktop/IV/query_data2/demographics.csv'
data = pd.read_csv(file_path)

# Define the age groups and the total
age_groups = [
    ('Female 0 - 4', 'Male 0 - 4'),
    ('Female 5 - 11', 'Male 5 - 11'),
    ('Female 12 - 17', 'Male 12 - 17'),
    ('Female 18 - 59', 'Male 18 - 59'),
    ('Female 60', 'Male 60'),
    ('Female total', 'Male total')
]

# Create a figure with subplots for the 6 age groups
fig, axes = plt.subplots(3, 2, figsize=(12, 15))  # 3x2 subplots
axes = axes.flatten()  # Flatten the 2D array of axes for easy iteration

for i, (age_group_female, age_group_male) in enumerate(age_groups):
    ax = axes[i]
    
    # Diagnostic print statement
    print(f"Type of axes[{i}]:", type(ax))

    # Scatter plot for each age group
    ax.scatter(data['Country of asylum (ISO)'], data[age_group_female], color='pink', label='Female')
    ax.scatter(data['Country of asylum (ISO)'], data[age_group_male], color='blue', label='Male')

    title = 'Population of age group 60+' if '60' in age_group_female else f'Population for age group {age_group_female.split()[1]} - {age_group_female.split()[-1]}'
    ax.set_title(title, fontsize=12)
    ax.set_xlabel('Country of Asylum (ISO)', fontsize=11)
    ax.set_ylabel('Population', fontsize=11)
    ax.legend(fontsize=11)

    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_horizontalalignment('right')
        label.set_fontsize(10)

# Adjust subplot spacing and margins
plt.subplots_adjust(bottom=0.18, hspace=0.5, wspace=0.3)  # Increased bottom margin

caption_part1 = "This graph shows the population distribution by age group and gender"
caption_part2 = "across 7 countries of asylum (including Afghanistan, Iran, Pakistan, Germany, Turkey,Switzerland and India), highlighting the highest number of Afghanistan refugees."
fig.text(0.5, 0.03, caption_part1, ha='center', va='bottom', fontsize=11, color='black')
fig.text(0.5, 0.015, caption_part2, ha='center', va='bottom', fontsize=11, color='black')


plt.show()

