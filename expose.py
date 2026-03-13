from pyngrok import ngrok
import time

# Expose Streamlit sur ngrok
public_url = ngrok.connect(8502, "http")
print(f"\n✅ Streamlit accessible via : {public_url}")
print(f"\nOuvrez ce lien sur votre téléphone Android :\n{public_url}\n")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Tunnel fermé")
    ngrok.kill()
