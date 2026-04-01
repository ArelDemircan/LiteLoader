import customtkinter as ctk
from yt_dlp import YoutubeDL
import os
import sys

# Mac'teki gereksiz sürüm uyarılarını susturur
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Uygulama Teması
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LiteLoader(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pencere Ayarları
        self.title("LiteLoader - Universal Downloader")
        self.geometry("600x400")

        # --- Arayüz Elemanları ---
        
        # Başlık
        self.label = ctk.CTkLabel(self, text="🚀 LiteLoader", font=("Arial", 32, "bold"))
        self.label.pack(pady=(30, 10))

        self.sub_label = ctk.CTkLabel(self, text="Fast & Simple Media Downloader", font=("Arial", 14), text_color="gray")
        self.sub_label.pack(pady=(0, 20))

        # Link Giriş Alanı
        self.url_entry = ctk.CTkEntry(self, width=450, height=40, placeholder_text="Paste YouTube or Instagram link here...")
        self.url_entry.pack(pady=10)

        # İndirme Butonu
        self.download_btn = ctk.CTkButton(self, text="DOWNLOAD NOW", font=("Arial", 16, "bold"), 
                                        width=200, height=45, command=self.start_download)
        self.download_btn.pack(pady=25)

        # Durum Mesajı
        self.status_label = ctk.CTkLabel(self, text="Ready to download", text_color="gray", font=("Arial", 12))
        self.status_label.pack(pady=10)

    def start_download(self):
        url = self.url_entry.get()
        
        if not url or url == "Paste YouTube or Instagram link here...":
            self.status_label.configure(text="❌ Please paste a valid link!", text_color="#FF6B6B")
            return

        try:
            self.status_label.configure(text="⏳ Downloading... Please wait.", text_color="#FFD93D")
            self.update()

            # İndirme klasörünü her sistemde "Downloads" (İndirilenler) yapalım
            download_path = os.path.join(os.path.expanduser("~"), "Downloads")

            ydl_opts = {
                'format': 'best',
                'outtmpl': f'{download_path}/%(title)s.%(ext)s',
                'nocheckcertificate': True,
                'quiet': True,
                'no_warnings': True,
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.status_label.configure(text="✅ Success! Check your Downloads folder.", text_color="#6BCB77")
            
        except Exception as e:
            self.status_label.configure(text="⚠️ Error: Download failed!", text_color="#FF6B6B")
            print(f"Hata detayı: {e}")

if __name__ == "__main__":
    app = LiteLoader()
    app.mainloop()