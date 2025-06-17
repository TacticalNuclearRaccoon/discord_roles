# Roles Questionnaire for the Vigies Community

This project provides an interactive web application that allows users to assess their dominant roles within a community, using a questionnaire based on five profiles: Philanthropist, Socializer, Free Spirit, Disruptor, and Achiever.

## Features
- Interactive questionnaire with sliders for each question.
- Automatic calculation of scores for each role.
- Graphical display of results as a bar chart.
- Presentation of the user's top three roles.

## Main File
- **roles.py**: Contains all the code for the Streamlit app, from displaying questions to visualizing results.

## Requirements
- Python 3.7 or newer
- [Streamlit](https://streamlit.io/)
- [matplotlib](https://matplotlib.org/)

## Installation
1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd discord_roles
   ```
2. **Install dependencies**
   ```bash
   pip install streamlit matplotlib
   ```

## Running the App
In the project folder, run:
```bash
streamlit run roles.py
```

This will automatically open the app in your default web browser.

## Usage
- For each question, move the slider from 0 (not at all) to 7 (completely) according to your feelings.
- The scores for each role will be calculated and displayed, along with a bar chart and your top three roles.

## Customization
You can modify the questions or add new roles by editing the `roles.py` file.

## Help
For any questions or suggestions, please open an issue in the repository. 