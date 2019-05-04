import sys

import pandas as pd

csv_file = folder = sys.argv[1]
data = pd.read_csv(csv_file, encoding='UTF-8')
output = open("output.vcf", "w+")

# parse jobs
jobs = []
for _, row in data.iterrows():
  print(str(row))
  output.write('BEGIN:VCARD\n')
  output.write('VERSION:2.1\n')
  output.write('N:{}\n'.format(row['Name']))
  output.write('TEL;TYPE=WORK,VOICE:{}\n'.format(row['Phone 1 - Value']))
  output.write('TEL;TYPE=HOME,VOICE:{}\n'.format(row['Phone 1 - Value']))
  output.write('END:VCARD\n')

output.close()
