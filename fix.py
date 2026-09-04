with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# revert the bad edit
bad_edit = "                    }\n                }\n    if (showResetConfirm) {"
content = content.replace(bad_edit, "    if (showResetConfirm) {")

# find the place to close the tab condition
# we want to insert '                    }\n' right before the end of the scrollable column.
# Let's find:
target = """                            }
                        }
                    }
                }
            }
        }
    }

    if (showResetConfirm) {"""

# The inner column closes, then the card closes.
# So after Card closes, we should close the tab.
# Let's just find:
# "                    }\n                }\n            }\n        }\n    }\n\n    if (showResetConfirm) {"
# and insert `                    }\n` before `            }\n        }\n    }\n`
import re
content = re.sub(
    r"(\s+)\}\n\s+\}\n\s+\}\n\n\s+if \(showResetConfirm\) \{",
    r"\1}\n                    }\n                }\n            }\n\n    if (showResetConfirm) {",
    content
)

# Actually let's just use Python string operations manually to be safe.
# We can just run gradle to see the error and fix it precisely.
with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
