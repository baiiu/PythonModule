import os

# 1. generate apk
generateApkPath = os.path.dirname(__file__) + '/' + 'apkGenerator.py'
print(generateApkPath)
os.system('python ' + generateApkPath)

#5. uploadApk
uploadApkPath = os.path.dirname(__file__) + '/' + 'apkUploader.py'
print(uploadApkPath)
os.system('python ' + uploadApkPath)
