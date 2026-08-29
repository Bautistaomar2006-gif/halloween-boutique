import streamlit as st
import pandas as pd

# 1. PAGE CONFIGURATION & INTENSE SPIRIT HALLOWEEN THEME STYLING
st.set_page_config(page_title="The Spirit Costume Zone", page_icon="🎃", layout="wide")

st.markdown("""
    <style>
    /* Spirit Halloween vibrant neon yellow background with creepy overlay texture */
    .main { 
        background-color: #FFD200; 
        color: #111111;
        background-image: radial-gradient(rgba(0,0,0,0.06) 15%, transparent 16%);
        background-size: 24px 24px;
    }
    
    /* Bold Crimson Red Impact Headers */
    h1, h2, h3 { 
        color: #D6001C !important; 
        font-family: 'Impact', 'Arial Black', sans-serif; 
        text-transform: uppercase; 
        letter-spacing: 2px;
        margin-bottom: 2px;
    }
    
    /* Promotional Scarcity Banner Line */
    .promo-banner {
        background-color: #111111; color: #FFD200; padding: 15px; 
        text-align: center; font-weight: bold; font-family: 'Impact', sans-serif;
        font-size: 24px; border-bottom: 6px solid #D6001C; letter-spacing: 2px;
    }
    
    /* Dark haunted contrast styling for product cards */
    .product-card {
        background-color: #111111; padding: 25px; border-radius: 0px;
        border: 4px solid #D6001C; margin-bottom: 30px; text-align: center;
        color: #FFFFFF;
        box-shadow: 0px 12px 30px rgba(214, 0, 28, 0.45);
        transition: transform 0.2s;
    }
    .product-card:hover {
        transform: scale(1.02);
    }
    
    /* Spirit Halloween Theme Buttons */
    .stButton>button { 
        background-color: #D6001C; color: #FFFFFF; border-radius: 0px; 
        font-weight: bold; font-family: 'Impact', sans-serif; border: none; 
        width: 100%; height: 55px; font-size: 24px; letter-spacing: 1px;
    }
    .stButton>button:hover { background-color: #A30014; color: #FFD200; border: 2px solid #FFD200; }
    
    /* Pricing Display Text Elements */
    .retail-price { color: #FFD200; font-size: 34px; font-weight: bold; font-family: 'Impact', sans-serif; margin-bottom: 0px; }
    .compare-price { color: #888888; font-size: 22px; text-decoration: line-through; margin-right: 12px; }
    
    /* Scarcity / Conversion Badges styling */
    .stock-badge { background-color: #D6001C; color: white; padding: 5px 12px; font-weight: bold; font-size: 14px; text-transform: uppercase; font-family: 'Impact', sans-serif; }
    .trend-badge { background-color: #222222; color: #FFD200; padding: 5px 12px; font-weight: bold; font-size: 14px; border: 1px solid #FFD200; }
    .size-text { color: #CCCCCC; font-size: 16px; margin-top: 5px; }
    
    /* Decorative Spooky Dividing Rules */
    .spooky-divider {
        font-size: 34px; text-align: center; margin: 25px 0; color: #111111; font-family: 'Impact', sans-serif; letter-spacing: 5px;
    }
    .section-header {
        background-color: #111111; color: #FFD200 !important; padding: 10px 20px; text-align: center; font-family: 'Impact', sans-serif; margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. EMERGENCY SCARCITY TICKER BAR
st.markdown('<div class="promo-banner">💀 WARNING: HALLOWEEN APPROACHES! USE CODE "SPOOKY20" FOR 20% OFF EXTRA & FREE INSTANT DISPATCH! 💀</div>', unsafe_allow_html=True)
st.write("")

# Main Branding Presentation Layout - FIXED: Added specific arguments to layout columns
m_col1, m_col2 = st.columns(2)
with m_col1:
    st.image("https://icons8.com", width=110)
with m_col2:
    st.title("🎃 THE HALLOWEEN COSTUME ZONE")
    st.markdown("##### *Boutique Apparel & Female Costumes Sourced Globally. Enter at your own risk...*")

st.markdown('<div class="spooky-divider">🕸️ 🦇 🕸️ 🦇 🕸️ 🦇 🕸️ 🦇 🕸️ 🦇 🕸️</div>', unsafe_allow_html=True)

# 3. LIVE DATABASE MATRIX (Featuring Your Chuangerm Alibaba Listing)
@st.cache_data
def load_inventory():
    return [
        {
            "id": "CH-1601692800505",
            "name": "Chuangerm Spot Luxury Lace Corset Dress (Built-in Shorts)",
            "img": "https://unsplash.com",  # Replace with direct Alibaba photo link later
            "compare_at": 59.99,
            "retail_price": 29.99,
            "sizes": ["XS", "S", "M", "L", "XL"],
            "checkout_url": "https://stripe.com",  # Paste your real Stripe Link here
            "tags": "Dresses",
            "stock_left": 4,
            "social_proof": "🔥 241 Claimed This Week",
            # Exact sizing matrix metrics sourced from product definitions
            "sizes_data": {
                "XS (US 0-2)": "Bust: 27.6\" | Waist: 23.6\" | Hips: 29.5\" | Length: 22.2\"",
                "S (US 2-4)": "Bust: 29.1\" | Waist: 25.2\" | Hips: 31.1\" | Length: 22.6\"",
                "M (US 6)": "Bust: 30.7\" | Waist: 26.8\" | Hips: 32.7\" | Length: 23.0\"",
                "L (US 8-10)": "Bust: 33.1\" | Waist: 29.1\" | Hips: 35.0\" | Length: 23.8\"",
                "XL (US 12)": "Bust: 35.4\" | Waist: 31.5\" | Hips: 37.4\" | Length: 24.2\""
            }
        },
        {
            "id": "HW-002",
            "name": "Luxury Velvet Midnight Siren Witch Gown",
            "img": "https://unsplash.com",
            "compare_at": 89.99,
            "retail_price": 44.99,
            "sizes": ["S", "M", "L", "XL"],
            "checkout_url": "https://stripe.com",
            "tags": "Full Costumes",
            "stock_left": 2,
            "social_proof": "🚨 Only 2 Items Left!",
            "sizes_data": {
                "S": "Standard US 4-6",
                "M": "Standard US 8-10",
                "L": "Standard US 12-14",
                "XL": "Standard US 16"
            }
        },
        {
            "id": "HW-003",
            "name": "Spellbound Dark Angel Bodysuit & Feather Set",
            "img": "https://unsplash.com",
            "compare_at": 99.99,
            "retail_price": 49.99,
            "sizes": ["S", "M", "L"],
            "checkout_url": "https://stripe.com",
            "tags": "Full Costumes",
            "stock_left": 3,
            "social_proof": "⭐ Top Trending Choice",
            "sizes_data": {
                "S": "Standard US 4-6",
                "M": "Standard US 8-10",
                "L": "Standard US 12"
            }
        }
    ]

inventory = load_inventory()

# 4. FILTER CONTROLS PANEL
st.sidebar.markdown("### 🕷️ CATALOG FILTER")
category = st.sidebar.selectbox("Choose Costume Family", ["All Apparels", "Dresses", "Full Costumes"])

filtered_items = inventory if category == "All Apparels" else [i for i in inventory if i['tags'] == category]

# 5. DYNAMIC E-COMMERCE PRODUCT GRID DISPLAY
st.markdown('<div class="section-header"><h2>🔥 LIVE PRICE MARKDOWNS — 50% OFF TODAY</h2></div>', unsafe_allow_html=True)

cols = st.columns(3)
for idx, item in enumerate(filtered_items):
    col = cols[idx % 3]
    with col:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        
        # Scarcity and Conversion Badges
        st.markdown(f'<span class="stock-badge">🚨 ONLY {item["stock_left"]} REMAINING</span> &nbsp; <span class="trend-badge">{item["social_proof"]}</span>', unsafe_allow_html=True)
        st.write("")
        
        st.image(item["img"], use_container_width=True)
        st.markdown(f"<h3>{item['name']}</h3>", unsafe_allow_html=True)
        
        # Interactive Text Size Guide Drawer
        with st.expander("📐 View Interactive Sizing Matrix"):
            for size, measurements in item["sizes_data"].items():
                st.markdown(f"**{size}:** `{measurements}`")
            st.caption("Measurements are shown in inches. Highly flexible stretch fabrics.")
        
        size_str = " | ".join(item["sizes"])
        st.markdown(f"<p class='size-text'><b>Fitments:</b> {size_str}</p>", unsafe_allow_html=True)
        
        # Dual Markup Retail Pricing Display
        st.markdown(f'<p><span class="compare-price">${item["compare_at"]:.2f}</span><span class="retail-price">${item["retail_price"]:.2f}</span></p>', unsafe_allow_html=True)
        st.markdown("<p style='color:#00FFCC; font-size:15px; font-weight:bold; margin-top:-10px;'>🔥 HALLOWEEN MARKDOWN APPLIED</p>", unsafe_allow_html=True)
        
        st.link_button("💥 SECURE ITEM NOW", item["checkout_url"])
        st.markdown('</div>', unsafe_allow_html=True)

# 6. POLICY BOTTOM TABS FOOTER
st.markdown('<div class="spooky-divider">🔮 🔮 🔮 🔮 🔮</div>', unsafe_allow_html=True)
policy_tab1, policy_tab2 = st.tabs(["📦 Spooky Delivery Timelines", "🛡️ Buyer Protection Program"])

with policy_tab1:
    st.markdown("""
    ### **Shipping Information**
    * **Dispatches:** Standard dropshipping logistics setup processes your boutique fashion items within **2-5 business days**.
    * **Arrival Window:** Expect global tracking air shipments to safely reach your doorstep inside **7-15 business days**.
    * *Note: Please place your orders early to ensure guaranteed delivery way ahead of Halloween night!*
    """)

with policy_tab2:
    st.markdown("""
    ### **Returns & Refund Framework**
    * **Defect Protections:** Damaged or incorrect items can be flagged within **30 days** of delivery for absolute order replacement settings.
    * **Sizing Notice:** Because our costumes leverage detailed custom measurements, we don't issue refunds for picking incorrect size choices. Please use our **Interactive Sizing Matrix** drawer carefully before purchasing!
    """)
