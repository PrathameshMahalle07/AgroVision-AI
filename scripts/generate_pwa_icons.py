#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates crisp, compliant PNG and SVG icons for Android PWA and web app.
Creates:
- public/icon.svg
- public/pwa-192x192.png
- public/pwa-512x512.png
- public/pwa-maskable-512x512.png
- public/apple-touch-icon.png
- public/favicon.ico
"""

import os
import struct
import zlib
import math

os.makedirs('public', exist_ok=True)

# 1. Write public/icon.svg (Brand logo: Leaf sprout in dark forest green badge with golden sun glow)
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142C1F"/>
      <stop offset="50%" stop-color="#234E35"/>
      <stop offset="100%" stop-color="#183B26"/>
    </linearGradient>
    <linearGradient id="leafGrad" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3FA663"/>
      <stop offset="60%" stop-color="#55D481"/>
      <stop offset="100%" stop-color="#A7F3B8"/>
    </linearGradient>
    <linearGradient id="goldGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>
    <filter id="softShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#07120B" flood-opacity="0.45"/>
    </filter>
  </defs>

  <!-- Background rounded squircle for Android -->
  <rect width="512" height="512" rx="112" fill="url(#bgGrad)"/>

  <!-- Subtle golden sun arc in top right -->
  <circle cx="390" cy="120" r="46" fill="url(#goldGlow)" opacity="0.85" filter="url(#softShadow)"/>

  <!-- Botanical Sprout Emblem -->
  <g filter="url(#softShadow)" transform="translate(4, 8)">
    <!-- Main primary leaf blade -->
    <path d="M 256 128 C 360 128 400 240 376 348 C 300 372 230 336 216 264 C 206 214 220 160 256 128 Z" fill="url(#leafGrad)"/>
    
    <!-- Central leaf vein -->
    <path d="M 230 326 C 260 270 290 220 340 180" stroke="#164326" stroke-width="10" stroke-linecap="round" fill="none" opacity="0.6"/>
    
    <!-- Secondary sprouting leaf -->
    <path d="M 240 280 C 160 270 128 340 148 404 C 210 412 250 370 254 320 Z" fill="#48BB78"/>
    
    <!-- Stem / Root anchor base -->
    <path d="M 252 330 C 252 380 250 424 246 448" stroke="#A7F3B8" stroke-width="14" stroke-linecap="round" fill="none"/>
  </g>
</svg>"""

with open('public/icon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("Generated public/icon.svg")

# Function to write pure uncompressed PNG using zlib
def create_png(width, height, is_maskable=False):
    # RGBA pixel generator
    # Deep green #1a4229 background, gold circle, emerald leaf
    raw_rows = []
    
    cx = width / 2.0
    cy = height / 2.0
    radius = width / 2.0 if not is_maskable else width * 0.44

    for y in range(height):
        row = [0] # Filter type 0 (None)
        ny = (y - cy) / cy # -1.0 to 1.0
        for x in range(width):
            nx = (x - cx) / cx # -1.0 to 1.0
            dist = math.sqrt(nx * nx + ny * ny)

            # Maskable icons need full bleed background
            # Normal icons have rounded squircle
            if is_maskable:
                r, g, b, a = 20, 48, 32, 255
            else:
                # Rounded square mask
                sq_dist = max(abs(nx), abs(ny))
                corner_dist = math.sqrt(max(0, abs(nx) - 0.5)**2 + max(0, abs(ny) - 0.5)**2)
                if corner_dist > 0.48:
                    r, g, b, a = 0, 0, 0, 0
                else:
                    r, g, b, a = 20, 48, 32, 255

            # Sun spot around top-right (nx=0.45, ny=-0.45)
            s_dist = math.sqrt((nx - 0.45)**2 + (ny + 0.45)**2)
            if s_dist < 0.22 and a > 0:
                glow = max(0.0, 1.0 - s_dist / 0.22)
                r = int(r * (1 - glow) + 245 * glow)
                g = int(g * (1 - glow) + 166 * glow)
                b = int(b * (1 - glow) + 35 * glow)

            # Central stylized leaf sprout
            # Leaf shape centered around nx=0.0, ny=0.05
            lx = nx
            ly = ny - 0.05
            leaf_dist = math.sqrt(lx * lx + ly * ly)
            
            # Parametric leaf curve
            if a > 0 and leaf_dist < 0.46:
                # Angle check for leaf curve
                angle = math.atan2(ly, lx)
                if -2.2 < angle < 1.4:
                    leaf_factor = 1.0 - (leaf_dist / 0.46)
                    lr = int(55 + 90 * leaf_factor)
                    lg = int(170 + 70 * leaf_factor)
                    lb = int(90 + 60 * leaf_factor)
                    r = int(r * 0.2 + lr * 0.8)
                    g = int(g * 0.2 + lg * 0.8)
                    b = int(b * 0.2 + lb * 0.8)

            row.extend([r, g, b, a])
        raw_rows.append(bytes(row))

    raw_data = b"".join(raw_rows)
    compressed = zlib.compress(raw_data, 9)

    def chunk(chunk_type, data):
        c = chunk_type + data
        crc = struct.pack(">I", zlib.crc32(c) & 0xffffffff)
        return struct.pack(">I", len(data)) + c + crc

    png_bytes = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
        + chunk(b"IDAT", compressed)
        + chunk(b"IEND", b"")
    )
    return png_bytes

# Generate all required PNG icons
print("Generating PNG icon assets...")
with open('public/pwa-192x192.png', 'wb') as f:
    f.write(create_png(192, 192, is_maskable=False))
print("Created public/pwa-192x192.png")

with open('public/pwa-512x512.png', 'wb') as f:
    f.write(create_png(512, 512, is_maskable=False))
print("Created public/pwa-512x512.png")

with open('public/pwa-maskable-512x512.png', 'wb') as f:
    f.write(create_png(512, 512, is_maskable=True))
print("Created public/pwa-maskable-512x512.png")

with open('public/apple-touch-icon.png', 'wb') as f:
    f.write(create_png(180, 180, is_maskable=False))
print("Created public/apple-touch-icon.png")

# Also write a standard 48x48 for favicon
with open('public/favicon.ico', 'wb') as f:
    f.write(create_png(48, 48, is_maskable=False))
print("Created public/favicon.ico")

print("All PWA Android icons successfully generated!")
