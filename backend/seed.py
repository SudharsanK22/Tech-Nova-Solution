import urllib.request
import json

works_data = [
    {
        "title": "Quantum AI Platform",
        "description": "Next-generation predictive analytics platform leveraging quantum machine learning algorithms.",
        "image_url": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=800&auto=format&fit=crop"
    },
    {
        "title": "Neon E-Commerce",
        "description": "High-performance storefront with real-time inventory and WebGL product configurator.",
        "image_url": "https://images.unsplash.com/photo-1558655146-d09347e92766?q=80&w=800&auto=format&fit=crop"
    },
    {
        "title": "CyberSec Dashboard",
        "description": "Real-time threat monitoring interface with dynamic visualizations and secure websocket integration.",
        "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800&auto=format&fit=crop"
    }
]

for work in works_data:
    try:
        req = urllib.request.Request(
            "http://localhost:8000/api/works", 
            data=json.dumps(work).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print(f"Added: {work['title']}")
            else:
                print(f"Failed to add {work['title']}: {response.status}")
    except Exception as e:
        print(f"Error adding {work['title']}. Is the backend running? Exception: {e}")
        break
