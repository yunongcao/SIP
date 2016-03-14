import pandas as pd
import numpy as np
from pymining import seqmining, itemmining, assocrules, perftesting
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set()

studydf = pd.read_csv("studydf.csv")
violationdf = studydf[['INSPECTION DATE','VIOLATION CODE']].reset_index()
violationdf['VIOLATION CODE'] = violationdf['VIOLATION CODE'].astype('str')
plotseries = violationdf['VIOLATION CODE'].value_counts().iloc[0:20]
ax = sns.barplot(y=plotseries.index, x=plotseries.values, palette="Blues_d")
testdf = violationdf.groupby(['CAMIS'])['VIOLATION CODE'].apply(list)
minelist = testdf.tolist()[0:10]
minelist = tuple(tuple(x) for x in minelist)
relim_input = itemmining.get_relim_input(minelist)
item_sets = itemmining.relim(relim_input, min_support=2)
rules = assocrules.mine_assoc_rules(item_sets, min_support=2, min_confidence=0.5)
print rules
freq_seqs = seqmining.freq_seq_enum(minelist, 2)
print freq_seqs
rules2 = assocrules.mine_assoc_rules(item_sets, min_support=1, min_confidence=0.5)
print rules2