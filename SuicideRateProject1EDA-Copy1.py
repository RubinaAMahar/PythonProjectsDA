#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


Suicide = pd.read_csv("suiciderates.csv")
Suicide.head()


# In[5]:


Suicide.tail()


# In[6]:


Suicide.drop_duplicates(inplace=True)


# In[7]:


Suicide.shape


# In[8]:


Suicide.isna().sum()


# In[9]:


Suicide.info()


# In[10]:


Suicide["Suicides number"] = Suicide["Suicides number"].astype(int)
Suicide["Suicides number"].dtype


# In[11]:


Suicide["Adult Mortality"] = Suicide["Adult Mortality"].astype(int)
Suicide["Adult Mortality"].dtype


# In[12]:


Suicide["Country"].nunique()


# In[13]:


Suicide["Year"].nunique()


# In[14]:


Suicide["Year"].unique()


# In[15]:


Top_10_Countries = Suicide.groupby("Country")["Suicides number"].sum().sort_values(ascending=False).reset_index()
Top_10_Countries = Top_10_Countries.head(10)


# In[16]:


Top_10_Countries


# In[17]:


plt.figure(figsize=(10,6))
barplot = sns.barplot(x="Country", y="Suicides number", data=Top_10_Countries)
plt.xlabel("Country")
plt.xlabel("Total Suicides")
plt.xticks(rotation=55)
plt.title("Top 10 Countries by Total Suicides(2000 - 2011)")


# In[18]:


Average_5_countries = Suicide.groupby("Country")["Suicides number"].mean().sort_values(ascending=False).reset_index()
Average_5_countries = Average_5_countries.head(5)
Average_5_countries


# In[19]:


plt.figure(figsize=(8,8))
plt.pie(Average_5_countries["Suicides number"], labels=Average_5_countries["Country"], autopct="%1.1f%%", explode = [0.1, 0, 0,0,0])
plt.title("Average Suicide Per Country (TOP 5)")


# In[20]:


plt.figure(figsize=(10, 6))
plt.scatter(Top_10_Countries['Country'], Top_10_Countries['Suicides number'], alpha=0.5)
plt.xlabel('Country')
plt.ylabel('Suicides Number')
plt.title('Scatter Plot: Suicides Number by Country')
plt.xticks(rotation=45)
plt.show()


# In[21]:


