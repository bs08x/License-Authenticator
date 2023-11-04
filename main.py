import dearpygui.dearpygui as dpg
from keyauth.api import Keyauth
import hashlib
import sys

dpg.create_context()

owner = "Bt08"


def checksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


client = Keyauth(
    name="App",
    owner_id="PcHoErgz5V",
    secret="52337d5585661df0ef8fe765bd660f51ac07f8ab9f3243593b153156e520973a",
    version="1.0",
    file_hash=checksum()
)


def login():
    username = dpg.get_value("username")
    password = dpg.get_value("password")

    try:
        reply = client.login(username, password)
        if reply is True:
            dpg.show_item("popup_true_login")
            dpg.hide_item("Authentication")
        else:
            dpg.show_item("popup_false_login")
    except:
        dpg.show_item("popup_false_login")


def register():
    username = dpg.get_value("username")
    password = dpg.get_value("password")
    license_key = dpg.get_value("license_key")

    try:
        reply = client.register(username, password, license_key)
        if reply is True:
            dpg.show_item("popup_true_register")
            dpg.hide_item("Authentication")
        else:
            dpg.show_item("popup_false_register")
    except:
        dpg.show_item("popup_false_register")


with dpg.window(tag="Premium window", no_resize=True):
    dpg.add_text("Welcome.")

with dpg.window(label="Login / Register" ,tag="Authentication", width=600, height=250, no_resize=True, no_close=True, no_collapse=True, no_move=True):
    dpg.add_input_text(label="Username", tag="username")
    dpg.add_input_text(label="Password", tag="password")
    dpg.add_input_text(label="License", tag="license_key")
    with dpg.popup(dpg.last_item()):
        dpg.add_text(f"Buy? {owner}")
    dpg.add_button(label="Login", callback=login, width=100)
    dpg.add_button(label="Register", callback=register, width=100)

    with dpg.popup(dpg.last_item(), modal=True, tag="popup_true_login"):
        dpg.add_text("Successfully logged in")

    with dpg.popup(dpg.last_item(), modal=True, tag="popup_false_login"):
        dpg.add_text("Login failed")

    with dpg.popup(dpg.last_item(), modal=True, tag="popup_true_register"):
        dpg.add_text("Successfully registered")

    with dpg.popup(dpg.last_item(), modal=True, tag="popup_false_register"):
        dpg.add_text("Register failed")

dpg.create_viewport(title='Authenticator by Bt08s', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Premium window", True)
dpg.start_dearpygui()
dpg.destroy_context()
