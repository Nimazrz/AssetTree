import re

with open("app/src/main/java/com/example/utils/AssetColorUtils.kt", "r") as f:
    content = f.read()

# I will just write a composable SharedAssetLegend in SharedViewHeader.kt instead of changing MAIN_LEGEND_ITEMS,
# because MAIN_LEGEND_ITEMS might be used in PDF generator (which needs colors).
