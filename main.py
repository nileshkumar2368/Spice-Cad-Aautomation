import os
import pandas as pd
import matplotlib.pyplot as plt

from parser.parse_dc import parse_dc
from parser.parse_tran import parse_transient
from analysis.metrics import calculate_delay

os.makedirs("reports", exist_ok=True)
os.makedirs("plots", exist_ok=True)

dc = parse_dc("spice_outputs/dc_iv.out")
dc.to_csv("reports/dc_iv.csv", index=False)

plt.plot(dc["VGS"], dc["IDS"])
plt.xlabel("VGS (V)")
plt.ylabel("IDS (A)")
plt.title("DC I-V Characteristics")
plt.savefig("plots/iv_curve.png")
plt.clf()

tran = parse_transient("spice_outputs/transient.out")
delay_ps = calculate_delay(tran)

summary = pd.DataFrame({
    "Metric": ["Propagation Delay (ps)"],
    "Value": [delay_ps]
})

summary.to_csv("reports/summary.csv", index=False)

print("Analysis complete. Reports and plots generated.")
