import streamlit as st
import pandas as pd

# 1. Page Configuration & Spooky Gothic Theme Layout
st.set_page_config(page_title="Gothic Glamour | Halloween Boutique", page_icon="🦇", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #f2f2f2; }
    h1, h2, h3 { color: #cc33ff !important; font-family: 'Georgia', serif; }
    .stButton>button { 
        background-color: #cc33ff; color: white; border-radius: 6px; 
        font-weight: bold; border: none; width: 100%; height: 45px;
    }
    .stButton>button:hover { background-color: #9900cc; color: white; }
    .product-card {
        background-color: #1a1a1a; padding: 25px; border-radius: 15px;
        border: 1px solid #2d2d2d; margin-bottom: 30px; text-align: center;
        box-shadow: 0px 4px 20px rgba(204, 51, 255, 0.15);
    }
    .price-text { color: #00ffcc; font-size: 24px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🔮 Gothic Glamour Halloween Boutique")
st.subheader("Premium Costumes & Apparels — Shipped Straight to Your Door")
st.write("---")

# 2. DATA MATRIX: MANUALLY ADD YOUR ALIBABA/ALIEXPRESS ITEMS HERE
# Simply swap out these images and names with items you find on Alibaba!
@st.cache_data
def load_alibaba_inventory():
    return [
        {
            "id": "HW-001",
            "name": "Luxury Velvet Witch Corset Dress",
            "img": "https://unsplash.com",
            "supplier_cost": 8.50,
            "retail_price": 39.99,
            "sizes": ["S", "M", "L", "XL"],
            "checkout_url": "https://stripe.com",
            "tags": "Dresses"
        },
        {
            "id": "HW-002",
            "name": "Classic Vintage Vampire Cloak & Gown",
            "img": "https://unsplash.com",
            "supplier_cost": 12.00,
            "retail_price": 49.95,
            "sizes": ["M", "L", "XL"],
            "checkout_url": "https://stripe.com",
            "tags": "Full Costumes"
        },
        {
            "id": "HW-003",
            "name": "Spooky Spiderweb Mesh Cocktail Dress",
            "img": "https://unsplash.com",
            "supplier_cost": 6.20,
            "retail_price": 29.99,
            "sizes": ["S", "M", "L"],
            "checkout_url": "https://stripe.com",
            "tags": "Dresses"
        }
    ]

inventory = load_alibaba_inventory()

# 3. Sidebar Filtering Options
st.sidebar.header("Filter Collection")
category = st.sidebar.selectbox("Category Selection", ["All Apparels", "Dresses", "Full Costumes"])
show_merchant_intel = st.sidebar.checkbox("🔒 Show My Dropship Margins", value=False)

# Margin Calculation Engine
if show_merchant_intel:
    st.sidebar.markdown("### 💸 Profit Breakdown")
    df = pd.DataFrame(inventory)
    df['Net Profit'] = df['retail_price'] - df['supplier_cost']
    st.sidebar.dataframe(df[['name', 'supplier_cost', 'retail_price', 'Net Profit']])

# Filter logic matching selection
filtered_items = inventory if category == "All Apparels" else [i for i in inventory if i['tags'] == category]

# 4. Display Products in Columns
cols = st.columns(3)
for idx, item in enumerate(filtered_items):
    col = cols[idx % 3]
    with col:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image(item["img"], use_container_width=True)
        st.markdown(f"### {item['name']}")
        
        # Display available sizes beautifully
        size_str = " | ".join(item["sizes"])
        st.markdown(f"**Sizes Available:** `{size_str}`")
        
        st.markdown(f'<p class="price-text">${item["retail_price"]:.2f}</p>', unsafe_allow_html=True)
        
        # Free Stripe / Payment link connector
        st.link_button("⚡ Claim This Look", item["checkout_url"])
        st.markdown('</div>', unsafe_allow_html=True)
