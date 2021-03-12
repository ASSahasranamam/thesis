
#  Statistics & Data Analysis


##  Req

#### Import Requirements

##### HTML formatting



from IPython.display import HTML

HTML("""<style type="text/css">
  table.dataframe td, table.dataframe th {
    max-width: none;
  }
</style>
""")


HTML("""<style type="text/css">
  table.dataframe td, table.dataframe th {
    max-width: none;
    white-space: normal;
  }
</style>
""")


HTML("""<style type="text/css">
  table.dataframe td, table.dataframe th {
    max-width: none;
    white-space: normal;
    line-height: normal;
  }
</style>
""")


HTML("""<style type="text/css">
  table.dataframe td, table.dataframe th {
    max-width: none;
    white-space: normal;
    line-height: normal;
    padding: 0.3em 0.5em;
  }
</style>
""")

import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype

from scipy.stats import *
import scikit_posthocs as sp
from pingouin import friedman




data = pd.read_csv("./NewCols.csv")



## Calculating the differences between the noremalized values. 

data_control = data[data["treatment"] == "baseline"]
data_treatment = data[data["treatment"] == "intravenous LPS"]
procData = data_treatment


procData['diff_AVAR2'] = (
    np.array(data_treatment["AVAR2"]) - np.array(data_control["AVAR2"])).tolist()
procData["diff_CVAR2"] = (
    np.array(data_treatment["CVAR2"]) - np.array(data_control["CVAR2"])).tolist()
procData["diff_AWT2"] = (np.array(data_treatment["AWT2"]) -
                         np.array(data_control["AWT2"])).tolist()
procData["diff_CWT2"] = (np.array(data_treatment["CWT2"]) -
                         np.array(data_control["CWT2"])).tolist()


procData["diff_total2"] = (
    np.array(data_control["total2"]) - np.array(data_treatment["total2"])).tolist()
procData["diff_totalA"] = (
    np.array(data_treatment["totalA"]) - np.array(data_control["totalA"])).tolist()
procData["diff_totalC"] = (
    np.array(data_treatment["totalC"]) - np.array(data_control["totalC"])).tolist()
procData["diff_totalWT"] = (np.array(
    data_treatment["totalWT"]) - np.array(data_control["totalWT"])).tolist()
procData["diff_totalVar"] = (np.array(
    data_treatment["totalVar"]) - np.array(data_control["totalVar"])).tolist()


newDF=  data_control[["testGroup","tg2"]]
newDF


newDF.rename(columns = {'testGroup':'c_tg','tg2':'c_tg2'},  inplace=True) 
newDF


newDF.index = procData.index
procData= pd.concat([procData,newDF], axis=1)




#### Difference Table



pd.set_option('display.max_rows', procData.shape[0]+1)

diff_data = procData.loc[ :,"diff_AVAR2":"diff_totalVar" ]


diff_data.describe()

diff_data.var()


diff_data.std()


diff_data.skew()


diff_data.kurtosis().tolist()

diff_data.kurtosis()



## QQ Data for LPS



### summary Statistics 

#### Baseline - summary stats - summary stats

baseline_summary = data_control.loc[:,'AWT2':'total2']

baseline_summary.describe()

#### Variance & STD DEv

baseline_summary.var()

baseline_summary.std()

#### skew

scipy.stats.skew(baseline_summary).tolist()


#### Kurtosis

scipy.stats.kurtosis(baseline_summary).tolist()


#### Intravenous LPS - summary stats

LPS_summary = data_treatment.loc[:,'AWT2':'total2']
LPS_summary.describe()

#### Variance & STd DEv

LPS_summary.var()


LPS_summary.std()

#### Skew


scipy.stats.skew(LPS_summary)

#### Kurtosis


scipy.stats.kurtosis(LPS_summary)


## Graph Data - 

from plotnine import *
ggplot(data, aes(x='treatment', y='AWT2') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))


a = 0.05

wilcoxon(data_control["AWT2"],data_treatment["AWT2"])


ggplot(data, aes(x='treatment', y='CWT2') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))


a = 0.05

