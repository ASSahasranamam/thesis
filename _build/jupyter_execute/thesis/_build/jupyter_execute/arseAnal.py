import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from plotnine import *
from scipy.stats import *
import scikit_posthocs   as sp
data = pd.read_csv("./NewCols.csv")
dataControl = pd.read_csv("./control.csv")
dataLps= pd.read_csv("./lps.csv")
diffData = pd.read_csv("./diffData.csv")



## TOTAL2

removed_outliers = data.total2.between(data.total2.quantile(.05), data.total2.quantile(.95))
data_total= data[removed_outliers]
ggplot(data_total, aes(x='treatment',y="total2" ), ) + geom_boxplot(outlier_shape = "") + geom_jitter(data_total,aes(y="total2",colour='treatment',shape='treatment') )  + ggtitle("QQ Plot of IRAK-1 expression per  GbP") + xlab("Treatment") + ylab("Total IRAK-1 Levels per Gigabase pair") + ylim(data_total.total2.quantile(.05), data_total.total2.quantile(.95))

a = 0.05

wilcoxon(diffData["diff_total2"])


removed_outliers_diffData = diff_data.diff_total2.between(diff_data.diff_total2.quantile(.05), diff_data.diff_total2.quantile(.95))
difftotalData=diff_data[removed_outliers_diffData]
ggplot(difftotalData, aes( x='0',y='diff_total2') ) + geom_boxplot() + geom_point(color="red") + ylim(difftotalData.diff_total2.quantile(.05), difftotalData.diff_total2.quantile(.95)) + ggtitle("QQ Plot of changes in IRAK-1 levels per Gbp") + xlab("Treatment") + ylab("Changes in  IRAK-1 Levels per Gigabase pair") 



from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(dataLps.total2.to_numpy().reshape((-1, 1)), dataControl.total2)
r_sq= model.score(dataLps.total2.to_numpy().reshape((-1, 1)), dataControl.total2)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

## - A


removed_outliers = data.total2.between(data.total2.quantile(.05), data.total2.quantile(.95))
data_total= data[removed_outliers]
ggplot(data_total, aes(x='treatment',y="total2" ), ) + geom_boxplot(outlier_shape = "") + geom_jitter(data_total,aes(y="total2",colour='treatment',shape='treatment') )  + ggtitle("QQ Plot of IRAK-1 expression per  GbP") + xlab("Treatment") + ylab("Total IRAK-1 Levels per Gigabase pair") + ylim(data_total.total2.quantile(.05), data_total.total2.quantile(.95))

removed_outliers_diffData = diff_data.diff_total2.between(diff_data.diff_total2.quantile(.05), diff_data.diff_total2.quantile(.95))
difftotalData=diff_data[removed_outliers_diffData]
ggplot(difftotalData, aes( x='0',y='diff_total2') ) + geom_boxplot() + geom_point(color="red") + ylim(difftotalData.diff_total2.quantile(.05), difftotalData.diff_total2.quantile(.95)) + ggtitle("QQ Plot of changes in IRAK-1 levels per Gbp") + xlab("Treatment") + ylab("Changes in  IRAK-1 Levels per Gigabase pair") 



from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(dataLps.total2.to_numpy().reshape((-1, 1)), dataControl.total2)
r_sq= model.score(dataLps.total2.to_numpy().reshape((-1, 1)), dataControl.total2)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)