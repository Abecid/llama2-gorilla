import markdown

def main():
  # Open and read the Markdown file
  with open('Blog.md', 'r', encoding='utf-8') as f:
      markdown_content = f.read()

  # Convert the Markdown content to HTML
  html_content = markdown.markdown(markdown_content)

  # Save the HTML content to an output file (optional)
  with open('Blog.html', 'w', encoding='utf-8') as f:
      f.write(html_content)

if __name__ == "__main__":
  main()