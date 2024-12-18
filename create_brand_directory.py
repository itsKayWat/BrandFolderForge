import os
from datetime import datetime

def create_directory_structure():
    # Base directory - Generic name for any brand
    base_dir = "Brand_Directory"
    
    # Main structure
    structure = {
        "Website": {
            "Pages": {
                "Home": {"images", "scripts", "styles"},
                "Book_Here": {"images", "scripts", "styles"},
                "Sign_up": {"images", "scripts", "styles"},
                "Services": {"images", "scripts", "styles"},
                "Book_Now": {"images", "scripts", "styles"}
            },
            "Assets": {
                "fonts",
                "global_styles",
                "global_scripts",
                "icons",
                "logos"
            }
        },
        "Staff_Portal": {
            "Pages": {
                "Login": {"images", "scripts", "styles"},
                "Dashboard": {"images", "scripts", "styles"},
                "Work_Orders": {"images", "scripts", "styles"},
                "Inventory": {"images", "scripts", "styles"},
                "Reports": {"images", "scripts", "styles"},
                "Store": {"images", "scripts", "styles"}
            },
            "Assets": {
                "templates",
                "forms",
                "documents"
            }
        },
        "Brand_Assets": {
            "Logos": {
                "Primary",
                "Secondary",
                "Icons",
                "Favicons"
            },
            "Colors": {
                "Palettes",
                "Guidelines"
            },
            "Typography": {
                "Fonts",
                "Guidelines"
            },
            "Images": {
                "Products",
                "Team",
                "Location",
                "Services"
            }
        },
        "Marketing": {
            "Social_Media": {
                "Facebook",
                "Instagram",
                "Twitter",
                "LinkedIn"
            },
            "Print": {
                "Brochures",
                "Business_Cards",
                "Flyers",
                "Posters"
            },
            "Digital": {
                "Email_Templates",
                "Banners",
                "Ads"
            },
            "Campaigns": {
                str(datetime.now().year): {
                    "Q1", "Q2", "Q3", "Q4"
                }
            }
        },
        "Operations": {
            "Daily_Duties": {
                "Checklists",
                "Procedures",
                "Templates"
            },
            "Inventory": {
                "Stock_Lists",
                "Suppliers",
                "Order_Forms"
            },
            "Reporting": {
                "Templates",
                "Analytics",
                "KPIs"
            },
            "Store": {
                "Products",
                "Pricing",
                "Promotions"
            },
            "Training": {
                "Manuals",
                "Guides",
                "Videos"
            }
        },
        "Documentation": {
            "Brand_Guidelines",
            "Style_Guide",
            "Process_Documentation",
            "Technical_Documentation"
        }
    }

    def create_structure(base_path, structure):
        if isinstance(structure, dict):
            for key, value in structure.items():
                path = os.path.join(base_path, key)
                os.makedirs(path, exist_ok=True)
                create_structure(path, value)
        elif isinstance(structure, set):
            for item in structure:
                path = os.path.join(base_path, item)
                os.makedirs(path, exist_ok=True)

    # Create the base directory
    os.makedirs(base_dir, exist_ok=True)

    # Create the structure
    create_structure(base_dir, structure)

    # Create placeholder files with generic content
    placeholder_files = {
        "README.md": "# Brand Directory\n\nThis directory contains all brand assets and materials for your company.",
        "STRUCTURE.md": "# Directory Structure Guide\n\nDetailed explanation of the directory structure and usage guidelines.",
        ".gitignore": "# Git Ignore File\n*.DS_Store\n*.log\n*.tmp"
    }

    for filename, content in placeholder_files.items():
        with open(os.path.join(base_dir, filename), 'w') as f:
            f.write(content)

    print(f"Brand directory structure created successfully at: {os.path.abspath(base_dir)}")
    print("\nDirectory structure is ready for your brand assets!")
    print("Start by adding your assets to the appropriate folders.")

if __name__ == "__main__":
    create_directory_structure()