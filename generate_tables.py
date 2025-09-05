#!/usr/bin/env python3
"""
Generate markdown tables for NWSL research documentation
"""

import pandas as pd
from markdowntable import Table

def create_player_tables():
    """Create tables for Kansas City Current and North Carolina Courage hotspot players"""
    
    # Kansas City Current hotspot data
    kc_data = {
        'Name': ['Lo\'eau LaBonta', 'Kayla Sharples', 'Michelle Cooper', 'Debinha', 'Claire Hutton'],
        'Count': [10, 8, 5, 4, 4]
    }
    
    # North Carolina Courage hotspot data
    nc_data = {
        'Name': ['Tyler Lussi', 'Cortnee Vine', 'Malia Berkely', 'Maycee Bell', 'Ryan Williams'],
        'Count': [7, 6, 5, 5, 5]
    }
    
    # Create DataFrames
    kc_df = pd.DataFrame(kc_data)
    nc_df = pd.DataFrame(nc_data)
    
    # Generate markdown tables
    kc_table = markdownTable(kc_df.to_dict('records')).getMarkdown()
    nc_table = markdownTable(nc_df.to_dict('records')).getMarkdown()
    
    return kc_table, nc_table

def update_markdown_file():
    """Update the markdown file with generated tables"""
    
    kc_table, nc_table = create_player_tables()
    
    # Read current file
    with open('docs/over-under-goals-prediction.md', 'r') as f:
        content = f.read()
    
    # Create the new tables section
    tables_section = f"""

**Key Players in the Kansas City Current's Hotspot**

{kc_table}

**Key Players in the North Carolina Courage's Hotspot**

{nc_table}
"""
    
    # Find where to insert the tables (after the image)
    image_line = "![alt text](download.png)"
    if image_line in content:
        # Replace everything after the image
        parts = content.split(image_line)
        new_content = parts[0] + image_line + "\n\nFor Kansas City, their key attackers controlled the most valuable territory. For North Carolina, their key players were busiest in less threatening areas of the pitch." + tables_section
        
        # Write back to file
        with open('docs/over-under-goals-prediction.md', 'w') as f:
            f.write(new_content)
        
        print("✅ Successfully updated markdown file with generated tables")
        print("\n📊 Generated tables:")
        print("\nKansas City Current:")
        print(kc_table)
        print("\nNorth Carolina Courage:")
        print(nc_table)
    else:
        print("❌ Could not find image reference to anchor the tables")

if __name__ == "__main__":
    update_markdown_file()