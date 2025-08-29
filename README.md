# NWSL Research Documentation

Advanced data analysis and predictive modeling for the National Women's Soccer League.

## Live Site

Visit the documentation at: [https://research.nwsldata.com](https://research.nwsldata.com)

## Local Development

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nwsl-research.git
cd nwsl-research
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Locally

Start the development server:
```bash
mkdocs serve
```

The site will be available at `http://localhost:8000`

To use a different port:
```bash
mkdocs serve -a localhost:8001
```

### Building the Site

Build the static site:
```bash
mkdocs build
```

The built site will be in the `site/` directory.

## Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the `main` branch.

The GitHub Actions workflow handles:
1. Building the MkDocs site
2. Deploying to the `gh-pages` branch
3. Configuring the custom domain

## Adding New Research Articles

1. Create a new markdown file in the `docs/` directory:
```bash
touch docs/your-research-topic.md
```

2. Add the article to the navigation in `mkdocs.yml`:
```yaml
nav:
  - Research:
    - Your Research Topic: your-research-topic.md
```

3. Write your content using Markdown formatting

## Markdown Formatting Guidelines

### Headers
```markdown
# H1 Title
## H2 Section
### H3 Subsection
```

### Tables
```markdown
| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
```

### Code Blocks
````markdown
```python
def example():
    return "code"
```
````

### Mathematical Formulas
```markdown
$$E = mc^2$$
```

### Admonitions
```markdown
!!! note
    This is a note

!!! warning
    This is a warning
```

## Project Structure

```
nwsl-research/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions deployment
├── docs/
│   ├── index.md                # Homepage
│   ├── *.md                    # Research articles
│   ├── stylesheets/
│   │   └── extra.css           # Custom styles
│   └── javascripts/
│       └── extra.js            # Custom JavaScript
├── mkdocs.yml                  # MkDocs configuration
├── requirements.txt            # Python dependencies
├── CNAME                       # Custom domain
└── README.md                   # This file
```

## Custom Domain Setup

1. The `CNAME` file contains: `research.nwsldata.com`
2. Configure DNS with your domain provider:
   - Add a CNAME record pointing to `yourusername.github.io`
3. Enable GitHub Pages in repository settings
4. Select source as GitHub Actions

## Features

- Material for MkDocs theme
- Search functionality
- Dark/light mode toggle
- Code syntax highlighting
- Mathematical formula support
- Responsive design
- Automatic deployment

## Troubleshooting

### Build Errors
- Check `mkdocs.yml` for syntax errors
- Ensure all referenced files exist
- Verify Python dependencies are installed

### Deployment Issues
- Check GitHub Actions logs
- Verify repository settings for Pages
- Ensure CNAME file is correct

## Contributing

1. Create a feature branch
2. Make your changes
3. Test locally with `mkdocs serve`
4. Submit a pull request

## License

[Your License Here]

## Links

- [Main NWSL Data Site](https://nwsldata.com)
- [NWSL Data Platform](https://platform.nwsldata.com)
- [GitHub Repository](https://github.com/yourusername/nwsl-research)