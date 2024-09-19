<p align="center">
  <img src="https://github.com/codereyinish/StoreRoom2/blob/main/Images/ImageText.jpg" width="100" alt="project-logo" style="border-radius: 15px; background-color: black; padding: 10px;">
</p>
</p>
<p align="center">
    <h1 align="center">IMG2TEXT_PYTESSERACT</h1>
</p>
<p align="center">
    <em>Transform Images into Text, Effortlessly and Accurately.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/codereyinish/Img2Texto?style=flat&logo=opensourceinitiative&logoColor=white&color=black" alt="license">
	<img src="https://img.shields.io/github/last-commit/codereyinish/Img2Texto?style=flat&logo=git&logoColor=white&color=black" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/codereyinish/Img2Texto?style=flat&color=black" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/codereyinish/Img2Texto?style=flat&color=black" alt="repo-language-count">
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Tesseract-OCR-4285F4?style=flat&logo=google&logoColor=white" alt="Tesseract">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/pyngrok-1DA1F2?style=flat&logo=ngrok&logoColor=white" alt="pyngrok">
  <img src="https://img.shields.io/badge/Google%20Colab-F9AB00?style=flat&logo=googlecolab&logoColor=white" alt="Google Colab">
  <img src="https://img.shields.io/badge/Google%20Drive-4285F4?style=flat&logo=googledrive&logoColor=white" alt="Google Drive">
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/VS%20Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white" alt="VS Code">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [📍 Overview](#-overview)
- [🧩 Features](#-features)
- [🗂️ Repository Structure](#️-repository-structure)
- [📦 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Usage](#-usage)
  - [🧪 Tests](#-tests)
- [🛠 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
- [🔗 Acknowledgments](#-acknowledgments)
</details>
<hr>

## 📍 Overview

The Img2Text_Pytesseract project is a robust software tool designed to convert images to text using optical character recognition (OCR) technology, facilitated by the pytesseract library(integration of  other OCR libraries is coming soon). It features a user-friendly web interface built with Streamlit, allowing users to upload images and view the extracted text. The project simplifies the process of handling various image formats and enhances text detection and organization. This makes Img2Text_Pytesseract invaluable for digitizing printed documents and making them editable and searchable, catering to both educational and professional needs.

---

## 🧩 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | Based on Python, uses pytesseract for OCR, Streamlit for UI, pillow_heif for image handling, and pyngrok for tunneling. Structured with main app and separate processing script. |
| 🔩 | **Code Quality**  | The codebase maintains high-quality standards with clear structure, comments, and well-documented code, ensuring readability and maintainability.|
| 📄 | **Documentation** | While not extensive, the code detailed documentation within the notebooks, includes inline comments  and helpful links, explaining key steps and the purpose of certain operations.|
| 🔌 | **Integrations**  | Integrates pytesseract for OCR, Streamlit for web interface, and pyngrok to expose local server to the internet. |
| 🧩 | **Modularity**    | High modularity with clear separation between image processing and user interface logic. Enhances maintainability and scalability. |
| ⚡️  | **Performance**   | Performance largely depends on pytesseract's OCR capabilities and image processing efficiency. Not benchmarked in the repository. |
| 🛡️ | **Security**      | No specific security measures or data protection techniques documented. Use of pyngrok may require security considerations. |
| 📦 | **Dependencies**  | Uses pytesseract, Streamlit, pillow_heif, and pyngrok. Dependencies are listed in `requirements.txt` for easy setup. |
| 🚀 | **Scalability**   | Scalable in terms of functionality through Streamlit and potential cloud deployment but lacks explicit scaling strategy. |
```

---

## 🗂️ Repository Structure

```sh
└── Img2Texto/
    ├── Files
    │   └── scanned_textfile
    ├── IMG2TEXTe.ipynb
    ├── app.py
    ├── image_processing.py
    └── requirements.txt
```

---

## 📦 Modules

<details closed><summary>.</summary>

| File                                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [requirements.txt](https://github.com/codereyinish/Img2Text0/blob/master/requirements.txt)       | Requirements.txt specifies dependencies essential for the Img2Text_Pytesseract project, ensuring the application can perform image processing and text extraction by utilizing libraries such as pytesseract, streamlit for web app interface, pillow_heif for image format handling, and pyngrok for public URL provisioning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [app.py](https://github.com/codereyinish/Img2Texto/blob/master/app.py)                           | App.py` serves as the user interface for the Img2Text_Pytesseract repository, utilizing Streamlit to facilitate image uploads and display extracted text. The script integrates image processing functionalities and offers a user-friendly sidebar with instructions and file upload capabilities, enhancing accessibility and interactivity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [IMG2TEXTe.ipynb](https://github.com/codereyinish/Img2Texto/blob/master/IMG2TEXTe.ipynb)         | main .ipynb file containing whole codebase |
| [image_processing.py](https://github.com/codereyinish/Img2Texto/blob/master/image_processing.py) | Image_processing.py` extracts text from images using optical character recognition (OCR) with pytesseract, processes the image for better text detection, and organizes the output text in a structured format by saving it to a file within the Img2Text_Pytesseract project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

</details>

<details closed><summary>Files</summary>

| File                                                                                                        | Summary                                                                                                                                                                                                                                                                                     |
| ---                                                                                                         | ---                                                                                                                                                                                                                                                                                         |
| [scanned_textfile](https://github.com/codereyinish/Img2Text_Pytesseract/blob/master/Files/scanned_textfile) | Contains a scanned image of a text, likely used by the Img2Text_Pytesseract repository to demonstrate or test the OCR capabilities of the system, converting image-based text into editable and searchable text. This aligns with the projects focus on image-to-text conversion processes. |

</details>

---

## 🚀 Getting Started

**System Requirements:**

**Google Collab Notebook**

### ⚙️ Installation

<h4>From <code>source</code></h4>

> 1. Clone the Img2Texto repository:
>
> ```console
> $ git clone https://github.com/codereyinish/Img2Texto
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd Img2Texto
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

### 🤖 Usage

<h4>From <code>source</code></h4>

> Run Img2Texto using the command below:
> ```console
> $ python main.py
> ```


---

## 🛠 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/codereyinish/Img2Texto/issues)**: Submit bugs found or log feature requests for the `Img2Text_Pytesseract` project.
- **[Submit Pull Requests](https://github.com/codereyinish/Img2Texto/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/codereyinish/Img2Texto/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/codereyinish/Img2Texto
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/codereyinish/Img2Text_Pytesseract/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=codereyinish/Img2Text_Pytesseract">
   </a>
</p>
</details>

---

## 🎗 License

[MIT-License](LICENSE)

---
## 🔗 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
