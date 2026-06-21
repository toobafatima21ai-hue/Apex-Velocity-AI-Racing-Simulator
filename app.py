import streamlit as st
import time

from models.car import create_car
from core.realtime_engine import RealTimeEngine

from engine.camera import CameraSystem
from engine.commentary import CommentaryEngine
from engine.minimap import MiniMap


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="F1 Broadcast Simulator",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.stApp{
    background-color:#0b0f19;
}

.main-title{
    text-align:center;
    color:#00f5ff;
    font-size:48px;
    font-weight:bold;
    margin-bottom:20px;
}

.player{
    color:#00ff88;
    font-weight:bold;
    font-size:20px;
}

.ai{
    color:#f8f8f8;
    font-size:18px;
}

.metric-box{
    background:#111827;
    padding:15px;
    border-radius:10px;
    text-align:center;
    border:1px solid #1f2937;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# INITIALIZATION
# ==================================================

if "cars" not in st.session_state:

    st.session_state.cars = {

        "PLAYER": create_car("PLAYER"),
        "VOLT": create_car("VOLT"),
        "NEON": create_car("NEON"),
        "SHADOW": create_car("SHADOW"),
        "CYBER": create_car("CYBER")
    }

if "engine" not in st.session_state:

    st.session_state.engine = RealTimeEngine(
        st.session_state.cars
    )

if "camera" not in st.session_state:
    st.session_state.camera = CameraSystem()

if "commentary" not in st.session_state:
    st.session_state.commentary = CommentaryEngine()

if "minimap" not in st.session_state:
    st.session_state.minimap = MiniMap()

if "player_action" not in st.session_state:
    st.session_state.player_action = "ACCELERATE"

if "running" not in st.session_state:
    st.session_state.running = False

# ==================================================
# TITLE
# ==================================================

st.markdown(
    "<div class='main-title'>🏁 F1 BROADCAST SIMULATOR</div>",
    unsafe_allow_html=True
)

# ==================================================
# PLAYER CONTROLS
# ==================================================

st.subheader("🎮 Driver Controls")

c1, c2, c3, c4, c5 = st.columns(5)

if c1.button("⚡ Accelerate"):
    st.session_state.player_action = "ACCELERATE"

if c2.button("🚀 Nitro"):
    st.session_state.player_action = "BOOST"

if c3.button("🛡 Defend"):
    st.session_state.player_action = "DEFEND"

if c4.button("⛽ Pit Stop"):
    st.session_state.player_action = "PIT"

if c5.button("🔄 Reset Race"):

    st.session_state.clear()
    st.rerun()

st.success(
    f"Current Action: {st.session_state.player_action}"
)

# ==================================================
# CAMERA SYSTEM
# ==================================================

cam_mode = st.selectbox(
    "🎥 Camera View",
    [
        "BROADCAST",
        "LEADER",
        "PLAYER"
    ]
)

st.session_state.camera.set_mode(cam_mode)

# ==================================================
# START / PAUSE
# ==================================================

colA, colB = st.columns(2)

if colA.button("▶ START RACE"):
    st.session_state.running = True

if colB.button("⏸ PAUSE RACE"):
    st.session_state.running = False

# ==================================================
# LIVE SIMULATION
# ==================================================

placeholder = st.empty()

if st.session_state.running:

    try:

        cars = st.session_state.engine.step()

        player = cars["PLAYER"]

        action = st.session_state.player_action

        # =====================================
        # PLAYER ACTIONS
        # =====================================

        if action == "BOOST":

            player["speed"] += 5
            player["tire"] -= 1

        elif action == "ACCELERATE":

            player["speed"] += 1

        elif action == "DEFEND":

            player["speed"] = max(
                40,
                player["speed"] - 1
            )

        elif action == "PIT":

            player["tire"] = min(
                100,
                player["tire"] + 25
            )

            player["speed"] = max(
                50,
                player["speed"] - 10
            )

        # =====================================
        # CAMERA VIEW
        # =====================================

        view_cars = (
            st.session_state.camera
            .get_view(cars)
        )

        leaderboard = sorted(
            cars.items(),
            key=lambda x: -x[1]["position"]
        )

        # =====================================
        # RENDER UI
        # =====================================

        with placeholder.container():

            st.subheader(
                f"🎥 CAMERA VIEW : {cam_mode}"
            )

            # ==========================
            # TRACK MAP
            # ==========================

            st.subheader("🗺 LIVE TRACK")

            for line in (
                st.session_state.minimap
                .render(cars)
            ):
                st.text(line)

            st.divider()

            # ==========================
            # PLAYER STATUS
            # ==========================

            p = cars["PLAYER"]

            m1, m2, m3 = st.columns(3)

            with m1:
                st.metric(
                    "🚀 Speed",
                    f"{p['speed']:.1f}"
                )

            with m2:
                st.metric(
                    "🛞 Tire",
                    f"{p['tire']:.0f}%"
                )

            with m3:
                st.metric(
                    "📍 Position",
                    f"{p['position']:.1f}"
                )

            st.divider()

            # ==========================
            # LEADERBOARD
            # ==========================

            st.subheader("🏆 LEADERBOARD")

            for pos, (name, car) in enumerate(
                leaderboard,
                start=1
            ):

                if name == "PLAYER":

                    st.markdown(
                        f"<div class='player'>"
                        f"{pos}. {name}"
                        f" | Speed {car['speed']:.1f}"
                        f" | Tire {car['tire']:.0f}%"
                        f" | Position {car['position']:.1f}"
                        f"</div>",
                        unsafe_allow_html=True
                    )

                else:

                    st.markdown(
                        f"<div class='ai'>"
                        f"{pos}. {name}"
                        f" | Speed {car['speed']:.1f}"
                        f" | Tire {car['tire']:.0f}%"
                        f" | Position {car['position']:.1f}"
                        f"</div>",
                        unsafe_allow_html=True
                    )

            st.divider()

            # ==========================
            # COMMENTARY
            # ==========================

            st.subheader("📡 LIVE COMMENTARY")

            commentary = (
                st.session_state.commentary
                .generate(
                    leaderboard[:3]
                )
            )

            for line in commentary:
                st.write("🎙", line)

        time.sleep(0.1)

        st.rerun()

    except Exception as e:

        st.error(
            f"Race Engine Error: {e}"
        )

        st.session_state.running = False