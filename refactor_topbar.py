with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "r") as f:
    content = f.read()

# We want to remove the block starting from "// وظیفه ۱: منوی بازشونده انتخاب انواع نمودارها"
# up to the end of the top bar Box.
import re
start_marker = "// وظیفه ۱: منوی بازشونده انتخاب انواع نمودارها"
end_marker = "                    }\n                }\n            }\n        }\n    }\n\n    // Theme Preset & Mode Selector Dialog"

# Let's find exactly how the blocks are nested.
