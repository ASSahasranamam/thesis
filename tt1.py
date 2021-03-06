# %% markdown
#
# #  Statistics & Data Analysis
#
# %% markdown
# ##  Req
# %% markdown
# #### Import Requirements
# %% markdown
# ##### HTML formatting
# %% codecell

# %% codecell
import numpy as np
import pandas as z
import scipy
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from plotnine import *
from scipy.stats import *
import scikit_posthocs   as sp



data = pd.read_csv("./NewCols.csv")


# %% markdown
# ## Calculating the differences between the noremalized values.
# %% codecell
data_control = data[data["treatment"] == "baseline"]
data_control.to_csv("./control.csv")
data_treatment = data[data["treatment"] == "intravenous LPS"]
data_control.to_csv("./lps.csv")

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
    np.array(data_treatment["total2"]) - np.array(data_control["total2"])).tolist()
procData["diff_totalA"] = (
    np.array(data_treatment["totalA"]) - np.array(data_control["totalA"])).tolist()
procData["diff_totalC"] = (
    np.array(data_treatment["totalC"]) - np.array(data_control["totalC"])).tolist()
procData["diff_totalWT"] = (np.array(
    data_treatment["totalWT"]) - np.array(data_control["totalWT"])).tolist()
procData["diff_totalVar"] = (np.array(
    data_treatment["totalVar"]) - np.array(data_control["totalVar"])).tolist()

procData.to_csv("./procData.csv")
# %% codecell
newDF=  data_control[["testGroup","tg2"]]
newDF

# %% codecell
newDF.rename(columns = {'testGroup':'c_tg','tg2':'c_tg2'},  inplace=True)
newDF

# %% codecell
newDF.index = procData.index
procData= pd.concat([procData,newDF], axis=1)

# %% codecell

# %% markdown
# #### Difference Table
#
# %% codecell

pd.set_option('display.max_rows', procData.shape[0]+1)

diff_data = procData.loc[ :,"diff_AVAR2":"diff_totalVar" ]
diff_data.to_csv("./diffData.csv")
# %% codecell
diff_data.describe()
# %% codecell
diff_data.var()

# %% codecell
diff_data.std()

# %% codecell
diff_data.skew()

# %% codecell
diff_data.kurtosis().tolist()
# %% codecell
diff_data.kurtosis()
# %% codecell

# %% markdown
# ## QQ Data for LPS
#
# %% markdown
#
# ### summary Statistics
#
# #### Baseline - summary stats - summary stats
# %% codecell
baseline_summary = data_control.loc[:,'AWT2':'total2']

baseline_summary.describe()
# %% markdown
# #### Variance & STD DEv
# %% codecell
baseline_summary.var()
# %% codecell
baseline_summary.std()
# %% markdown
# #### skew
# %% codecell
scipy.stats.skew(baseline_summary).tolist()

# %% markdown
# #### Kurtosis
# %% codecell
scipy.stats.kurtosis(baseline_summary).tolist()

# %% markdown
# #### Intravenous LPS - summary stats
# %% codecell
LPS_summary = data_treatment.loc[:,'AWT2':'total2']
LPS_summary.describe()
# %% markdown
# #### Variance & STd DEv
# %% codecell
LPS_summary.var()

# %% codecell
LPS_summary.std()
# %% markdown
# #### Skew
#
# %% codecell
scipy.stats.skew(LPS_summary)
# %% markdown
# #### Kurtosis
#
# %% codecell
scipy.stats.kurtosis(LPS_summary)

# %% markdown
#
# %% markdown
# ## Graph Data -
# %% codecell
from plotnine import *
ggplot(data, aes(x='treatment', y='AWT2') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))
# %% codecell
a = 0.05

wilcoxon(data_control["AWT2"],data_treatment["AWT2"])

# %% codecell
ggplot(data, aes(x='treatment', y='CWT2') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))

# %% codecell
a = 0.05

wilcoxon(data_control["CWT2"],data_treatment["CWT2"])

# %% codecell
ggplot(data, aes(x='treatment', y='AVAR2') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))

# %% codecell
a = 0.05

wilcoxon(data_control["AVAR2"],data_treatment["AVAR2"])

# %% codecell
ggplot(data, aes(x='treatment', y='CVAR2') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))

# %% codecell
a = 0.05

wilcoxon(data_control["CVAR2"],data_treatment["CVAR2"])

# %% codecell
removed_outliers = data.total2.between(data.total2.quantile(.05), data.total2.quantile(.95))
data_total= data[removed_outliers]
ggplot(data_total, aes(x='treatment',y="total2" ), ) + geom_boxplot(outlier_shape = "") + geom_jitter(data_total,aes(y="total2",colour='treatment',shape='treatment') )  + ggtitle("QQ Plot of IRAK-1 expression per  GbP") + xlab("Treatment") + ylab("Total IRAK-1 Levels per Gigabase pair") + ylim(data_total.total2.quantile(.05), data_total.total2.quantile(.95))
# %% codecell
a = 0.05

wilcoxon(diff_data["diff_total2"])

