import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Custora | RFM Customer Segmentation",
    page_icon="🛍️",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/rfm_segments.csv")
    df["CustomerID"] = df["CustomerID"].astype(int).astype(str)
    return df

df = load_data()

PLAYBOOK = {
    "Champions": "Reward with VIP loyalty perks, early product access, and referral incentives. Avoid discounting.",
    "Loyal Customers": "Upsell higher-margin categories and enroll in tiered loyalty rewards.",
    "Big Spenders": "Offer personalized concierge recommendations, bundle upgrades, and VIP retention perks.",
    "Frequent Buyers": "Increase average order value (AOV) using product bundles, volume discounts, and free-shipping thresholds.",
    "Potential Loyalist": "Offer membership perks and targeted cross-sell bundles to increase order frequency.",
    "Recent Customers": "Trigger an automated 3-email onboarding sequence with a second-purchase incentive.",
    "Need Attention": "Send personalized 'We miss you' check-ins and limited-time replenishment reminders before they churn into At Risk.",
    "At Risk": "Deploy urgent win-back campaigns, time-limited offers, and customer feedback surveys.",
    "Hibernating": "Run low-cost automated re-engagement email flows; suppress from expensive paid ads.",
    "Lost": "Exclude from paid acquisition spend; include only in major seasonal clearance campaigns."
}

# Header
st.title("🛍️ Custora — RFM Customer Segmentation & Retention Dashboard")
st.markdown(
    "End-to-end customer analytics on the **UCI Online Retail Dataset (2010–2011)**. "
    "Explore RFM score distributions, revenue concentration, and targeted retention strategies."
)

# Sidebar Filters
st.sidebar.header("Filter Segments")
all_segments = sorted(df["Segment"].dropna().unique().tolist())
selected_segments = st.sidebar.multiselect(
    "Select Customer Segments:",
    options=all_segments,
    default=all_segments
)

min_spend = float(df["Monetary"].min())
max_spend = float(df["Monetary"].max())
spend_range = st.sidebar.slider(
    "Filter by Total Spend ($):",
    min_value=min_spend,
    max_value=max_spend,
    value=(min_spend, max_spend)
)

filtered_df = df[
    (df["Segment"].isin(selected_segments)) &
    (df["Monetary"].between(spend_range[0], spend_range[1]))
]

# Top KPI Cards
k1, k2, k3, k4 = st.columns(4)
k1.metric("Customers Selected", f"{len(filtered_df):,}")
k2.metric("Total Revenue", f"${filtered_df['Monetary'].sum():,.0f}")
k3.metric("Avg Spend / Customer", f"${filtered_df['Monetary'].mean():,.2f}" if len(filtered_df) else "$0.00")
k4.metric("Median Recency", f"{filtered_df['Recency'].median():.0f} days" if len(filtered_df) else "0 days")

st.divider()

# Charts Row
c1, c2 = st.columns(2)

with c1:
    st.subheader("Customer Distribution by Segment")
    seg_counts = filtered_df["Segment"].value_counts().reset_index()
    seg_counts.columns = ["Segment", "Customers"]
    fig_bar = px.bar(
        seg_counts,
        x="Segment",
        y="Customers",
        color="Segment",
        text="Customers"
    )
    fig_bar.update_layout(showlegend=False, xaxis_title="", yaxis_title="Number of Customers")
    st.plotly_chart(fig_bar, use_container_width=True)

with c2:
    st.subheader("Revenue Contribution by Segment")
    seg_rev = filtered_df.groupby("Segment")["Monetary"].sum().reset_index()
    fig_pie = px.pie(
        seg_rev,
        names="Segment",
        values="Monetary",
        hole=0.45
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Actionable Marketing Playbook
st.subheader("🎯 Segment Retention Action Plan")
target_seg = st.selectbox("Select a Segment to Inspect Strategy:", all_segments)
sub = df[df["Segment"] == target_seg]

p1, p2, p3, p4 = st.columns(4)
p1.info(f"**Customers:** {len(sub):,} ({len(sub)/len(df)*100:.1f}%)")
p2.info(f"**Avg Spend:** ${sub['Monetary'].mean():,.2f}")
p3.info(f"**Avg Frequency:** {sub['Frequency'].mean():.1f} orders")
p4.info(f"**Avg Recency:** {sub['Recency'].mean():.0f} days")

st.success(
    f"**Recommended Action for {target_seg}:** "
    f"{PLAYBOOK.get(target_seg, 'Tailor retention messaging based on recency, order frequency, and spend tier.')}"
)

# Customer Data Explorer + CSV Download
with st.expander("🔍 Explore & Export Segmented Customer Table"):
    st.dataframe(filtered_df.sort_values("Monetary", ascending=False).head(500), use_container_width=True)
    csv_export = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Filtered Customers (CSV)",
        data=csv_export,
        file_name="custora_filtered_segments.csv",
        mime="text/csv"
    )