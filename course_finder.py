#!/usr/bin/python3

import pandas as pd

counter = 0

keyword = str(input('Ano ang keyword base sa hinahanap mong kurso?: '))

data = pd.read_csv('courses.csv', encoding='ISO-8859-1')

passed = list(data.sort_values(by='Grade Achieved', ascending=False).head(37)['Course Name'])

matched_courses = []

for course in data['Course Name']:
    if course.lower().find(keyword.lower()) != -1:
        if course in passed:
            continue
            
        matched_courses.append(course)
        
        counter += 1

for i in sorted(matched_courses):
    print(i)
    
print(f'\nNo. of courses matched - {counter}')
        
        
