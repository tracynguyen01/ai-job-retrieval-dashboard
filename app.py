import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="AI Job Dashboard", layout="wide")

# -----------------------------
# File paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")

COMPARE_PATH = os.path.join(RESULTS_DIR, "algorithm_comparison.csv")
GA1_PATH = os.path.join(RESULTS_DIR, "ga_convergence_dataset1.csv")
GA2_PATH = os.path.join(RESULTS_DIR, "ga_convergence_dataset2.csv")


# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_data():
    compare_df = pd.read_csv(COMPARE_PATH)
    ga1_df = pd.read_csv(GA1_PATH)
    ga2_df = pd.read_csv(GA2_PATH)
    return compare_df, ga1_df, ga2_df


def check_required_files():
    missing = []

    for path in [COMPARE_PATH, GA1_PATH, GA2_PATH]:
        if not os.path.exists(path):
            missing.append(path)

    if missing:
        st.error("Missing required result files:")
        for m in missing:
            st.write(f"- {m}")
        st.stop()


check_required_files()
compare_df, ga1_df, ga2_df = load_data()

# -----------------------------
# Header
# -----------------------------
st.title("🚀 AI Job Retrieval & Optimization Dashboard")
st.caption("Comparative Analysis of Search & Optimization Algorithms for AI Job Retrieval")

col1, col2, col3 = st.columns(3)
col1.metric("Datasets", "2")
col2.metric("Algorithms", "3")
col3.metric("Max Jobs", "123,849")

st.markdown("---")

# -----------------------------
# Dataset Overview
# -----------------------------
st.header("📂 Dataset Overview")
st.caption("Dataset 2 enables more reliable evaluation due to richer features and larger scale.")

d1, d2 = st.columns(2)

with d1:
    st.info(
        """
        **Dataset 1**
        - 19,001 job postings
        - Older dataset
        - AI roles identified partly through proxy features
        """
    )

with d2:
    st.success(
        """
        **Dataset 2**
        - 123,849 job postings
        - Larger, more modern dataset
        - Richer salary and metadata fields
        """
    )

st.markdown("---")

# -----------------------------
# Algorithm Comparison
# -----------------------------
st.header("📊 Algorithm Comparison")
st.info("A* achieves the best balance between runtime efficiency and ranking quality, while GA provides strong optimization performance at higher computational cost.")

dataset_choice = st.selectbox(
    "Select dataset",
    ["Dataset 1", "Dataset 2"]
)

filtered_df = compare_df[compare_df["Dataset"] == dataset_choice].copy()

metric_choice = st.selectbox(
    "Select metric",
    [
        "Runtime_Seconds",
        "Memory_MB",
        "Node_Expansions",
        "Ranking_Quality",
        "Best_Avg_Salary",
        "Best_Jobs_Remaining"
    ]
)

pretty_metric = {
    "Runtime_Seconds": "Runtime (seconds)",
    "Memory_MB": "Memory (MB)",
    "Node_Expansions": "Node Expansions",
    "Ranking_Quality": "Ranking Quality",
    "Best_Avg_Salary": "Best Average Salary",
    "Best_Jobs_Remaining": "Best Jobs Remaining"
}[metric_choice]

c1, c2 = st.columns([2, 1])

with c1:
    fig = px.bar(
        filtered_df,
        x="Algorithm",
        y=metric_choice,
        title=f"{pretty_metric} - {dataset_choice}",
        text_auto=True
    )
    fig.update_layout(xaxis_title="", yaxis_title=pretty_metric)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Summary Table")
    st.dataframe(
        filtered_df[
            [
                "Algorithm",
                "Runtime_Seconds",
                "Memory_MB",
                "Node_Expansions",
                "Ranking_Quality",
                "Best_Avg_Salary",
                "Best_Jobs_Remaining"
            ]
        ],
        use_container_width=True
    )

st.markdown("---")

# -----------------------------
# GA Convergence
# -----------------------------
st.header("📈 Genetic Algorithm Convergence")
st.caption("GA quickly converges to a stable solution, with minimal improvement after early generations, indicating early optimization saturation.")

ga_dataset_choice = st.radio(
    "Select GA dataset",
    ["Dataset 1", "Dataset 2"],
    horizontal=True
)

if ga_dataset_choice == "Dataset 1":
    selected_ga_df = ga1_df
else:
    selected_ga_df = ga2_df

if "Avg_Fitness" in selected_ga_df.columns:
    ga_long = selected_ga_df.melt(
        id_vars="Generation",
        value_vars=["Best_Fitness", "Avg_Fitness"],
        var_name="Metric",
        value_name="Fitness"
    )

    fig_ga = px.line(
        ga_long,
        x="Generation",
        y="Fitness",
        color="Metric",
        markers=True,
        title=f"GA Convergence - {ga_dataset_choice}"
    )
else:
    fig_ga = px.line(
        selected_ga_df,
        x="Generation",
        y="Best_Fitness",
        markers=True,
        title=f"GA Convergence - {ga_dataset_choice}"
    )

st.plotly_chart(fig_ga, use_container_width=True)

st.markdown("---")

# -----------------------------
# Industry Insights
# -----------------------------
st.header("🧠 Industry Insights")

left, right = st.columns(2)

with left:
    st.subheader("Older Market Pattern")
    st.write("- Software Developer")
    st.write("- Web Developer")
    st.write("- C/C++ Software Engineer")
    st.write("- Core technologies: C++, SQL, Java")

with right:
    st.subheader("Modern AI Market Pattern")
    st.write("- AI/ML Data Scientist")
    st.write("- AI Infrastructure Engineer")
    st.write("- Applied AI Engineer")
    st.write("- Core technologies: Python, TensorFlow, PyTorch, cloud systems")

st.markdown(
    "👉 The analysis suggests a shift from general software roles toward specialised AI-focused positions."
)

st.markdown("---")
st.caption("Built from exported experimental outputs generated from the original notebook.")