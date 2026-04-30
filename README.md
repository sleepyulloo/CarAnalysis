# Best Car to Buy

A Python data analysis project that processes a real-world automobile dataset 
to identify trends across car makes, body styles, fuel types, pricing, and 
fuel efficiency — concluding with a data-driven purchase recommendation.

##  Analysis & Visualizations

- **Car Make Distribution** — Pie chart of vehicle counts by manufacturer
- **Body Style Breakdown** — Bar chart comparing sedan, hatchback, wagon, etc.
- **Fuel Type Comparison** — Horizontal bar chart of gas vs. diesel counts
- **City MPG Scatter Plot** — Distribution of city fuel efficiency across all vehicles
- **Highway MPG Scatter Plot** — Distribution of highway fuel efficiency
- **Price Line Chart** — Price frequency distribution across the dataset

##  Data Cleaning

- Drops 20 irrelevant columns (engine specs, dimensions, etc.) to focus on 
  consumer-relevant features
- Replaces missing `?` values to ensure clean aggregation

##  Key Findings

After analyzing 205 vehicles across make, body style, fuel type, and price:

- Most represented manufacturer: **Toyota**
- Most common body style: **Sedan**
- Dominant fuel type: **Gas**
- Average city MPG: computed from dataset
- Average highway MPG: computed from dataset
- Average price: **~$15,236**

> **Conclusion**: A Toyota sedan running on gasoline near the $15,236 price 
> point represents the best-value purchase based on availability, 
> body style prevalence, and average pricing in the dataset.

##  Technologies

- **Python 3**
- **Pandas** — Data loading, cleaning, and aggregation
- **Matplotlib** — All visualizations
- **NumPy** — Numerical support

## How to Run

```bash
git clone <repo-url>
cd best-car-to-buy
pip install pandas matplotlib numpy
python CarAnalysis.py
```

> Make sure `Automobile_data.csv` is in the same directory before running.

## Dataset

The [UCI Automobile Dataset](https://www.kaggle.com/datasets/toramky/automobile-dataset) 
contains 205 vehicles with attributes covering make, body style, fuel type, 
MPG, and price.