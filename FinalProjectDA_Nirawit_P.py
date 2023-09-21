from matplotlib import pyplot as plt
import pandas as pd

# Read the CSV file into a DataFrame
bigmac_df = pd.read_csv('big mac.csv', parse_dates=['date'])
us_min_df = pd.read_csv('Minimum-Wage-USA.csv')
thai_min_df = pd.read_csv('Minimum-Wage-Thai.csv')




# Filter for big mac in Thailand
thai_df = bigmac_df[bigmac_df['name'] == 'Thailand']
# Filter for big mac in the United States
us_df = bigmac_df[bigmac_df['name'] == 'United States']

# merge





# Create the first figure and chart (Thailand and USA)
fig1 = plt.figure(figsize=(6, 5))
ax1 = fig1.add_subplot(2, 1, 1)
ax2 = ax1.twinx()
thai_line = thai_df.plot(kind='line', x='date', y='local_price', ax=ax1, label='local_price_THB', color='#3776ab')
us_line = us_df.plot(kind='line', x='date', y='local_price', ax=ax2, label='local_price_USD', color='red')
ax1.legend(loc='upper left')
ax2.legend(loc='center left')
ax1.set_ylabel('Local Price (THB)', color='#3776ab')
ax2.set_ylabel('Local Price (USD)', color='red')
ax1.set_title('Big Mac price : Thailand vs. USA')

# Create the second chart (Thailand and USA minimum wage)
ax3 = fig1.add_subplot(2, 1, 2)
ax4 = ax3.twinx()
thai_min_line = thai_min_df.plot(kind='line', x='DATE', y='perday', ax=ax3, label='THB_perday', color='#3776ab')
usa_min_line = us_min_df.plot(kind='line', x='DATE', y='perday', ax=ax4, label='USD_perday', color='red')
ax3.legend(loc='upper left')
ax4.legend(loc='center left')
ax3.set_ylabel('THB_perday', color='#3776ab')
ax4.set_ylabel('USD_perday', color='red')
ax3.set_title('Minimum Wage per day : Thai VS USA')





# Show the plots
plt.tight_layout()
plt.show()