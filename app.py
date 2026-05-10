import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# Personal Credentials Display
st.sidebar.title("Developer Info")
st.sidebar.write(f"**Name:** Awais Ahmad")
st.sidebar.write(f"**Roll Number:** 25-ME-108")

st.title("⚙️ Mechanical Unit Converter & Density Checker")
st.markdown("---")

# Unit Conversion Section
st.header("1. Unit Converter")
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Pressure", "Force"])

if conversion_type == "Length":
    val = st.number_input("Enter Value", value=1.0)
    unit = st.radio("Convert from:", ["Meters to Feet", "Feet to Meters"])
    if unit == "Meters to Feet":
        st.success(f"{val} m = {round(val * 3.28084, 4)} ft")
    else:
        st.success(f"{val} ft = {round(val / 3.28084, 4)} m")

elif conversion_type == "Pressure":
    val = st.number_input("Enter Value", value=1.0)
    unit = st.radio("Convert from:", ["PSI to Bar", "Bar to PSI"])
    if unit == "PSI to Bar":
        st.success(f"{val} PSI = {round(val * 0.0689476, 4)} Bar")
    else:
        st.success(f"{val} Bar = {round(val / 0.0689476, 4)} PSI")

elif conversion_type == "Force":
    val = st.number_input("Enter Value", value=1.0)
    unit = st.radio("Convert from:", ["Newton (N) to Pound-force (lbf)", "Lbf to Newton (N)"])
    if unit == "Newton (N) to Pound-force (lbf)":
        st.success(f"{val} N = {round(val * 0.224809, 4)} lbf")
    else:
        st.success(f"{val} lbf = {round(val / 0.224809, 4)} N")

st.markdown("---")

# Material Density Checker Section
st.header("2. Material Density Checker")
material_data = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Concrete": 2400,
    "Cast Iron": 7200,
    "Titanium": 4500
}

selected_material = st.selectbox("Select a Material", list(material_data.keys()))
density = material_data[selected_material]

st.info(f"The density of **{selected_material}** is approximately **{density} kg/m³**.")

# Footer with Credentials
st.markdown("---")
st.caption(f"Developed by: Awais Ahmad | Roll No: 25-ME-108")
