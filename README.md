# 📸 Instagram Reel Uploader

Welcome to the Instagram Reel Uploader! This Python script allows you to automatically upload reels to your Instagram account on a daily basis. With just a few simple steps, you can sit back and let the script do the work for you.

## 🌟 Features

- 🤖 Automated daily reel uploads
- 📅 Customizable caption with an incremental day counter
- 🏷️ Hashtag support for increased visibility
- 🔒 Secure authentication using Instagram credentials

## 🚀 Getting Started

To get started with the Instagram Reel Uploader, follow these steps:

1. 📥 Clone the repository:
   ```
   git clone https://github.com/SilverCrocus/dailyinstagram.git
   ```
2. 📂 Navigate to the project directory:
   ```
   cd dailyinstagram
   ```
3. 🐍 Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
   4. 🔐 Set up your Instagram credentials:
- Create a `.env` file in the project directory
- Add the following lines to the `.env` file:
  ```
  IG_USERNAME=your_username
  IG_PASSWORD=your_password
  ```
- Replace `your_username` and `your_password` with your actual Instagram credentials

5. 🎥 Place your reel video in the `video` directory and make sure it follows the naming convention: `whatareyoudoing.mp4`

6. ▶️ Run the script:
  ```
  python main.py
  ```

Sit back and let the script upload the reel to your Instagram account! 🎉

## 📝 Customization

You can customize the caption and hashtags by modifying the following line in the `upload_reel()` function:

```python
caption = f"Day {daily_count}: What are you doing\n\n#ITZY #itzy #lia #midzy #yuna #ryujin #yeji #chaeryeong #borntobe"
```
Feel free to adjust the caption text and add or remove hashtags to suit your preferences.

📜 License
This project is licensed under the MIT License.

🙏 Acknowledgements
Special thanks to the creators of the instagrapi library for making this project possible.
