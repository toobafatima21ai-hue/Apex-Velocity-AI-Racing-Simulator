class MiniMap:

    def render(self, cars):

        track_length = 100

        lines = []

        leaderboard = sorted(
            cars.items(),
            key=lambda x: -x[1]["position"]
        )

        for name, car in leaderboard:

            pos = int(car["position"]) % track_length

            track = ["·"] * 50

            marker = min(49, int(pos / 2))

            track[marker] = "🏎️"

            lines.append(
                f"{name:<8} | {''.join(track)}"
            )

        return lines