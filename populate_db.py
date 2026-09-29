import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 1. Initialize the Admin SDK using your service account key file
cert_path = "./service-key.json"
cred = credentials.Certificate(cert_path)
firebase_admin.initialize_app(cred)

# 2. Open a direct client connection to your Cloud Firestore database
db = firestore.client()

# 3. Define the initial multi-device catalog layout dataset
device_catalog = {
    "dream2lte": {
        "brand": "Samsung",
        "marketing_name": "Galaxy S8+ (Exynos)",
        "codename": "dream2lte",
        "supported_roms": {
            "Havoc-OS v6.0": {
                "version": "13.0",
                "download_url": "https://github.com",
                "gapps_included": True,
                "twrp_commands": [
                    "wipe system",
                    "wipe cache",
                    "wipe dalvik",
                    "install /sdcard/Havoc-OS-v6.0-20240321-dream2lte-Unofficial-GApps.zip",
                    "reboot"
                ]
            },
            "RisingOS 5.2": {
                "version": "13.0",
                "download_url": "https://github.com",
                "gapps_included": True,
                "twrp_commands": [
                    "wipe system",
                    "wipe cache",
                    "wipe dalvik",
                    "install /sdcard/RisingOS-5.2.1-COMMUNITY-dream2lte-ota.zip",
                    "reboot"
                ]
            }
        }
    }
    # Future device dictionary mappings (like 'cheeseburger', 'payton') go here!
}

def upload_catalog():
    print("⏳ Connecting to WebFlash Firestore instances...")
    
    # Target collection identifier block
    collection_ref = db.collection("devices")
    
    for codename, data in device_catalog.items():
        print(f"📦 Injecting manifest entry block for: {codename}...")
        
        # Creates or targets the document named exactly after the phone's codename
        doc_ref = collection_ref.document(codename)
        
        # Set uploads the data structure completely into the cloud node
        doc_ref.set(data)
        
    print("✅ Done! Your database is successfully populated.")

if __name__ == "__main__":
    upload_catalog()
