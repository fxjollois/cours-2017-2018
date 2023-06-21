# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:27:35 2018

@author: François-XavierJollo
"""

#%%
import numpy
import pandas
import seaborn

ordis = pandas.read_csv("../Computers.csv")
ordis.head()

#%%
#Histogramme
seaborn.distplot(ordis.price)

#%%
# Boîte à moustaches
seaborn.factorplot("price", data = ordis, kind = "box")

#%%
# violin
seaborn.factorplot("price", data = ordis, kind = "violin")

#%%
# Lien entre price et var quanti (speed, hd)
seaborn.factorplot("speed", "price", data = ordis)
seaborn.jointplot("hd", "price", data = ordis, kind = "reg")

#%%
# Lien entre price et var quali (ram, cd, premium, screen)
seaborn.factorplot("ram", "price", data = ordis, kind = "box")
seaborn.factorplot("cd", "price", data = ordis, kind = "box")
seaborn.factorplot("premium", "price", data = ordis, kind = "box")
seaborn.factorplot("screen", "price", data = ordis, kind = "box")

#%%
# price ~ speed et hd
t = pandas.crosstab(pandas.cut(ordis.hd, 6, precision = 0), ordis.speed,
                    values = ordis.price, aggfunc = numpy.mean)
seaborn.heatmap(t, cmap = "Blues", cbar_kws = { 'label' : 'mean price' })

#%%
# price ~ hd et screen
seaborn.lmplot("hd", "price", data = ordis, hue = "screen", 
               col = "screen", col_wrap = 2)

#%%
# price ~ speed et premium
t = pandas.crosstab(ordis.speed, ordis.premium, 
                    values = ordis.price, aggfunc = numpy.mean)
seaborn.heatmap(t, cmap = "Blues", cbar_kws = { 'label' : 'mean price' })

seaborn.factorplot("speed", "price", data = ordis, hue = "premium")
seaborn.factorplot("speed", "price", data = ordis, hue = "premium", kind = "box")

#%%
# price ~ hd et premium
seaborn.lmplot("hd", "price", data = ordis, hue = "premium", 
               col = "premium", col_wrap = 2)

ordis2 = ordis.assign(hd_cut = pandas.cut(ordis.hd, 6))
seaborn.factorplot("hd_cut", "price", data = ordis2, hue = "premium", kind = "box")

#%%




