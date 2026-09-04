import re
with open("app/src/main/java/com/example/data/model/Models.kt", "r") as f:
    content = f.read()

old_presets = """enum class AppThemePreset(
    val labelFa: String,
    val primaryHex: Long,
    val darkBgHex: Long,
    val lightBgHex: Long
) {
    NAVY_CLASSIC("سرمه‌ای", 0xFF005FB1, 0xFF090A0E, 0xFFEAEFF5),
    EMERALD_GOLD("زمردی", 0xFF059669, 0xFF061410, 0xFFEBF6EE),
    RUBY_ROYAL("یاقوتی", 0xFFE11D48, 0xFF14080B, 0xFFFBECEE),
    OCEAN_TEAL("فیروزه‌ای", 0xFF0891B2, 0xFF041217, 0xFFEBF8FA),
    PURPLE_MODERN("بنفش", 0xFF7C3AED, 0xFF0F0818, 0xFFF4ECFB),
    GRAY_NEUTRAL("خاکستری", 0xFF64748B, 0xFF111827, 0xFFF1F5F9),
    ORANGE_WARM("نارنجی", 0xFFEA580C, 0xFF1C1917, 0xFFFFF7ED),
    BROWN_EARTH("قهوه‌ای", 0xFF92400E, 0xFF1E1B18, 0xFFFEF3C7),
    WHITE_CLEAN("سفید", 0xFF9CA3AF, 0xFF171717, 0xFFFAFAFA),
    BLACK_PURE("مشکی", 0xFF3F3F46, 0xFF000000, 0xFFE4E4E7),
    YELLOW_SUN("زرد", 0xFFEAB308, 0xFF1A1500, 0xFFFEFCE8),
    PINK_ROSE("صورتی", 0xFFEC4899, 0xFF1A0811, 0xFFFDF2F8),
    CYAN_LIGHT("سایان", 0xFF06B6D4, 0xFF041214, 0xFFECFEFF),
    INDIGO_DEEP("نیلی", 0xFF4F46E5, 0xFF0B091C, 0xFFEEF2FF),
    LIME_FRESH("لیموئی", 0xFF84CC16, 0xFF0D1402, 0xFFF7FEE7),
    AMOLED_DARK("آمولد", 0xFF1E88E5, 0xFF000000, 0xFFFFFFFF)
}"""

new_presets = """enum class AppThemePreset(
    val labelFa: String,
    val primaryHex: Long,
    val darkBgHex: Long,
    val lightBgHex: Long
) {
    NAVY_CLASSIC("سرمه‌ای", 0xFF005FB1, 0xFF090A0E, 0xFFEAEFF5),
    EMERALD_GOLD("زمردی", 0xFF059669, 0xFF061410, 0xFFEBF6EE),
    RUBY_ROYAL("یاقوتی", 0xFFE11D48, 0xFF14080B, 0xFFFBECEE),
    OCEAN_TEAL("فیروزه‌ای", 0xFF0891B2, 0xFF041217, 0xFFEBF8FA),
    PURPLE_MODERN("بنفش", 0xFF7C3AED, 0xFF0F0818, 0xFFF4ECFB),
    GRAY_NEUTRAL("خاکستری", 0xFF64748B, 0xFF111827, 0xFFF1F5F9),
    GRAY_DARK("خاکستری تیره", 0xFF4B5563, 0xFF0F172A, 0xFFE2E8F0),
    GRAY_LIGHT("خاکستری روشن", 0xFF94A3B8, 0xFF1E293B, 0xFFF8FAFC),
    ORANGE_WARM("نارنجی", 0xFFEA580C, 0xFF1C1917, 0xFFFFF7ED),
    BROWN_EARTH("قهوه‌ای", 0xFF92400E, 0xFF1E1B18, 0xFFFEF3C7),
    BROWN_LIGHT("قهوه‌ای روشن", 0xFFD97706, 0xFF292524, 0xFFFEF9C3),
    WHITE_CLEAN("سفید", 0xFF9CA3AF, 0xFF171717, 0xFFFAFAFA),
    WHITE_PURE("سفید خالص", 0xFFD1D5DB, 0xFF27272A, 0xFFFFFFFF),
    BLACK_PURE("مشکی", 0xFF3F3F46, 0xFF000000, 0xFFE4E4E7),
    YELLOW_SUN("زرد", 0xFFEAB308, 0xFF1A1500, 0xFFFEFCE8),
    PINK_ROSE("صورتی", 0xFFEC4899, 0xFF1A0811, 0xFFFDF2F8),
    CYAN_LIGHT("سایان", 0xFF06B6D4, 0xFF041214, 0xFFECFEFF),
    INDIGO_DEEP("نیلی", 0xFF4F46E5, 0xFF0B091C, 0xFFEEF2FF),
    LIME_FRESH("لیموئی", 0xFF84CC16, 0xFF0D1402, 0xFFF7FEE7),
    BLUE_LIGHT("آبی روشن", 0xFF3B82F6, 0xFF0F172A, 0xFFEFF6FF),
    GREEN_LIGHT("سبز روشن", 0xFF22C55E, 0xFF064E3B, 0xFFF0FDF4),
    RED_LIGHT("قرمز روشن", 0xFFEF4444, 0xFF450A0A, 0xFFFEF2F2),
    TEAL_DEEP("کله غازی", 0xFF0F766E, 0xFF042F2E, 0xFFF0FDFA),
    AMBER_WARM("کهربایی", 0xFFF59E0B, 0xFF451A03, 0xFFFFFBEB)
}"""

content = content.replace(old_presets, new_presets)
# Wait, task 15 says "در قسمت تم amoledحذف شود" (Remove AMOLED theme)
# So I didn't include AMOLED_DARK in new_presets. Good.

with open("app/src/main/java/com/example/data/model/Models.kt", "w") as f:
    f.write(content)