plt.figure(figsize=(10, 6))
plt.hist(Suicide['Year'],  bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Total Suicides Number')
plt.ylabel('Frequency')
plt.title('Histogram of Total Suicides Number Years')
plt.show()


# In[22]:


Top_10_Countries = Suicide.groupby("Year")["Suicides number"].sum().sort_values(ascending=False).reset_index()
Top_10_Countries = Top_10_Countries.head(10)
Top_10_Countries


# In[23]:


plt.figure(figsize=(10, 6))
plt.scatter(Top_10_Countries['Year'], Top_10_Countries['Suicides number'], alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Suicides Number')
plt.title('Scatter Plot: Suicides Number by Year')
plt.xticks(rotation=45)
plt.show()


# In[24]:


plt.figure(figsize=(10, 6))
barplot = sns.barplot(x='Year', y='Suicides number', data=Top_10_Countries)
plt.xlabel('Year')
plt.ylabel('Total Suicides')
plt.title('Top 10 Years by Total Suicides(2000 - 2011)')


# In[25]:


avg_5_years = Suicide.groupby('Year')['Suicides number'].mean().sort_values(ascending=False).reset_index()
avg_5_years = avg_5_years.head(5)
avg_5_years


# In[26]:


plt.figure(figsize=(8, 8))
plt.pie(avg_5_years['Suicides number'], labels=avg_5_years['Year'], autopct='%1.1f%%', explode=[0.1,0,0,0,0])
plt.title('Average Suicides per Year (Top 5)')


# In[28]:


country_per_year = Suicide.groupby(['Country','Year'])['Suicides number'].sum().sort_values(ascending=False).reset_index()
country_per_year = country_per_year.head(10)
country_per_year


# In[29]:


plt.figure(figsize=(12, 8))
barplot = sns.barplot(x='Year', y='Suicides number', hue='Country', data=country_per_year)
plt.xlabel('Country')
plt.ylabel('Total Suicides')
plt.title('Total Suicides per Country in one Year (Top 10)')


# In[31]:


Suicide.head()


# In[32]:


avg_adult_death = Suicide.groupby('Country')['Adult Mortality'].mean().sort_values(ascending=False).reset_index()
avg_adult_death = avg_adult_death.head(5)
avg_adult_death


# In[33]:


plt.figure(figsize=(10, 6))
plt.scatter(avg_adult_death['Country'], avg_adult_death['Adult Mortality'], alpha=0.5)
plt.xlabel('Country')
plt.ylabel('Adult Mortality')
plt.title('Scatter Plot: Adult Mortality by Country')
plt.xticks(rotation=45)
plt.show()


# In[34]:


plt.figure(figsize=(8, 8))
plt.pie(avg_adult_death['Adult Mortality'], labels=avg_adult_death['Country'], autopct='%1.1f%%', explode=[0.1,0,0,0,0])
plt.title('Average Adult deaths top 5 Countries (per 1000)')


# In[36]:


avg_adult_death_per_year = Suicide.groupby('Year')['Adult Mortality'].mean().sort_values(ascending=False).reset_index()
avg_adult_death_per_year = avg_adult_death_per_year.head(5)
avg_adult_death_per_year


# In[37]:


plt.figure(figsize=(10, 6))
plt.scatter(avg_adult_death_per_year['Year'], avg_adult_death_per_year['Adult Mortality'], alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Adult Mortality')
plt.title('Scatter Plot: Adult Mortality by Year')
plt.xticks(rotation=45)
plt.show()


# In[38]:


plt.figure(figsize=(8, 8))
plt.pie(avg_adult_death_per_year['Adult Mortality'], labels=avg_adult_death_per_year['Year'], autopct='%1.1f%%', explode=[0.1,0,0,0,0])
plt.title('Average Adult deaths top 5 Countries (per 1000)')


# In[40]:


avg_life_expectancy = Suicide.groupby('Country')['Life expectancy'].mean().sort_values(ascending=False).reset_index()
avg_life_expectancy = avg_life_expectancy.head(5)
avg_life_expectancy


# In[41]:


plt.figure(figsize=(10, 6))
plt.scatter(avg_life_expectancy['Country'], avg_life_expectancy['Life expectancy'], alpha=0.5)
plt.xlabel('Country')
plt.ylabel('Life expectancy')
plt.title('Scatter Plot: Life expectancy by Country')
plt.xticks(rotation=45)
plt.show()


# In[42]:


plt.figure(figsize=(8, 8))
plt.pie(avg_life_expectancy['Life expectancy'], labels=avg_life_expectancy['Country'], autopct='%1.1f%%', explode=[0.1,0,0,0,0])
plt.title('Average life expectancy (top 5 Countries)')


# In[44]:


avg_infant_deaths = Suicide.groupby('Country')['Infant deaths'].mean().sort_values(ascending=False).reset_index()
avg_infant_deaths = avg_infant_deaths.head(5)
avg_infant_deaths


# In[45]:


plt.figure(figsize=(10, 6))
plt.scatter(avg_infant_deaths['Country'], avg_infant_deaths['Infant deaths'], alpha=0.5)
plt.xlabel('Country')
plt.ylabel('Infant deaths')
plt.title('Scatter Plot: Infant deaths by Country')
plt.xticks(rotation=45)
plt.show()


# In[46]:


plt.figure(figsize=(8, 8))
plt.pie(avg_infant_deaths['Infant deaths'], labels=avg_infant_deaths['Country'], autopct='%1.1f%%', explode=[0.1,0,0,0,0])
plt.title('Average infant deaths (top 5 Countries)')


# In[48]:


avg_infant_deaths_per_year = Suicide.groupby('Year')['Infant deaths'].mean().sort_values(ascending=False).reset_index()
avg_infant_deaths_per_year = avg_infant_deaths_per_year.head(5)
avg_infant_deaths_per_year


# In[49]:


plt.figure(figsize=(10, 6))
plt.scatter(avg_infant_deaths_per_year['Year'], avg_infant_deaths_per_year['Infant deaths'], alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Infant deaths')
plt.title('Scatter Plot: Infant deaths by Year')
plt.xticks(rotation=45)
plt.show()


# In[50]:


plt.figure(figsize=(8, 8))
plt.pie(avg_infant_deaths_per_year['Infant deaths'], labels=avg_infant_deaths_per_year['Year'], autopct='%1.1f%%', explode=[0.1,0,0,0,0])
plt.title('Average infant deaths (top 5 Years)')


# In[ ]:




