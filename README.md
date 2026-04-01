# Supply Chain Optimization Project

## Project Overview
This project focuses on optimizing supply chain allocation between plants and warehouses under capacity constraints.

The objective is to reduce total transportation cost while ensuring demand fulfillment using a structured analytical workflow.

---

## Business Problem
We are given:
- Multiple plants with limited capacities
- Multiple warehouses with demand requirements
- Variable transportation costs between each plant and warehouse

### The challenge:
How can we allocate supply efficiently to:
- Minimize total cost
- Respect plant capacity constraints
- Fulfill demand as much as possible

---

##  Tools & Technologies
- Python (Pandas, NumPy, Plotly.express)
- SQL
- Jupyter Notebook
- Greedy Allocation Logic
- Data Validation Techniques

---

##  Project Workflow (Step-by-Step)

---

### 1. Data Preparation
- Cleaned raw datasets
- Handled missing values and inconsistencies
- Standardized entities (plants, warehouses, products)

---

### 2. Data Understanding & EDA
- Explored demand distribution across warehouses
- Analyzed cost variation between routes
- Calculated initial KPI:
  - **Total Cost (baseline metric)**

This helped define the optimization goal clearly:  
👉 minimize total transportation cost under constraints.

---

### 3. SQL Logic & Scenario Setup
- Built structured logic to simulate allocation scenarios
- Defined filtering logic to avoid duplicate allocations
- Used ranking logic (ROW_NUMBER concept) to structure best-case selection logic

👉 This step helped define how the allocation decision should behave before implementation in Python.

---

### 4. Optimization Approach (Greedy Algorithm)
We implemented a greedy allocation strategy:

- Sorted routes based on transportation cost
- Allocated supply starting from lowest-cost routes
- Ensured allocation respects plant capacity
- Updated capacity dynamically after each allocation

👉 This ensured that we always choose the most cost-efficient available option at each step.

---

### 5. Critical Issue Identified
During implementation, we discovered a major issue:

- Plant capacity was being reused incorrectly across allocations

---

### 6. Fix Applied (Capacity Tracking)
To solve this:
- Introduced dynamic capacity tracking per plant
- Updated remaining capacity after each allocation step
- Prevented over-allocation and ensured realistic constraints

---

### 7. Validation Framework
We validated the final allocation using:

- No plant exceeds capacity
- No warehouse demand is exceeded
- Allocation consistency across all records
- No invalid or negative allocations

---

## 📊 Scenario Analysis

---

###  Ideal Scenario (Unconstrained)
- No capacity limits
- Full demand is satisfied
- Represents theoretical best-case allocation
- Used as a benchmark for comparison

---

###  Constrained Scenario (Real Case)
- Plant capacities are enforced
- Greedy allocation applied
- Some demand may remain unmet due to constraints
- Reflects real-world operational limitations

---

##  Key Metrics

We evaluated the solution using:

- Total Cost (Constrained vs Ideal)
- Unmet Demand
- Allocation Efficiency

---

##  Business Insights

###  Cost Drivers
- Transportation cost differences strongly influence allocation decisions
- Low-cost routes dominate the allocation flow

---

###  Capacity Bottlenecks
- Certain plants reach capacity limits early
- This restricts flexibility in fulfilling demand

---

###  Operational Risks
- Risk of unmet demand under constrained capacity
- Over-reliance on few low-cost plants increases system fragility

---

###  Optimization Opportunities
- Improve capacity distribution across plants
- Consider advanced optimization methods beyond greedy logic
- Explore better balancing of supply vs demand distribution

---

##  Key Takeaways
- Optimization starts from clear KPI definition (Total Cost)
- Greedy approach is effective but not globally optimal
- Capacity tracking is critical for realistic modeling
- Scenario comparison provides business-level decision clarity

---

## 👤 Author
Hussein Abbas  
Data Analyst | Supply Chain Analytics | Python & SQLSupply Chain Optimization Project — Data Analyst Portfolio Case Study
