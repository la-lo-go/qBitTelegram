def append_emoji_to_state(state):
    state_emoji_map = {
        "error": "❗",
        "missingFiles": "❌",
        "uploading": "⬆️",
        "pausedUP": "⏸️",
        "queuedUP": "🔃",
        "stalledUP": "🔄",
        "checkingUP": "✔️",
        "forcedUP": "⏫",
        "allocating": "💽",
        "downloading": "⬇️",
        "metaDL": "📚",
        "pausedDL": "⏸️",
        "queuedDL": "🔃",
        "stalledDL": "🔄",
        "checkingDL": "✔️",
        "forcedDL": "⏬",
        "checkingResumeData": "🔄",
        "moving": "🚚",
        "unknown": "❓"
    }

    return state.capitalize() + " " + state_emoji_map.get(state, "❓")