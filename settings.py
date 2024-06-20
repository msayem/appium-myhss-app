# Appium server locally
APPIUM_SERVER = True

# Mail service
SECMAIL_SERVICE = "@1secmail.com"


# TESTRAIL CONFIGURATION
TESTRAIL = {
    'host': 'https://hssit.testrail.net',
    'user': 'guilliannoc@hss.edu'
}

# BROWSERSTACK CONFIGURATION
# BROWSER_STACK = {
#     'projectName': 'MyHSS App',
#     'appiumVersion': '2.0.1',
#     'forceLocal': True,
#
#     'test': {
#         # iOS
#          # bs://41e2ffea27371301141da817e9c2b3e3f1eb238c
#          'iOSApp': 'bs://41e2ffea27371301141da817e9c2b3e3f1eb238c',# account for hss
#          # 'iOSApp': 'bs://82df50d330e1036808bf7abfe8ecd2d95370bea7',# account carlo
#         'iOSBuildVersion': 'v2.6.5 b5',
#         # Android
#         'androidApp': '',
#         'androidBuildVersion': ''
#     }
# }
BROWSER_STACK = {
    'projectName': 'MyHSS App',
    'appiumVersion': '2.0.1',
    'forceLocal': True,
    'test': {
        # iOS
        'iOSApp': 'bs://41e2ffea27371301141da817e9c2b3e3f1eb238c',  # account for hss
        # 'iOSApp': 'bs://82df50d330e1036808bf7abfe8ecd2d95370bea7',# account carlo
        'iOSBuildVersion': 'v2.6.5 b5',
        # Android
        'androidApp': '',
        'androidBuildVersion': ''
    },
    'prod': {
        # iOS
        'iOSApp': 'bs://61f113ac823c6fcd49dbe32993f7974990d187b5',  # account for hss
        'iOSBuildVersion': 'v2.6.5 b6',
        # Android
        'androidApp': '',
        'androidBuildVersion': ''
    }
}

IOS_SIMULATOR = {
    'platformVersion': '16.4',
    'device': 'iPhone 14 Pro',
    'test': {
        'app': 'dfd-ios-mvp-test.app',
        'buildVersion': 'v2.6.5 b1'
    },
    'prod': {
        'app': 'dfd-ios-mvp-prod.app',
        'buildVersion': 'v2.6.5 b1'
    },
}

IOS_REAL = {
    'udid': '00008110-000C70100C0A401E',
    'test': {
        'app': 'MyHSS-Test.ipa',
        'buildVersion': 'v2.6.5 b5'
    },
    'prod': {
        'app': 'MyHSS-PRD.ipa',
        'buildVersion': 'v2.6 b2'
    },
}

ANDROID_EMULATOR = {
    'platformName': 'Android',
    'platformVersion': '13',
    'deviceName': 'Pixel 4',
   # 'app': 'dfd_android_mvp-production.apk',
    'test': {
        'app': 'dfd_android_mvp-tst.apk',
        'buildVersion': 'v2.5 b1'
        },
    'prod': {
        'app': 'dfd_android_mvp-production.apk',
        'buildVersion': 'v2.6 b2'
        },
}

ANDROID_REAL = {
    'udid': "",
   # 'app': 'dfd_android_mvp-production.apk',
    'test': {
        'app': 'dfd_android_mvp-tst.apk',
        'buildVersion': 'v2.5 b1'
        },
    'prod': {
        'app': 'dfd_android_mvp-production.apk',
        'buildVersion': 'v2.6 b2'
        },


}
