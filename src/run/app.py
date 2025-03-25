import streamlit as st
import pandas as pd
from objects.app import App
import threading


def app():
    a = App()
    threading.Thread(target=a.executeApp()).start()
    
if __name__ == "__main__":
    app()