import random


class CommentaryEngine:

    def generate(self, leaders):

        templates = [
            "🔥 WHAT A MOMENT ON TRACK!",
            "🏎 DRAMA UNFOLDING AT HIGH SPEED!",
            "💥 ABSOLUTE CHAOS IN THE MIDFIELD!",
            "📡 TEAM RADIOS ARE GOING CRAZY!",
            "⚡ PURE CINEMATIC RACING ENERGY!",
            "🚀 DRS ACTIVATED!",
            "🏁 BATTLE FOR POSITION!"
        ]

        lines = []

        for driver, data in leaders:

            lines.append(
                f"{random.choice(templates)} "
                f"{driver} running at "
                f"{data['speed']:.1f} km/h"
            )

        return lines