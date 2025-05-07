# 🤝 Contributing to TiamaT

Thank you for your interest in contributing to **TiamaT** — a modular, open, and evolving pipeline for image annotation and model training.

Your feedback, suggestions, and contributions are always welcome 🙏

---

## 🚀 How to Contribute

### 🐛 Found a bug?
- Open an issue with a **clear title** and a **step-by-step description** of how to reproduce it.
- Include error messages, screenshots, or relevant snippets if possible.

### 💡 Have an idea or improvement?
- Feel free to open a feature request via an issue or discussion.
- Suggestions for improving usability, flexibility, or performance are appreciated!

### 🔧 Want to contribute code or notebooks?
1. Fork the repository
2. Create a feature branch  
   `git checkout -b feature/my-feature`
3. Commit your changes with clear messages  
   `git commit -m "Add new data export function"`
4. Push to your fork  
   `git push origin feature/my-feature`
5. Open a pull request (PR) and describe your contribution

---

## 📐 Guidelines

- Stick to the folder and variable naming conventions defined in the [README](../README.md)
- Refer to [pipeline_overview.md](./pipeline_overview.md) for detailed information about each pipeline stage
- Avoid hardcoding paths — use configuration variables or environment files
- Keep your code modular: reusable functions should go in `src/modules/`
- If you modify a notebook, make sure markdown cells are clear and consistent with the existing tone
- Notebooks should be runnable end-to-end (no undefined variables, broken paths, or missing data)

### ✏️ Style & Formatting

- Use clear and descriptive variable names
- Comment your code when needed (in English)
- Follow consistent indentation (e.g., 4 spaces, no mixed tabs/spaces)
- Avoid unnecessary verbosity — keep code clean and focused

---

## 🧪 Testing Your Changes

Before submitting a PR:
- Ensure the modified notebook or script runs successfully on your machine
- Double-check compatibility with the expected file structure (`project/`, `data/`, etc.)
- Update the `README.md`, docstrings, or other documentation if your changes affect usage or inputs/outputs

---

## 📬 Questions?

Feel free to reach out via GitHub [Issues](https://github.com/Chaouabti/TiamaT/issues) or [Discussions](https://github.com/Chaouabti/TiamaT/discussions) if you have questions, ideas, or need support.

Thanks again for helping improve TiamaT!

—
*Made with ❤️ by Marion Charpier*