wilcoxon(data_control["CWT2"],data_treatment["CWT2"])


ggplot(data, aes(x='treatment', y='AVAR2') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))


a = 0.05

wilcoxon(data_control["AVAR2"],data_treatment["AVAR2"])


ggplot(data, aes(x='treatment', y='CVAR2') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))


a = 0.05

wilcoxon(data_control["CVAR2"],data_treatment["CVAR2"])


ggplot(data, aes(x='treatment', y='total2') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))


a = 0.05

wilcoxon(diff_data["diff_total2"])


ggplot(diff_data, aes(x=0,y='diff_total2') ) + geom_boxplot() + geom_jitter(diff_data)




data_plot = data_treatment
controlData = data_control['total2']
controlData

data_plot["ctrl_total2"]=controlData.to_list()
data_plot




ggplot(data_plot,aes(x='total2',y='ctrl_total2') )  + geom_point() + geom_smooth(method='lm')



from sklearn import linear_model
lm = linear_model.LinearRegression()


shapiro_test = shapiro(data_control['total2'])
shapiro_test

shapiro_test = shapiro(data_treatment['total2'])
shapiro_test

shapiro_test = shapiro(diff_data['diff_total2'])
shapiro_test

ggplot(data, aes(x='treatment', y='totalVar') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))


a = 0.05

wilcoxon(diff_data["diff_totalVar"])


ggplot(data, aes(x='treatment', y='totalWT') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))


a = 0.05

wilcoxon(diff_data["diff_totalWT"])


ggplot(data, aes(x='treatment', y='totalA') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))


a = 0.05

wilcoxon(diff_data["diff_totalA"])


ggplot(data, aes(x='treatment', y='totalC') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))


a = 0.05

wilcoxon(diff_data["diff_totalC"])




## Statistics

### Total 2 Comparison

#### Wilcoxon non-parametric

a = 0.05

w, p = wilcoxon(data_control["total2"],data_treatment["total2"])
print(w, p)

if (p < a):
    print("As P"+str(p)+" is less than a: "+str(a))
    print( "we reject the Null Hypothesis.")
    print(". There is significant difference betwween the groups")
else: 
    print("As P"+p+" is larger than a: "+str(a))
    print( "we FAIL TO reject the Null Hypothesis.")
    print(". There is NOT a significant difference betwween the groups")

#### Freidman's Anova

sp.posthoc_nemenyi_friedman(diff_data)

Friedman Tes 

### other

a = 0.05

w, p = wilcoxon((data_control["totalA"]/data_control["totalC"] ),(data_treatment["totalA"]/data_treatment["totalC"]))
print(w, p)

a = 0.05

w, p = wilcoxon((data_control["AVAR2"]/data_control["CVAR2"] ),(data_treatment["AVAR2"]/data_treatment["CVAR2"]))
print(w, p)

a = 0.05

w, p = wilcoxon((data_control["AWT2"]/data_control["CWT2"] ),(data_treatment["AWT2"]/data_treatment["CWT2"]))
print(w, p)

ggplot()+geom_histogram(procData,aes(x="tg2"))

ggplot()+geom_histogram(procData,aes(x="mutant"))

ggplot()+geom_bar(procData,aes(x="spliceVariant",fill="mutant"))

ggplot()+geom_col(procData,aes(x="spliceVariant",y="diff_totalA/diff_totalC",fill="mutant"))

a = 0.05
diff_data = procData[(data["totalC"] > 0 ) & (data["totalA"] > 0 )]
ggplot()+geom_histogram(diff_data,aes(x="tg2"))


w, p = wilcoxon((diff_data["totalC"] )/(diff_data["totalA"]))
print(w, p)

a = 0.05

w, p = wilcoxon(data_control["total2"],data_treatment["total2"])
print(w, p)



2 graphs 

1. Do the Table
3. Black and white
3. Make sure its not sloppy
4. 

control, LPS & Difference.

correlation plot for each patient - total 2 & diff_total2

Look for A/C ratios 

ggplot(data_plot,aes(x='total2',y='ctrl_total2') )  + geom_point(colour) + geom_smooth(method='lm')
