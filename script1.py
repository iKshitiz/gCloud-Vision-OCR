import re
from vision import fetchText
import json

string = fetchText('report1.jpg')

res = {}

res['Age'] = ' '.join((re.search('Age: \d+\sYears', string).group()).split()[1:])
res['Name'] = ' '.join((re.search('Name (Mr\.|Mrs\.|Ms\.) \w+\s\w+', string).group()).split()[1:])
res['Gender'] = ' '.join((re.search('Gender \w+', string).group()).split()[1:])
res['Ref by'] = ' '.join((re.search('Ref\sBy:\s\w+', string).group()).split()[2:])

res['HEMOGLOBIN: Hb, BLOOD'] = ' '.join((re.search('HEMOGLOBIN:\s\w+\,\s\w+\s\(\w+\)\s\d+\.\d+', string).group()).split()[-1])
res['CREATININE SERUM'] = ' '.join((re.search('CREATININE\,\sSERUM\s\(.*?\)\s\d+\.\d+', string).group()).split()[-1])
res['A/c status'] = ' '.join((re.search('Aic\s\w+\s\w', string).group()).split()[-1])
res['Lab No'] =  ' '.join((re.search('\d+\sLab', string).group()).split(' ')[0])

print(res)

with open('result.json', 'w') as fp:
    json.dump(res, fp)