import customtkinter as ctk
import json
import serial
import urllib.request

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("400x350")

address = "http://localhost:8085/data.json"
esp_bridge = None
does_it_work = False

def scan_data (node):
    if isinstance(node, dict):
        if node.get("Type") == "Temperature" and node.get("Text") == "CPU Package":
            return node.get("Value")
        if "Children" in node:
            for call_child in node["Children"]:
                answer = scan_data (call_child)
                if answer is not None:
                    return answer
                
def send_data():
    global does_it_work

    if does_it_work:
        try: 
            door = urllib.request.urlopen(address, timeout=0.5)
            raw_data = door.read()
            clean_data = json.loads(raw_data)

            raw_temp = scan_data(clean_data)

            if raw_temp:
                clean_temp = float(raw_temp.split(" ")[0].replace(",", "."))

                temperature_label.configure(text=f"{clean_temp} °C", text_color="#00ffcc")                
                
                if esp_bridge and esp_bridge.is_open:
                    data_package = str(clean_temp) + "\n"
                    esp_bridge.write(data_package.encode('utf-8'))

            app.after(1000, send_data)        

        except Exception:

            does_it_work = False

            if esp_bridge and esp_bridge.is_open:
                esp_bridge.close()
                
            temperature_label.configure(text="Libre is close!", text_color="orange")

        app.after(1000, send_data)               


def start_system():
    global esp_bridge, does_it_work

    if not does_it_work:
        try:
            esp_bridge = serial.Serial(port="COM5", baudrate=115200)
            does_it_work = True

            send_data()

        except Exception:
            temperature_label.configure(text="COM5 ERROR!", text_color="red")    

def stop_system():
    global esp_bridge, does_it_work

    does_it_work = False

    if esp_bridge and esp_bridge.is_open:
        esp_bridge.close()

    temperature_label.configure(text="System is close", text_color="red")        

temperature_label = ctk.CTkLabel(master=app, text="-- °C", font=("Arial", 55, "bold"))
temperature_label.pack(pady=20)

start_btn = ctk.CTkButton(master = app, text="START", fg_color="#2FA572", hover_color="#1D7850", command=start_system)
start_btn.pack(pady=10)

stop_btn = ctk.CTkButton(master = app, text="STOP", fg_color="#E03448", hover_color="#A32432", command=stop_system )
stop_btn.pack(pady=10)

app.mainloop()