# %% codecell
removed_outliers_diffData = diff_data.diff_total2.between(diff_data.diff_total2.quantile(.05), diff_data.diff_total2.quantile(.95))
difftotalData=diff_data[removed_outliers_diffData]
ggplot(difftotalData, aes( x='0',y='diff_total2') ) + geom_boxplot() + geom_point(color="red") + ylim(difftotalData.diff_total2.quantile(.05), difftotalData.diff_total2.quantile(.95)) + ggtitle("QQ Plot of changes in IRAK-1 levels per Gbp") + xlab("Treatment") + ylab("Changes in  IRAK-1 Levels per Gigabase pair")

# %% codecell
data_plot = data_treatment
controlData = data_control['total2']
controlData
# %% codecell
data_plot["ctrl_total2"]=controlData.to_list()
data_plot


# %% codecell
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(data_plot.total2.to_numpy().reshape((-1, 1)), data_plot.ctrl_total2)
r_sq= model.score(data_plot.total2.to_numpy().reshape((-1, 1)), data_plot.ctrl_total2)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
# %% codecell

ggplot(data_plot,aes(x='total2',y='ctrl_total2') )  + geom_point() + geom_smooth(method='lm')

# %% codecell

from sklearn import linear_model
lm = linear_model.LinearRegression()

# %% codecell
shapiro_test = shapiro(data_control['total2'])
shapiro_test
# %% codecell
shapiro_test = shapiro(data_treatment['total2'])
shapiro_test
# %% codecell
shapiro_test = shapiro(diff_data['diff_total2'])
shapiro_test
# %% codecell
ggplot(data, aes(x='treatment', y='totalVar') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))

# %% codecell
a = 0.05

wilcoxon(diff_data["diff_totalVar"])

# %% codecell
ggplot(data, aes(x='treatment', y='totalWT') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))

# %% codecell
a = 0.05

wilcoxon(diff_data["diff_totalWT"])

# %% codecell
ggplot(data, aes(x='treatment', y='totalA') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))

# %% codecell
a = 0.05

wilcoxon(diff_data["diff_totalA"])

# %% codecell
ggplot(data, aes(x='treatment', y='totalC') ) + geom_boxplot() + geom_jitter(data,aes(colour='treatment',shape='treatment'))

# %% codecell
a = 0.05

wilcoxon(diff_data["diff_totalC"])

# %% codecell

# %% markdown
# ## Statistics
# %% markdown
# ### Total 2 Comparison
# %% markdown
# #### Wilcoxon non-parametric
# %% codecell
a = 0.05

w, p = wilcoxon(data_control["total2"],data_treatment["total2"])
print(w, p)
# %% codecell
if (p < a):
    print("As P"+str(p)+" is less than a: "+str(a))
    print( "we reject the Null Hypothesis.")
    print(". There is significant difference betwween the groups")
else:
    print("As P"+p+" is larger than a: "+str(a))
    print( "we FAIL TO reject the Null Hypothesis.")
    print(". There is NOT a significant difference betwween the groups")
# %% markdown
# #### Freidman's Anova
# %% codecell
sp.posthoc_nemenyi_friedman(diff_data)
# %% markdown
# Friedman Tes
# %% markdown
# ### other
# %% codecell
a = 0.05

w, p = wilcoxon((data_control["totalA"]/data_control["totalC"] ),(data_treatment["totalA"]/data_treatment["totalC"]))
print(w, p)
# %% codecell
a = 0.05

w, p = wilcoxon((data_control["AVAR2"]/data_control["CVAR2"] ),(data_treatment["AVAR2"]/data_treatment["CVAR2"]))
print(w, p)
# %% codecell
a = 0.05

w, p = wilcoxon((data_control["AWT2"]/data_control["CWT2"] ),(data_treatment["AWT2"]/data_treatment["CWT2"]))
print(w, p)
# %% codecell
ggplot()+geom_histogram(procData,aes(x="tg2"))
# %% codecell
ggplot()+geom_histogram(procData,aes(x="mutant"))
# %% codecell
ggplot()+geom_bar(procData,aes(x="spliceVariant",fill="mutant"))
# %% codecell
ggplot()+geom_col(procData,aes(x="spliceVariant",y="diff_totalA/diff_totalC",fill="mutant"))
# %% codecell
a = 0.05
diff_data = procData[(data["totalC"] > 0 ) & (data["totalA"] > 0 )]
ggplot()+geom_histogram(diff_data,aes(x="tg2"))
# %% codecell

w, p = wilcoxon((diff_data["totalC"] )/(diff_data["totalA"]))
print(w, p)
# %% codecell
a = 0.05

w, p = wilcoxon(data_control["total2"],data_treatment["total2"])
print(w, p)
# %% codecell

# %% markdown
# 2 graphs
#
# 1. Do the Table
# 3. Black and white
# 3. Make sure its not sloppy
# 4.
#
# control, LPS & Difference.
#
# correlation plot for each patient - total 2 & diff_total2
#
# Look for A/C ratios
#
# ggplot(data_plot,aes(x='total2',y='ctrl_total2') )  + geom_point(colour) + geom_smooth(method='lm')
#
# %% markdown
#
# %% codecell
