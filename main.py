import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM
from sklearn.preprocessing import StandardScaler



df = pd.read_csv("nexus_data.csv")

features = ['Mkt_RF', 'VIX', 'Term_Spread']
X = df[features].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = GaussianHMM(n_components=2, covariance_type="full", n_iter=1000, random_state=42)
model.fit(X_scaled)

regimes = model.predict(X_scaled)

df_results = df.copy()
df_results['Regime'] = regimes

# Convert the index to actual monthly dates
df_results.index = pd.date_range(start='1990-01-31', periods=len(df_results), freq='M')

fig, ax = plt.subplots(figsize=(15, 7))

# Plot the Market Excess Returns (Mkt_RF) [cite: 137]
ax.plot(df_results.index, df_results['Mkt_RF'], color='black', lw=1, label='Market Excess Return')

# Shade the background for detected stress regimes
for i in range(len(df_results)):
    if df_results['Regime'].iloc[i] == 0: # Assuming 1 is your 'Stressed' regime
        ax.axvspan(df_results.index[i], 
                   df_results.index[i] + pd.Timedelta(days=30), 
                   color='red', alpha=0.3)

ax.set_title('Market Regimes: Shaded Areas Represent Stressed Environments')
ax.set_ylabel('Monthly Return (%)')
ax.legend()
plt.show()
# Check the average VIX for each regime
print(df_results.groupby('Regime')['VIX'].mean())

plt.plot()