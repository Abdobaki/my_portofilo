from PIL import Image, ImageDraw, ImageFont

projects = [
    {
        'file': 'proj-pos-clothing.jpg',
        'title': 'Clothing POS System',
        'sub': 'Desktop Retail Point of Sale & Inventory',
        'tech': ['ELECTRON', 'REACT', 'TYPESCRIPT', 'SQLITE'],
        'color1': (15, 23, 42),
        'color2': (30, 41, 59),
        'accent': (249, 115, 22),
        'icon': 'POS & INVENTORY'
    },
    {
        'file': 'proj-skillbridge.jpg',
        'title': 'SkillBridge Platform',
        'sub': 'Student Academic & Mentorship Network',
        'tech': ['REACT', 'TYPESCRIPT', 'TAILWIND', 'SUPABASE'],
        'color1': (15, 23, 42),
        'color2': (23, 37, 84),
        'accent': (59, 130, 246),
        'icon': 'ACADEMIC COLLAB'
    },
    {
        'file': 'proj-haios.jpg',
        'title': 'HAIOS Operating System',
        'sub': 'Agency Workflow & CRM Automation Engine',
        'tech': ['GO', 'NODE.JS', 'REACT', 'SUPABASE', 'N8N'],
        'color1': (15, 23, 42),
        'color2': (4, 47, 46),
        'accent': (20, 184, 166),
        'icon': 'AGENCY WORKFLOW'
    },
    {
        'file': 'proj-gym-pos.jpg',
        'title': 'Gym Management & POS',
        'sub': 'Subscriptions, Access Control & Billing',
        'tech': ['ELECTRON', 'REACT', 'VITE', 'SQLITE'],
        'color1': (24, 24, 27),
        'color2': (39, 39, 42),
        'accent': (234, 179, 8),
        'icon': 'MEMBERSHIP & BILLING'
    },
    {
        'file': 'proj-restaurant-menu.jpg',
        'title': 'Restaurant E-Menu',
        'sub': 'QR Digital Ordering & Real-Time Menu',
        'tech': ['REACT', 'TYPESCRIPT', 'TAILWIND CSS'],
        'color1': (24, 15, 30),
        'color2': (45, 10, 40),
        'accent': (236, 72, 153),
        'icon': 'QR DIGITAL MENU'
    },
    {
        'file': 'proj-sign-language-ai.jpg',
        'title': 'Sign Language AI',
        'sub': 'Real-Time 21 Hand Landmarks & 98.9% ASL',
        'tech': ['PYTHON', 'OPENCV', 'MEDIAPIPE', 'RANDOM FOREST'],
        'color1': (15, 23, 42),
        'color2': (49, 10, 80),
        'accent': (168, 85, 247),
        'icon': 'COMPUTER VISION AI'
    }
]

W, H = 765, 440
try:
    font_lg = ImageFont.truetype('arial.ttf', 38)
    font_md = ImageFont.truetype('arial.ttf', 20)
    font_sm = ImageFont.truetype('arial.ttf', 14)
    font_tag = ImageFont.truetype('arialbd.ttf', 13)
except Exception:
    font_lg = font_md = font_sm = font_tag = ImageFont.load_default()

for p in projects:
    img = Image.new('RGB', (W, H), p['color1'])
    draw = ImageDraw.Draw(img)
    
    # Draw gradient background
    c1, c2 = p['color1'], p['color2']
    for y in range(H):
        t = y / H
        r = int(c1[0] * (1-t) + c2[0] * t)
        g = int(c1[1] * (1-t) + c2[1] * t)
        b = int(c1[2] * (1-t) + c2[2] * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))
    
    # Modern subtle grid lines
    for x in range(0, W, 40):
        draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 12), width=1)
    for y in range(0, H, 40):
        draw.line([(0, y), (W, y)], fill=(255, 255, 255, 12), width=1)
        
    # App window card mockup inside
    card_x0, card_y0 = 50, 40
    card_x1, card_y1 = W - 50, H - 40
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=16, fill=(15, 20, 30), outline=(50, 65, 85), width=1)
    
    # Window header bar
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y0 + 44], radius=16, fill=(22, 28, 42))
    draw.rectangle([card_x0, card_y0 + 30, card_x1, card_y0 + 44], fill=(22, 28, 42))
    
    # Window dot controls
    draw.ellipse([card_x0 + 16, card_y0 + 16, card_x0 + 28, card_y0 + 28], fill=(239, 68, 68))
    draw.ellipse([card_x0 + 36, card_y0 + 16, card_x0 + 48, card_y0 + 28], fill=(245, 158, 11))
    draw.ellipse([card_x0 + 56, card_y0 + 16, card_x0 + 68, card_y0 + 28], fill=(34, 197, 94))
    
    # Badge in window header
    draw.rounded_rectangle([card_x1 - 190, card_y0 + 10, card_x1 - 20, card_y0 + 34], radius=6, fill=p['accent'])
    draw.text((card_x1 - 105, card_y0 + 22), p['icon'], fill=(255, 255, 255), anchor='mm', font=font_tag)
    
    # Content inside mockup card
    draw.text((card_x0 + 36, card_y0 + 75), p['title'], fill=(255, 255, 255), font=font_lg)
    draw.text((card_x0 + 36, card_y0 + 130), p['sub'], fill=(180, 195, 215), font=font_md)
    
    # Tech tags
    tag_x = card_x0 + 36
    tag_y = card_y0 + 210
    for t in p['tech']:
        bbox = draw.textbbox((0, 0), t, font=font_tag)
        tw = bbox[2] - bbox[0] + 20
        th = 30
        draw.rounded_rectangle([tag_x, tag_y, tag_x + tw, tag_y + th], radius=6, fill=(30, 41, 59), outline=(70, 85, 110), width=1)
        draw.text((tag_x + tw//2, tag_y + th//2), t, fill=p['accent'], anchor='mm', font=font_tag)
        tag_x += tw + 10
        
    # Bottom subtitle
    draw.text((card_x0 + 36, card_y1 - 35), 'SYSTEM ARCHITECTURE // PRODUCTION-READY CODEBASE', fill=(100, 116, 139), font=font_sm)
    
    out_path = f"Portfolio/assets/images/thumbs/{p['file']}"
    img.save(out_path, quality=95)
    print("Generated:", out_path)
