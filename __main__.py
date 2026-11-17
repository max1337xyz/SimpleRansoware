import customtkinter as ctk
from datetime import datetime
from encrypter import *
from decrypter import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class CryptorUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("CRYPTOR | Security Panel")
        self.geometry("1050x720")
        self.minsize(950, 650)

        self.configure(fg_color="#0b0b0f")

        self.create_interface()

    def create_interface(self):

        # SIDEBAR
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0,
            fg_color="#111116"
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        ctk.CTkLabel(
            self.sidebar,
            text="CRYPTOR",
            font=("Consolas", 27, "bold"),
            text_color="#e63946"
        ).pack(pady=(35, 5))

        ctk.CTkLabel(
            self.sidebar,
            text="SECURITY SIMULATOR",
            font=("Consolas", 10),
            text_color="#666670"
        ).pack(pady=(0, 45))

        self.sidebar_button("Dashboard", True)


        # SIDEBAR FOOTER
        ctk.CTkLabel(
            self.sidebar,
            text="VERSION 1.0.0\nEDUCATIONAL BUILD",
            font=("Consolas", 10),
            text_color="#55555f"
        ).pack(side="bottom", pady=25)

        # MAIN CONTENT
        self.main = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.main.pack(
            side="right",
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        # TOP HEADER
        header = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )
        header.pack(fill="x", pady=(0, 25))

        ctk.CTkLabel(
            header,
            text="Dashboard",
            font=("Segoe UI", 27, "bold"),
            text_color="#eeeeee"
        ).pack(side="left")

        ctk.CTkLabel(
            header,
            text="● SYSTEM ONLINE",
            font=("Consolas", 11, "bold"),
            text_color="#52b788"
        ).pack(side="right", pady=10)

        # STATUS CARDS
        cards = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )
        cards.pack(fill="x", pady=(0, 20))

        self.create_card(cards, "SYSTEM STATUS", "READY", "#52b788")
        self.create_card(cards, "FILES SELECTED", "00", "#eeeeee")
        self.create_card(cards, "SESSION", "ACTIVE", "#e63946")

        # FILE ENCRYPTION PANEL
        file_panel = self.create_panel(
            self.main,
            "01 / FILE SIMULATION"
        )
        file_panel.pack(fill="x", pady=(0, 18))

        ctk.CTkLabel(
            file_panel,
            text="Target filename",
            font=("Segoe UI", 12),
            text_color="#aaaaaa"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.filename = ctk.CTkEntry(
            file_panel,
            placeholder_text="Enter filename...",
            height=42,
            border_color="#34343e",
            fg_color="#111116"
        )
        self.filename.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(
            file_panel,
            text="SIMULATION PROGRESS",
            font=("Consolas", 10),
            text_color="#888888"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.progress = ctk.CTkProgressBar(
            file_panel,
            height=8,
            progress_color="#e63946",
            fg_color="#292930"
        )
        self.progress.pack(fill="x", padx=20, pady=(5, 15))
        self.progress.set(0)

        buttons = ctk.CTkFrame(
            file_panel,
            fg_color="transparent"
        )
        buttons.pack(fill="x", padx=20, pady=(0, 20))

        ctk.CTkButton(
            buttons,
            text="ENCRYPT",
            height=40,
            fg_color="#a4161a",
            hover_color="#660708",
            font=("Consolas", 12, "bold"),
            command=lambda:self.encrypt_file()
        ).pack(side="left", expand=True, fill="x", padx=(0, 8))

        ctk.CTkButton(
            buttons,
            text="RESET",
            height=40,
            fg_color="#292930",
            hover_color="#393942",
            font=("Consolas", 12, "bold"),
            command=self.reset
        ).pack(side="left", expand=True, fill="x", padx=(8, 0))

        # DECRYPTION PANEL
        decrypt_panel = self.create_panel(
            self.main,
            "02 / DECRYPTION KEY"
        )
        decrypt_panel.pack(fill="x", pady=(0, 18))

        self.key_entry = ctk.CTkEntry(
            decrypt_panel,
            placeholder_text="Enter your decryption key...",
            height=42,
            show="*",
            border_color="#34343e",
            fg_color="#111116"
        )
        self.key_entry.pack(
            fill="x",
            padx=20,
            pady=(15, 12)
        )

        ctk.CTkButton(
            decrypt_panel,
            text="DECRYPT",
            height=38,
            fg_color="#386641",
            hover_color="#2d5235",
            font=("Consolas", 12, "bold"),
            command=lambda: self.decrypt_file()
        ).pack(fill="x", padx=20, pady=(0, 18))

        # TERMINAL
        terminal_panel = self.create_panel(
            self.main,
            "03 / SYSTEM LOG"
        )
        terminal_panel.pack(fill="both", expand=True)

        self.terminal = ctk.CTkTextbox(
            terminal_panel,
            fg_color="#09090c",
            text_color="#52b788",
            font=("Consolas", 11),
            height=100,
            border_width=0
        )
        self.terminal.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        self.log("CRYPTOR interface initialized.")
        self.log("Simulation environment ready.")
        self.log("Waiting for user interaction...")

    def sidebar_button(self, text, active=False):

        ctk.CTkButton(
            self.sidebar,
            text=text,
            anchor="w",
            height=42,
            corner_radius=6,
            fg_color="#292930" if active else "transparent",
            hover_color="#292930",
            text_color="#e63946" if active else "#aaaaaa",
            font=("Segoe UI", 12),
            command=lambda: self.log(f"Navigation: {text}")
        ).pack(fill="x", padx=15, pady=4)
    def encrypt_file(self):
        self.log(f'File {self.filename.get()} Crypted')
        encrypt(self.filename.get())
        self.progress.set(1)
    def decrypt_file(self):
        self.log(f'File {self.filename.get()} DeCrypted')
        decrypt(self.filename.get()+ '.ransoware')
        self.progress.set(0)
    def create_card(self, parent, title, value, color):

        card = ctk.CTkFrame(
            parent,
            fg_color="#17171e",
            corner_radius=10
        )
        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=("Consolas", 10),
            text_color="#777780"
        ).pack(anchor="w", padx=15, pady=(15, 5))

        ctk.CTkLabel(
            card,
            text=value,
            font=("Consolas", 19, "bold"),
            text_color=color
        ).pack(anchor="w", padx=15, pady=(0, 15))

    def create_panel(self, parent, title):

        panel = ctk.CTkFrame(
            parent,
            fg_color="#17171e",
            corner_radius=10
        )

        ctk.CTkLabel(
            panel,
            text=title,
            font=("Consolas", 12, "bold"),
            text_color="#e63946"
        ).pack(anchor="w", padx=20, pady=(15, 0))

        return panel

    def log(self, message):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.terminal.insert(
            "end",
            f"[{timestamp}] {message}\n"
        )

        self.terminal.see("end")

    def reset(self):

        self.filename.delete(0, "end")
        self.key_entry.delete(0, "end")
        self.progress.set(0)

        self.log("Interface fields reset.")


if __name__ == "__main__":

    app = CryptorUI()
    app.mainloop()