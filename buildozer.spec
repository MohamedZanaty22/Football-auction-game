
[app]
title = Football Auction
package.name = footballauction
package.domain = org.football
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 1.0
requirements = python3,kivy,sqlite3
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# إعدادات أندرويد لضمان قبول التخصيص والترخيص تلقائياً
android.api = 33
android.minapi = 21
android.sdk = 30
android.ndk = 25b
android.archs = arm64-v8a

# الموافقة التلقائية على شروط ترخيص جوجل SDK
android.accept_sdk_license = True
