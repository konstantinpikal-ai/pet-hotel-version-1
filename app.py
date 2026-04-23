import streamlit as st
from datetime import date, timedelta

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🐾 Paws & Stay – Pet Hotel",
    page_icon="🐾",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
h1, h2, h3 {
    font-family: 'Playfair Display', serif;
}

/* Hero header */
.hero {
    background: linear-gradient(135deg, #1a3c34 0%, #2d6a4f 60%, #52b788 100%);
    border-radius: 18px;
    padding: 2.2rem 2rem 1.8rem;
    margin-bottom: 1.8rem;
    color: white;
    text-align: center;
}
.hero h1 {
    font-size: 2.4rem;
    margin: 0;
    letter-spacing: -0.5px;
    color: #d8f3dc;
}
.hero p {
    font-size: 1.05rem;
    margin: 0.4rem 0 0;
    color: #b7e4c7;
    font-weight: 500;
}

/* Price card */
.price-card {
    background: linear-gradient(135deg, #081c15 0%, #1b4332 100%);
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    color: #d8f3dc;
    margin-top: 0.5rem;
}
.price-card h3 {
    color: #95d5b2;
    font-size: 1.05rem;
    margin-bottom: 0.8rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    font-family: 'DM Sans', sans-serif;
    font-weight: 600;
}
.price-row {
    display: flex;
    justify-content: space-between;
    padding: 0.35rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.07);
    font-size: 0.97rem;
}
.price-row:last-child { border-bottom: none; }
.price-row .label { color: #b7e4c7; }
.price-row .value { font-weight: 600; color: #d8f3dc; }
.price-total {
    display: flex;
    justify-content: space-between;
    padding: 0.8rem 0 0;
    margin-top: 0.4rem;
    border-top: 2px solid #52b788;
    font-size: 1.3rem;
    font-weight: 700;
    color: #74c69d;
}

/* Section label */
.section-label {
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #52b788;
    margin-bottom: 0.3rem;
}

/* Confirmation banner */
.confirm-banner {
    background: #d8f3dc;
    border-left: 5px solid #2d6a4f;
    border-radius: 10px;
    padding: 1.1rem 1.4rem;
    color: #1b4332;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ── Pricing tables ────────────────────────────────────────────────────────────
BASE_RATES = {
    "Dog":    {"Small (< 10 kg)": 28, "Medium (10–25 kg)": 38, "Large (> 25 kg)": 50},
    "Cat":    {"Small (< 10 kg)": 22, "Medium (10–25 kg)": 22, "Large (> 25 kg)": 22},
    "Rabbit": {"Small (< 10 kg)": 15, "Medium (10–25 kg)": 15, "Large (> 25 kg)": 15},
    "Bird":   {"Small (< 10 kg)": 12, "Medium (10–25 kg)": 12, "Large (> 25 kg)": 12},
    "Other":  {"Small (< 10 kg)": 18, "Medium (10–25 kg)": 18, "Large (> 25 kg)": 18},
}

GROOMING_RATES = {
    "Dog":    {"Small (< 10 kg)": 25, "Medium (10–25 kg)": 35, "Large (> 25 kg)": 50},
    "Cat":    {"Small (< 10 kg)": 20, "Medium (10–25 kg)": 20, "Large (> 25 kg)": 20},
    "Rabbit": {"Small (< 10 kg)": 15, "Medium (10–25 kg)": 15, "Large (> 25 kg)": 15},
    "Bird":   {"Small (< 10 kg)":  0, "Medium (10–25 kg)":  0, "Large (> 25 kg)":  0},
    "Other":  {"Small (< 10 kg)": 15, "Medium (10–25 kg)": 15, "Large (> 25 kg)": 15},
}

WALK_RATE_PER_DAY = 8   # per walk session per day
WALK_SESSIONS = [1, 2, 3]

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>🐾 Paws &amp; Stay</h1>
  <p>Luxury pet hotel · See your price instantly</p>
</div>
""", unsafe_allow_html=True)

# ── Layout: form left, summary right ─────────────────────────────────────────
col_form, col_summary = st.columns([1.1, 0.9], gap="large")

with col_form:
    st.markdown('<div class="section-label">Your pet\'s details</div>', unsafe_allow_html=True)

    pet_name = st.text_input("Pet's name", placeholder="e.g. Bella", key="pet_name")

    col_type, col_size = st.columns(2)
    with col_type:
        pet_type = st.selectbox("Pet type", list(BASE_RATES.keys()), key="pet_type")
    with col_size:
        size_options = list(BASE_RATES[pet_type].keys())
        pet_size = st.selectbox("Size", size_options, key="pet_size")

    col_cin, col_cout = st.columns(2)
    today = date.today()
    with col_cin:
        checkin = st.date_input("Check-in", value=today + timedelta(days=1),
                                min_value=today, key="checkin")
    with col_cout:
        checkout = st.date_input("Check-out", value=today + timedelta(days=3),
                                 min_value=today + timedelta(days=1), key="checkout")

    st.markdown('<div class="section-label" style="margin-top:1.2rem">Add-ons</div>', unsafe_allow_html=True)

    grooming = st.checkbox("🛁 Grooming session (once during stay)", key="grooming")
    if pet_type in ("Bird",):
        st.caption("⚠️ Grooming not available for birds — price shown as €0.")

    walks = st.checkbox("🦮 Daily walks (dogs only)", key="walks",
                        disabled=(pet_type != "Dog"))
    if pet_type != "Dog" and walks:
        st.session_state["walks"] = False
        walks = False

    walk_sessions = 1
    if walks:
        walk_sessions = st.radio("Sessions per day", WALK_SESSIONS,
                                 horizontal=True, key="walk_sessions")

    st.markdown("---")
    book_btn = st.button("✅ Confirm Booking", use_container_width=True, type="primary")

# ── Pricing logic ─────────────────────────────────────────────────────────────
nights = max((checkout - checkin).days, 0) if checkout > checkin else 0
rate_per_night = BASE_RATES[pet_type][pet_size]
base_cost = rate_per_night * nights

grooming_cost = GROOMING_RATES[pet_type][pet_size] if grooming else 0

walk_cost = 0
if walks and pet_type == "Dog":
    walk_cost = WALK_RATE_PER_DAY * walk_sessions * nights

total = base_cost + grooming_cost + walk_cost

# ── Summary card ──────────────────────────────────────────────────────────────
with col_summary:
    st.markdown('<div class="section-label">Live booking summary</div>', unsafe_allow_html=True)

    name_display = pet_name.strip() if pet_name.strip() else "Your pet"

    rows_html = ""

    rows_html += f"""
    <div class="price-row">
        <span class="label">🐾 {name_display} · {pet_type} ({pet_size.split()[0]})</span>
        <span class="value"></span>
    </div>
    <div class="price-row">
        <span class="label">📅 Nights</span>
        <span class="value">{nights}</span>
    </div>
    <div class="price-row">
        <span class="label">🏠 Accommodation (€{rate_per_night}/night)</span>
        <span class="value">€{base_cost}</span>
    </div>
    """

    if grooming:
        rows_html += f"""
        <div class="price-row">
            <span class="label">🛁 Grooming</span>
            <span class="value">€{grooming_cost}</span>
        </div>
        """

    if walks and pet_type == "Dog":
        rows_html += f"""
        <div class="price-row">
            <span class="label">🦮 Walks ({walk_sessions}×/day × {nights} nights)</span>
            <span class="value">€{walk_cost}</span>
        </div>
        """

    rows_html += f"""
    <div class="price-total">
        <span>Total</span>
        <span>€{total}</span>
    </div>
    """

    st.markdown(
        '<div class="price-card"><h3>Booking estimate</h3>' + rows_html + '</div>',
        unsafe_allow_html=True
    )

    if nights == 0:
        st.caption("⚠️ Check-out must be after check-in.")

    # Rate reference table
    with st.expander("📋 View all nightly rates"):
        import pandas as pd
        rate_data = []
        for animal, sizes in BASE_RATES.items():
            for sz, price in sizes.items():
                rate_data.append({"Pet": animal, "Size": sz, "Rate / night": f"€{price}"})
        df = pd.DataFrame(rate_data)
        st.dataframe(df, hide_index=True, use_container_width=True)

# ── Booking confirmation ──────────────────────────────────────────────────────
if book_btn:
    if not pet_name.strip():
        st.warning("Please enter your pet's name before confirming.")
    elif nights == 0:
        st.warning("Please select valid check-in and check-out dates.")
    else:
        addons = []
        if grooming:
            addons.append("grooming")
        if walks and pet_type == "Dog":
            addons.append(f"{walk_sessions} daily walk(s)")
        addon_str = " + " + ", ".join(addons) if addons else ""

        st.markdown(f"""
        <div class="confirm-banner">
            ✅ <strong>Booking request received!</strong><br>
            <strong>{pet_name.strip()}</strong> ({pet_type}, {pet_size.split()[0]}) ·
            {checkin.strftime("%d %b")} → {checkout.strftime("%d %b %Y")} · {nights} night(s){addon_str}<br>
            <strong>Estimated total: €{total}</strong><br>
            <span style="font-size:0.9rem; opacity:0.75">We'll confirm your booking by phone or email shortly. 🐾</span>
        </div>
        """, unsafe_allow_html=True)
