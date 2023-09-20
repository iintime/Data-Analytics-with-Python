from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# อ่านไฟล์ csv
bigmac_df = pd.read_csv('big mac.csv', parse_dates=['date'])


# Filter ให้เหลือแค่ของไทย
thai_df = bigmac_df[bigmac_df['name'] == 'Thailand']
# Filter ให้เหลือแค่อเมริกา
us_df = bigmac_df[bigmac_df['name'] == 'United States']



fig = plt.figure(figsize=(10, 5))

# .subplots() ในวงเล็บไม่ใส่ คือ 1x1 หรือ 1รูป
ax1 = fig.subplots()
# .twinx() สร้างคู่ตรงข้าม, x คือ ใช้แกน x ร่วมกัน
ax2 = ax1.twinx()
thai_line = thai_df.plot(kind='line', x='date', y='local_price', ax=ax1, label='local_price_THB', color='#3776ab')
us_line = us_df.plot(kind='line', x='date', y='local_price', ax=ax2, label='local_price_USD', color='red')

ax1.legend(loc='upper left')
ax2.legend(loc='center left')
ax1.set_ylabel('Local Price (THB)', color='#3776ab')
ax2.set_ylabel('Local Price (USD)', color='red')

plt.show()