import pygame
from tkinter import *

# Create a new Browser Window
win = window.open()

# Set the Window Size
win.resize(800, 600)

# Set the Window Title
win.document.title = "Pluto"

# Load a web page
win.location = "http://google.com"

# Animation
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pluto")

# Draw Animation
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

# Navigation bar
navbar = win.document.createElement("nav")

# New Tab Button
var newTabButton = document.createElement("button");
newTabButton.innerHTML = "New Tab";
newTabButton.onclick = function() {
    window.open();
};

# Back Button
var backButton = document.createElement("button");
backButton.innerHTML = "⬅";
backButton.onclick = function() {
    window.history.back();
};

# Forward Button
var forwardButton = document.createElement("button");
forwardButton.innerHTML = "➡";
forwardButton.onclick = function() {
    window.history.forward();
};

# Reload Button
var reloadButton = document.createElement("button");
reloadButton.innerHTML = "↻";
reloadButton.onclick = function() {
    window.location.reload();
};

# Add the buttons to nav
navbar.appendChild(backButton);
navbar.appendChild(forwardButton);
navbar.appendChild(reloadButton);
navbar.appendChild(newTabButton);
