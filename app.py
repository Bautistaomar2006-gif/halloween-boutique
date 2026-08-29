import streamlit as st
import pandas as pd

# 1. Page Configuration & Spirit Halloween Theme Styling
st.set_page_config(page_title="The Costume Zone | Mega Deals", page_icon="🎃", layout="wide")

st.markdown("""
    <style>
    /* Spirit Halloween bright yellow background */
    .main { background-color: #FFD200; color: #111111; }
    
    /* Bold Crimson Red Headers */
    h1, h2, h3 { color: #D6001C !important; font-family: 'Impact', 'Arial Black', sans-serif; text-transform: uppercase; margin-bottom: 2px; }
    
    /* Promotional Banner Ticker Line */
    .promo-banner {
        background-color: #111111; color: #FFD200; padding: 12px; 
        text-align: center; font-weight: bold; font-family: 'Impact', sans-serif;
        font-size: 20px; border-bottom: 4px solid #D6001C; letter-spacing: 1px;
    }
    
    /* Dark contrast styling for cards */
    .product-card {
        background-color: #111111; padding: 25px; border-radius: 0px;
        border: 4px solid #D6001C; margin-bottom: 30px; text-align: center;
        color: #FFFFFF; position: relative;
    }
    
    /* Spirit Halloween Theme Buttons */
    .stButton>button { 
        background-color: #D6001C; color: #FFFFFF; border-radius: 0px; 
        font-weight: bold; font-family: 'Impact', sans-serif; border: none; 
        width: 100%; height: 55px; font-size: 22px; letter-spacing: 1px;
    }
    .stButton>button:hover { background-color: #A30014; color: #FFD200; }
    
    /* Pricing Text Variations */
    .retail-price { color: #FFD200; font-size: 28px; font-weight: bold; font-family: 'Impact', sans-serif; margin-bottom: 0px; }
    .compare-price { color: #999999; font-size: 18px; text-decoration: line-through; margin-right: 10px; }
    
    /* Urgency Badges styling */
    .stock-badge { background-color: #D6001C; color: white; padding: 4px 10px; font-weight: bold; font-size: 14px; text-transform: uppercase; }
    .trend-badge { background-color: #333333; color: #FFD200; padding: 4px 10px; font-weight: bold; font-size: 14px; border: 1px solid #FFD200; }
    .size-text { color: #CCCCCC; font-size: 15px; margin-top: 5px; }
    </style>
""", unsafe_allow_html=True)

# 2. EMERGENCY SCARCITY TOP BANNER
st.markdown('<div class="promo-banner">🚨 FLASH HALLOWEEN DEALS: USE CODE "SPOOKY20" TO CLAIM FREE SHIPPING & 20% OFF EXTRA AT CHECKOUT!</div>', unsafe_allow_html=True)
st.write("")

st.title("👻 THE HALLOWEEN COSTUME ZONE")
st.subheader("Your Ultimate Spot for Outfits & Costumes")
st.write("---")

# 3. DATA MATRIX: Boutique Female Costumes Inventory with Conversion Engine data
@st.cache_data
def load_inventory():
    return [
        {
            "id": "HW-001",
            "name": "Luxury Velvet Witch Corset Dress",
            "img": "https://unsplash.com",
            "compare_at": 79.99,
            "retail_price": 39.99,
            "sizes": ["S", "M", "L", "XL"],
            "checkout_url": "https://stripe.com",
            "tags": "Dresses",
            "stock_left": 4,
            "social_proof": "🔥 114 bought in last 24h",
            "size_guide_img": "https://unsplash.com"
        },
        {
            "id": "HW-002",
            "name": "Classic Vintage Vampire Cloak & Gown",
            "img": "https://unsplash.com",
            "compare_at": 99.95,
            "retail_price": 49.95,
            "sizes": ["M", "L", "XL"],
            "checkout_url": "https://stripe.com",
            "tags": "Full Costumes",
            "stock_left": 2,
            "social_proof": "🚨 Selling out fast!",
            "size_guide_img": "https://unsplash.com"
        },
        {
            "id": "HW-003",
            "name": "Spooky Spiderweb Mesh Cocktail Dress",
            "img": "https://unsplash.com",
            "compare_at": 59.99,
            "retail_price": 29.99,
            "sizes": ["S", "M", "L"],
            "checkout_url": "https://stripe.com",
            "tags": "Dresses",
            "stock_left": 7,
            "social_proof": "⭐ Top Trending Outfit",
            "size_guide_img": "https://unsplash.com"
        }
    ]

inventory = load_inventory()

# 4. Sidebar Filtering Options
st.sidebar.header("Filter Collection")
category = st.sidebar.selectbox("Category Selection", ["All Apparels", "Dresses", "Full Costumes"])

filtered_items = inventory if category == "All Apparels" else [i for i in inventory if i['tags'] == category]

# 5. Display Products in Columns
cols = st.columns(3)
for idx, item in enumerate(filtered_items):
    col = cols[idx % 3]
    with col:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        
        # Scarcity Indicators Layout
        st.markdown(f'<span class="stock-badge">⚠️ Only {item["stock_left"]} Left in Stock</span> &nbsp; <span class="trend-badge">{item["social_proof"]}</span>', unsafe_allow_html=True)
        st.write("")
        
        st.image(item["img"], use_container_width=True)
        st.markdown(f"<h3>{item['name']}</h3>", unsafe_allow_html=True)
        
        # 📐 EXPANDABLE SIZE GUIDE
        with st.expander("📐 View Size Guide & Measurements"):
            st.image(item["size_guide_img"], use_container_width=True)
            st.caption("Please review carefully! Costumes offer true form-fitting styles.")
        
        size_str = " | ".join(item["sizes"])
        st.markdown(f"<p class='size-text'><b>Sizes Available:</b> {size_str}</p>", unsafe_allow_html=True)
        
        # Dual Pricing Display
        st.markdown(f'<p><span class="compare-price">${item["compare_at"]:.2f}</span><span class="retail-price">${item["retail_price"]:.2f}</span></p>', unsafe_allow_html=True)
        st.markdown("<p style='color:#00FFCC; font-size:14px; margin-top:-10px; font-weight:bold;'>🎉 50% OFF FOR A LIMITED TIME ONLY</p>", unsafe_allow_html=True)
        
        st.link_button("🔥 BUY NOW", item["checkout_url"])
        st.markdown('</div>', unsafe_allow_html=True)

# 6. POLICY BOTTOM FOOTER
st.write("---")
policy_tab1, policy_tab2 = st.tabs(["📦 Shipping & Free Delivery", "🛡️ Safe Purchase Protection"])

with policy_tab1:
    st.markdown("""
    ### **Shipping Information**
    * **Processing Time:** All orders are processed and prepared within **2-5 business days** before dispatch.
    * **Delivery Estimates:** Standard shipping typically takes **7-15 business days** after processing. 
    * **Tracking:** You will receive a tracking link via email as soon as your package is scanned by the carrier.
    * *Note: Please place your orders early to ensure guaranteed delivery ahead of Halloween night!*
    """)

with policy_tab2:
    st.markdown("""
    ### **Returns & Refund Policy**
    We want you to look spectacular in your seasonal look! Please read our policy carefully:
    * **30-Day Window:** You have **30 days** from delivery to request a return if your item arrives damaged, defective, or incorrect.
    * **Sizing Policy:** Because our collection features precise sizing dimensions, we do not accept refunds for ordering the incorrect size. Please consult our **Live Size Guide** before purchasing!
    * **How to Start a Return:** Contact our support email with your order number and clear photos of any product defects.
    """)
